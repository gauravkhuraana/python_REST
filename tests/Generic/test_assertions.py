from config import BASE_URI_REQRES_GET
import requests
from assertpy import assert_that, soft_assertions

def test_assertionsAll():
    path ='api/users?page=2'
    response = requests.get(BASE_URI_REQRES_GET+path)
    print ("Response is ", response.content)
    responseJson = response.json()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    assert_that(responseJson).extracting('page').is_not_empty().contains("reqres")
    #assert_that(response.status_code,description=" Status code is not for success ").is_equal_to(requests.codes.no_content)

def test_softAssertions():
    path ='api/users?page=2'
    response = requests.get(BASE_URI_REQRES_GET+path)

    print( " Response code is ", response.status_code)
    
    with soft_assertions():
           # though this statement will fail but still next will run
          # assert_that(response.status_code,description = "mismatch of status codes").is_equal_to(requests.codes.no_content)
           assert_that(response.status_code) .is_equal_to(requests.codes.ok)
           

