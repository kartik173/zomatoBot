from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import Restarted, SlotSet
import zomatoAPI
import pandas as pd
import sendMail
pd.set_option('display.max_colwidth', -1)

restaurants=pd.DataFrame()

class ActionSearchRestaurants(Action):
    
    def name(self):
        return 'action_restaurant'
    
    def getResults(self, loc, cuisine):
        config={ "user_key":"a67c96823657beee597b9234eed8906d"}
        zomato = zomatoAPI.initialize_app(config)
        location_detail=zomato.get_location(loc, 1)
        if len(location_detail['location_suggestions'])==0:
            return pd.DataFrame()
        lat=location_detail["location_suggestions"][0]["latitude"]
        lng=location_detail["location_suggestions"][0]["longitude"]
        cityId=location_detail["location_suggestions"][0]["city_id"]
        cuisines_dict=zomato.get_cuisines(cityId)
    
        list1 = [0,20,40,60,80]
        results = []
        
        for i in list1:
            results+=zomato.restaurant_search("", lat, lng, str(cuisines_dict.get(cuisine)), start=i)
            
        df = pd.DataFrame(results)
        return df.sort_values(['rating'], ascending=False).reset_index()
    
    
    def budget_group(self, row):
        if row['average'] <300 :
            return 'lesser than 300'
        elif 300 <= row['average'] <700 :
            return 'between 300 to 700'
        else:
            return 'more than 700'
        
    def filterByBudget(self, df, price, top=5):
        if df.empty:
            return df
        res_filter = df.copy()
        res_filter['budget'] = res_filter.apply(lambda row: self.budget_group(row), axis=1)
        res_filter = res_filter[(res_filter.budget == price)]
        return res_filter.iloc[:top,:]
    
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        
        print("all--", loc, cuisine, price)
        res=self.getResults(loc, cuisine)
        
        global restaurants
        restaurants= self.filterByBudget(res, price, 10)
        filtered = restaurants.iloc[:5,:]
        
        print("filtered df", filtered)
        
        response=""
        if filtered.empty or len(filtered)==0:
            response= "No results found for your given search"
        else:
#            contentDf = filtered.loc[:5,['name','address','budget','rating']]
#            contentDf = contentDf.rename(columns={'name':'Restraunt Name','address':'Address',
#                                     'budget':'Average budget for two', 'rating':'Average Rating'})
#    
#            response=contentDf.to_string(index=False, justify='center')
            ind=1
            for i in range(len(filtered)):
                response=response+ str(ind)+") "+ filtered['name'].iloc[i]+ " in "+ filtered['address'].iloc[i]+ " has been rated "+filtered['rating'].iloc[i]+"\n"
                ind+=1
        print(response)
        dispatcher.utter_message("---\n"+response+"\n---")
        return []
        
    
class SendMail(Action):
    def name(self):
        return 'email_restaurant_details'
    
    def sendMail(self, df, mailid, top=10):
        if df.empty:
            return False
        contentDf = df.loc[:top,['name','address','average','rating']]
        contentDf = contentDf.rename(columns={'name':'Restaurant Name','address':'Address',
                                     'average':'Average budget for two', 'rating':'Average Rating'})
        
        mail_content=contentDf.to_html(index=False, justify='center')
        start = '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
          font-family: arial, sans-serif;
          border-collapse: collapse;
          width: 80%;
          margin-left: auto;
          margin-right: auto
        }
        
        td, th {
          border: 1px solid #dddddd;
          text-align: left;
          padding: 8px;
        }
        
        </style>
        </head>
        <body>
        <h2 align="center" style="font-family:arial">HERE ARE YOUR TOP 10 RESTAURANTS</h2>
        '''
        
        end ='''
        </body>
        </html>
        '''
     
        mail_content=start+mail_content+end
#        print(mail_content)
        try:
            mail =sendMail.Mail(mailid, mail_content)
            mail.send()
        except:
            return False
        
        return True
        
    def run(self, dispatcher, tracker, domain):
        mail = tracker.get_slot('email')
        global restaurants
        print("---inside mail---\n",restaurants)
        flag=self.sendMail(restaurants.reset_index(), mail)
        if flag:
            dispatcher.utter_message("We have sent you a mail..")
        else:
            dispatcher.utter_message("Sorry we have encountered a problem, Please try again later..!\n")
            
        return []
    
class ActionRestart(Action):     
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        print("restarted---")
        return[Restarted()]


class ActionValidateLocation(Action):
    def name(self):
        return 'action_check_location'
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        loc=loc.split()[-1]
        cities=[]
        with open('cities.txt', 'r') as file:
            cities+=[x.strip().lower() for x in list(file)]
            
        print("location", loc)
        location_validation = True

        if not loc or loc.lower() not in cities:
            location_validation = False
    
        return [SlotSet("location_validation", location_validation), SlotSet("location", loc)]
        
        
class ActionValidateCuisine(Action):
    def name(self):
        return "action_check_cuisine"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        supported_cuisines = ["american", "chinese", "italian", "mexican", "north indian", "south indian"]

        cuisine_validation = True
        
        print("cuisine", cuisine)

        if not cuisine or cuisine.lower() not in supported_cuisines:
            cuisine_validation = False
    
        return [SlotSet("cuisine_validation", cuisine_validation), SlotSet("cuisine", cuisine)]
    
class ActionValidatePrice(Action):
    def name(self):
        return "action_check_price"

    def run(self, dispatcher, tracker, domain):

        price = tracker.get_slot("price")
        supported_price = ["lesser than 300", "between 300 to 700", "more than 700"]

        price_validation = True
        
        print("price value", price)

        if not price or price.lower() not in supported_price:
            price_validation = False
    
        return [SlotSet("price_validation", price_validation), SlotSet("price", price)]

