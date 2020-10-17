from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatoAPI
import pandas as pd
import sendMail
pd.set_option('display.max_colwidth', -1)

class ActionSearchRestaurants(Action):
    
    def name(self):
        return 'action_search_restaurants'
    
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
        if row['budget'] <300 :
            return 'lesser than 300'
        elif 300 <= row['budget'] <700 :
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
    
    def sendMail(self, df, mailid, top=10):
        if df.empty:
            return
        contentDf = df.loc[:top,['name','address','budget','rating']]
        contentDf = contentDf.rename(columns={'name':'Restraunt Name','address':'Address',
                                     'budget':'Average budget for two', 'rating':'Average Rating'})
        
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
        <h2 align="center" style="font-family:arial">HERE ARE YOUR TOP 10 RESTRAUNTS</h2>
        '''
        
        end ='''
        </body>
        </html>
        '''
     
        mail_content=start+mail_content+end
        
        mail =sendMail.Mail(mailid, mail_content)
        mail.send()
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('budget')
        res=self.getResults(loc, cuisine)
        filtered = self.filterByBudget(res, price)
        
        response=""
        if filtered.empty:
            response= "No results found"
        else:
            for i in range(len(filtered)):
                response=response+ "Found "+ filtered['name'].iloc[i]+ " in "+ filtered['address'].iloc[i]+ "has been rated"+filtered['rating'].iloc[i]+"\n"
        
        dispatcher.utter_message("-----"+response)
        
        self.sendMail(res)
        
        return [SlotSet('location',loc)]

