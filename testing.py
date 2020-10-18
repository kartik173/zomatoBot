import zomatoAPI
import pandas as pd
import sendMail
pd.set_option('display.max_colwidth', -1)

class Actions:

    def getResults(self, loc, cuisine):
        config={ "user_key":"a67c96823657beee597b9234eed8906d"}
        zomato = zomatoAPI.initialize_app(config)
        location_detail=zomato.get_location(loc, 1)
        print(location_detail)
        lat=location_detail["location_suggestions"][0]["latitude"]
        lng=location_detail["location_suggestions"][0]["longitude"]
        cityId=location_detail["location_suggestions"][0]["city_id"]
        cuisines_dict=zomato.get_cuisines(cityId)
        print(cuisines_dict.get(cuisine))
    
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
        res_filter = df.copy()
        res_filter['budget'] = res_filter.apply(lambda row: self.budget_group(row), axis=1)
        res_filter = res_filter[(res_filter.budget == price)]
        return res_filter.iloc[:top,:]
    
    def sendMail(self, df, top=10):
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
        
        return mail_content

        
loc = "delhi"
cuisine = 'chinese'
price='lesser than 300'  
mailid='sc.13302.cs2013@gmail.com'
action=Actions()
res=action.getResults(loc, cuisine)
filtered = action.filterByBudget(res, price)
msg=action.sendMail(res)

mail =sendMail.Mail(mailid, msg)
mail.send()



