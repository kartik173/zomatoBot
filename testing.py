import zomatoAPI
import pandas as pd

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

    def budget_group(row):
        if row['budget'] <300 :
            return 'lesser than 300'
        elif 300 <= row['budget'] <700 :
            return 'between 300 to 700'
        else:
            return 'more than 700'

    df['budget'] = df.apply(lambda row: budget_group (row), axis=1)
    
    restaurant_df = df[(df.budget == price)]
    restaurant_df = restaurant_df.sort_values(['rating'], ascending=False)    

    return restaurant_df

    
loc = "delhi"
cuisine = 'chinese'
price='lesser than 300'  
res1=test(loc, cuisine, price)

#{"code":403,"status":"Forbidden","message":"Invalid API Key"}