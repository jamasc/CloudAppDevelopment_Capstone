import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def post_request(url, json_payload, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    try:
        response = requests.post(url, params=kwargs, json=json_payload)
        status_code = response.status_code
        print("With status {} ".format(status_code))
    except:
        # If any error occurs
        print("Network exception occurred")
    

def get_dealers_from_cf(url, **kwargs):
    results = []
    json_result = get_request(url, **kwargs)
    if json_result:
        dealers = json_result
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer( id=dealer_doc["id"],
                                    city=dealer_doc["city"],
                                    state=dealer_doc["state"], 
                                    st=dealer_doc["st"], 
                                    address=dealer_doc["address"], 
                                    zip=dealer_doc["zip"], 
                                    lat=dealer_doc["lat"], 
                                    longt=dealer_doc["long"], 
                                    short_name=dealer_doc["short_name"], 
                                    full_name=dealer_doc["full_name"])
            results.append(dealer_obj)
    return results

def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealerId=dealerId)
    if json_result:
        # Get the row list in JSON as dealers
        reviews = json_result
        # For each dealer object
        for thisreview in reviews:    
            review_obj = DealerReview( dealership=thisreview["dealership"],
                                       name=thisreview["name"], 
                                       purchase=thisreview["purchase"], 
                                       review=thisreview["review"], 
                                       purchase_date=thisreview["purchase_date"], 
                                       car_make=thisreview["car_make"], 
                                       car_model=thisreview["car_model"], 
                                       car_year=thisreview["car_year"], 
                                       sentiment='',
                                       id=thisreview["id"])
            review_obj.sentiment = analyze_review_sentiments(review_obj.review)
            results.append(review_obj)
    return results

def analyze_review_sentiments(text):
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/f35a808e-3e7c-49c4-a12a-9750ddcb934c"
    params = {
        'version': '2022-04-07',  
        'features': 'sentiment',
        'text': text,
    }
    response = get_request(url, params=params, auth=HTTPBasicAuth('apikey', "0UisJ7LOaI543FUv_mrow7jRwOe6xAy9tKdmOmYuF2On"))
    return response



