from json import dumps
from uuid import uuid4
from config import BASE_URI
from assertpy import assert_that
import requests

def test_new_person_can_be_Added():
    unique_last_name = create_new_person()

    peoples = requests.get(BASE_URI).json()

    is_new_user_created = search_created_user_in(peoples,unique_last_name)
    print (" Is new user created ? == ",is_new_user_created)
    assert_that(is_new_user_created).is_not_empty()
     


def create_new_person():
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps ({
        'fname' : 'New',
        'lname' : unique_last_name 
    })

    headers = {
        'Content-Type' : 'application/json',
        'Accept' : 'application/json'
    }
    print("URL is " , BASE_URI )
    print("payload is ",payload)
    print("headers are", headers)

    exit(0)
    response = requests.post(url=BASE_URI , data= payload, headers=headers)
    print ("\n Response is \n ", response.content)
    print ("\n Response code is is \n ", response.status_code)
    
    assert_that(response.status_code,description='Person not created').is_equal_to(requests.codes.no_content)
    return unique_last_name

def search_created_user_in(peoples,unique_last_name):
    return [person for person in peoples if person['lname'] == unique_last_name]