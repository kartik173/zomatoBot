## story_send_mail
> checkpoint_mail
* affirm
  - utter_ask_mail
* send_over_email{"email": "abc@abc.com"}
  - email_restaurant_details
  - utter_goodbye
  - action_restart

## story_deny_mail
> checkpoint_mail
* deny
  - utter_did_that_help
* affirm
  - utter_goodbye
  - action_restart
  
## story_greet
* greet
  - utter_greet

## story_01_location_cuisine_valid
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location": "Bangalore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_02_location_invalid_retry
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Japan"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location": "Bangalore"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Mexican"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine": "Mexican"}
  - utter_ask_price
* search_by_budget{"price": "more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_03_location_invalid
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "America"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* deny
  - utter_deny
  - utter_goodbye 
  - action_restart


<!-- greet, location + cuisine-->
## story_06_location_cuisine_given
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Chinese"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location": "Mumbai"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_07_location_cuisine_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "french"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location": "Mumbai"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine": "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_08_cuisine_invalid_retry_deny
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location" : "Agra"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

<!-- no greet, location + cuisine -->
## story_09_no_greet_location_cuisine_budget_valid_no_email
* restaurant_search{"cuisine":"south indian","location":"Mysore"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Mysore"}  
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "South Indian"}
  - utter_ask_price
* search_by_budget{"price":"more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_10_no_greet_location_cuisine_budget_valid_with_email
* restaurant_search{"cuisine":"north indian","location":"Mysore"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location" : "Mysore"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "north indian"}
  - utter_ask_price
* search_by_budget{"price":"more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail

## story_11_no_greet_location_cuisine_invalid_retry_no_email
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location" : "Mysore"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price":"more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_12_no_greet_location_cuisine_invalid_retry_deny
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location" : "Mysore"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_13_no_greet_location_cuisine_invalid_retry_with_email
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_check_location
  - slot{"location_validation" : true}  
  - slot{"location" : "Mysore"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price":"more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "more than 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


<!-- queries with cuisine only -->
## story_14_greet_cuisine_valid_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "south indian"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "South Indian"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Patna"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_15_greet_cuisine_invalid_retry_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Patna"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail

## story_16_greet_cuisine_valid_location_invalid_retry_email
* greet
  - utter_greet
* restaurant_search{"cuisine": "south indian"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "south indian"}
  - utter_ask_location
* restaurant_search{"location": "USA"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Bangalore"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail



## story_17_no_greet_cuisine_invalid_retry_email
* restaurant_search{"cuisine": "french"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Delhi"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail

## story_18_no_greet_cuisine_valid_location_invalid_retry_email
* restaurant_search{"cuisine": "american"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "american"}
  - utter_ask_location
* restaurant_search{"location": "Bharatpur"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Bangalore"}
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail

<!-- queries with location only -->

<!-- start with greet, followed by question -->
## story_19_greet_location_valid
* greet
  - utter_greet
* restaurant_search{"location": "Chennai"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Chennai"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "North Indian"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail

## story_20_greet_location_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location": "Brazil"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location
* restaurant_search{"location": "Mumbai"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Mumbai"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


<!-- cuisine + location, both invalid -->
## story_21_greet_cuisine_and_location_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location": "Navi", "cuisine": "french"}
  - action_check_location
  - slot{"location_validation": false}
  - utter_location_invalid
* affirm
  - utter_ask_location
* restaurant_search{"location": "Mumbai"}
  - action_check_location
  - slot{"location_validation": true}
  - slot{"location" : "Mumbai"}
  - slot{"cuisine" : "french"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


## story_22_greet_location_valid
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Patna"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "south indian"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail

## story_23_greet_location_invalid_no_retry
* greet
  - utter_greet
* restaurant_search{"location": "Rameswaram"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location
* restaurant_search{"location": "Chennai"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Chennai"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "between 300 to 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "between 300 to 700"}
  - action_restaurant
  - utter_ask_for_send
> checkpoint_mail


<!-- stop conversation with denial-->
## story_24_greet_location_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location":"Kolar", "cuisine":"mexican"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* deny
  - utter_deny
  - utter_goodbye
  - action_restart

## story_25_greet_location_valid_cuisine_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location":"Kolkata", "cuisine":"Punjabi"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Kolkata"}
  - slot{"cuisine" : "Punjabi"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* deny
  - utter_deny
  - utter_goodbye
  - action_restart


## story_26_greet_location_invalid_retry
* greet
  - utter_greet
* restaurant_search{"location": "Munnar"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* deny
  - utter_deny
  - utter_goodbye
  - action_restart


## story_27_greet_cuisine_invalid_retry
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_check_cuisine
  - slot{"cuisine_validation" : false}
  - utter_cuisine_invalid
* deny
  - utter_deny
  - utter_goodbye
  - action_restart



<!-- handling out of scope responses -->
## story_28_greet_out_of_scope
* greet
  - utter_greet
* out_of_scope
  - utter_out_of_scope
  - utter_goodbye
  - action_restart

## story_29_no_greet_location_retry_out_of_scope
* restaurant_search
  - utter_ask_location
* out_of_scope
  - utter_out_of_scope
* out_of_scope
  - utter_goodbye
  - action_restart

## story_30_no_greet_location_invalid_out_of_scope
* restaurant_search{"location": "Paris"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* out_of_scope
  - utter_goodbye
  - action_restart

## story_31_location_invalid_retry_out_of_scope
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Alwar"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Bangalore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "between 300 to 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price": "between 300 to 700"}
  - action_restaurant
  - utter_ask_for_send
* out_of_scope
  - utter_out_of_scope
* deny
  - utter_goodbye
  - action_restart

## story_32_location_invalid_retry_email_out_of_scope
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Champaran"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Patna"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Patna"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "lesser than 300"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price" : "lesser than 300"}
  - action_restaurant
  - utter_ask_for_send
* out_of_scope
  - utter_out_of_scope
* affirm
  - utter_ask_mail
> checkpoint_mail

## story_33_location_invalid_out_of_scope
* restaurant_search{"location":"Kerala", "cuisine":"mexican"}
  - action_check_location
  - slot{"location_validation" : false}
  - utter_location_invalid
* out_of_scope
  - utter_out_of_scope
* deny
  - utter_deny
  - utter_goodbye
  - action_restart


## story_34_location_cuisine_budget_valid_with_email
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_check_location
  - slot{"location_validation" : true}
  - slot{"location" : "Mumbai"}
  - action_check_cuisine
  - slot{"cuisine_validation" : true}
  - slot{"cuisine" : "Chinese"}
  - utter_ask_price
* search_by_budget{"price": "more than 700"}
  - action_check_price
  - slot{"price_validation" : true}
  - slot{"price" : "more than 700"}
  - action_restaurant
  - utter_ask_for_send
* send_over_email{"email": "abc@abc.com"}
  - email_restaurant_details
  - utter_goodbye
  - action_restart
* thank
  - utter_goodbye
  - action_restart


## interactive_story_valid_location_cuisine_price
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_check_location
    - slot{"location_validation": true}
    - slot{"location": "Jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine_validation": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price
* search_by_budget{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_check_price
    - slot{"price_validation": true}
    - slot{"price": "between 300 to 700"}
    - action_restaurant
    - utter_ask_for_send
> checkpoint_mail
