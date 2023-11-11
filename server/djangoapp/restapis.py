import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs, auth=HTTPBasicAuth('apikey', "0UisJ7LOaI543FUv_mrow7jRwOe6xAy9tKdmOmYuF2On"))
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
        requests.post(url, params=kwargs, json=json_payload)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))

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

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
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


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(text):
    analyzed_text = get_request("https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/f35a808e-3e7c-49c4-a12a-9750ddcb934c", text=text)
    return analyzed_text



