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

#Assertions that can be applied on JSON response 

# Bdd style            
@then(parsers.parse('Validate API returns a response code of "{statuscode}"'))
def validate_code(statuscode):
    assert response.status_code == int(statuscode)

@then(parsers.parse('Validate API has a Content-Length of "{contentLength}"'))
def validate_content_length(contentLength):
    assert response.headers['Content-Length'] == int(contentLength)    


@then(parsers.parse('Validate the message value "{message}" in response'))
def validate_message_value(message):
    contentvalue = json.loads(response.text)
    logger.info("Response --- > ", contentvalue)
    if len(contentvalue) == 1:
        assert contentvalue['message'] == message
    else:
        values = jsonObj.readJsonfiles(message)
        assert len(values) == len(contentvalue)
        assert sorted(values.items()) == sorted(contentvalue.items())
        #assert (sorted(values, key = lambda item: item['id'])) == (sorted(contentvalue, key = lambda item: item['id']))

@then(parsers.parse('Validate the attribute "{attribute}" in response'))
def validate_attribute_value(attribute):
    jsonObj.keyPresenceInJson(response.text,attribute)  

@then(parsers.parse('Validate the attribute "{attribute}" has "{value}" in response'))
def validate_attribute_value(attribute,value):
    jsonObj.keyValuePresenceInJson(response.text,attribute,value)      

@then(parsers.parse('Validate the attribute "{attribute}" has size "{size}" in response'))
def validate_attribute_value(attribute,size):
    jsonObj.keyCountInJson(response.text,attribute,size)      


@then(parsers.cfparse('Validate the attribute list "{attributeList}" in response'))
def validate_attribute_value(attributeList):
    contentvalue=json.loads(response.text)
    for attribute in attributeList:
     try: 
       if contentvalue[attribute]:
         assert True
     except:
         assert False , print(attribute + " was not found in " + contentvalue)  

