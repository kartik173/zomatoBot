import requests
import json

base_url = "https://developers.zomato.com/api/v2.1/"


def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key = config["user_key"]
        
        
    def get_cuisines(self, city_ID):
        """
        Takes City ID as input.
        Returns a dictionary of all cuisine IDs and their respective cuisine names.
        """

        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "cuisines?city_id=" + str(city_ID), headers=headers).content).decode("utf-8")
        r = json.loads(r)
        if self.is_key_invalid(r) and self.is_rate_exceeded(r):
            cuisines = {}
            for cuisine in r['cuisines']:
                cuisines.update({cuisine['cuisine']['cuisine_name'].lower() : cuisine['cuisine']['cuisine_id']})
    
            return cuisines


    def restaurant_search(self, query="", latitude="", longitude="", cuisines="", start=0, limit=20):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "search?q=" + str(query) + "&start=" + str(start) + "&count=" + str(limit) + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&cuisines=" + cuisines, headers=headers).content).decode("utf-8")
        r = json.loads(r)
        if self.is_key_invalid(r) and self.is_rate_exceeded(r):
            details=[]
            for restraunt in r['restaurants']:
                temp={}
                temp['name']=restraunt['restaurant']['name']
                temp['address']=restraunt['restaurant']['location']['address']
                temp['average']=restraunt['restaurant']['average_cost_for_two']
                temp['rating']=restraunt['restaurant']['user_rating']['aggregate_rating']
                details.append(temp)
            return details


    def get_location(self, query="", limit=5):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        if str(limit).isalpha() == True:
            raise ValueError('LimitNotInteger')
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(base_url + "locations?query=" + str(query) + "&count=" + str(limit), headers=headers).content).decode("utf-8")
        r = json.loads(r)
        if self.is_key_invalid(r) and self.is_rate_exceeded(r):
            return r


    def is_key_invalid(self, a):
        """
        Checks if the API key provided is valid or invalid.
        If invalid, throws a InvalidKey Exception.
        """
        if a.get('code') == 403:
            raise ValueError('InvalidKey')
        else:
            return True


    def is_rate_exceeded(self, a):
        """
        Checks if the request limit for the API key is exceeded or not.
        If exceeded, throws a ApiLimitExceeded Exception.
        """
        if a.get('code') == 440:
            raise Exception('ApiLimitExceeded')
        else:
            return True

