import requests
from assertpy.assertpy import assert_that
from config import BASE_URI

def test_read_all_has_kentAsName():
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    responseJson = response.json()
    print ("Response is ", responseJson)
    
    first_names = [people['fname'] for people in responseJson]
    assert_that(first_names).contains('Kent')





