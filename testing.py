import zomatoAPI
import pandas as pd
import sendMail
pd.set_option('display.max_colwidth', -1)

def test(loc, cuisine, price):
    config={ "user_key":"a67c96823657beee597b9234eed8906d"}
    zomato = zomatoAPI.initialize_app(config)
    location_detail=zomato.get_location(loc, 1)
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
    
    return df


def budget_group(row):
    if row['budget'] <300 :
        return 'lesser than 300'
    elif 300 <= row['budget'] <700 :
        return 'between 300 to 700'
    else:
        return 'more than 700'
    
    
loc = "delhi"
cuisine = 'chinese'
price='lesser than 300'  
mailid='kartik10messi@gmail.com'
res1=test(loc, cuisine, price)
res1=res1.sort_values(['rating'], ascending=False).reset_index()

res_filter = res1.copy()
res_filter['budget'] = res_filter.apply(lambda row: budget_group (row), axis=1)

restaurant_df = res_filter[(res_filter.budget == price)]
restaurant_df = restaurant_df.sort_values(['rating'], ascending=False)

contentDf = res1.loc[:10,['name','address','budget','rating']]
contentDf = contentDf.rename(columns={'name':'Restraunt Name','address':'Address',
                             'budget':'Average budget for two', 'rating':'Average Rating'})

mail_content=contentDf.to_html(index=False, justify='center')
#
#start = '''<!DOCTYPE html>
#<html lang="en">
#<head>
#  <title>Bootstrap Example</title>
#  <meta charset="utf-8">
#  <meta name="viewport" content="width=device-width, initial-scale=1">
#  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
#</head>
#<body>
#<div class="container">
#  <h2>Top 10 restraunts -</h2><br>
#  <table class="table table-hover" border="1">
#'''
#
#end='''
#</div>
#</body>
#</html>
#'''
#mail_content = mail_content.replace('<table border="1" class="dataframe">','')
#mail_content= start+mail_content+end
mail =sendMail.Mail(mailid, mail_content)
mail.send()

#classes='table table-striped',