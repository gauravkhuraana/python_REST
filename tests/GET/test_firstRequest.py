import requests
import json
import jsonpath 
import pytest
from assertpy import assert_that
import logging


def test_GetAPI():
 
 #Arrange
 url = "https://reqres.in/api/users?page=2"

 #Act
 response = requests.get(url)

 #Assert
 print(" \n status_code == >")
 print (response.status_code)
 
 print(" \n Json Response of API printed in a pretty way == > ")
 json_object = json.loads(response.content)
 json_fomatted_str = json.dumps(json_object,indent=2)
 print(json_fomatted_str)


 
 print (" \n cookies")
 print (response.cookies)
 
 print (" \n headers")
 print (response.headers)
 
 print (" \n json")
 print (response.json)
 
 print (" \n request")
 print (response.request)
 
 print (" \n url")
 print (response.url)


@pytest.mark.Current
def test_getSpecificDatafromResponse():
     #Arrange
     url = "https://reqres.in/api/users?page=2"

     #Act
     response = requests.get(url)
     
     
     jsonResponse = json.loads(response.content)
     print(jsonResponse)

     #To pick direct element
     totalPages = jsonpath.jsonpath(jsonResponse,'total_pages')
     total = jsonpath.jsonpath(jsonResponse,'total')
     
     #to Pick list     
     print( " Total pages ======  ", totalPages[0])
     print( " Total ======  ", total[0])

     # to pick from json Object
     supportUrl = jsonpath.jsonpath(jsonResponse,'support.url')
     print( " ID ======  ", supportUrl)

     # to pick from json Array
     dataId = jsonpath.jsonpath(jsonResponse,'data[0].id')
     print( " ID ======  ", dataId)

     dataId = jsonpath.jsonpath(jsonResponse,'data[3].id')
     print( " ID ======  ", dataId)

def test_Add2Numbers():
     assert_that(6).is_equal_to(add(1,5))
     assert 4==add(1,3)

def add(a,b):
     return a+b



def validate_api(Base_URL,endpoint,request_headers):
    global response
    response = APIObj.GET(Base_URL + endpoint, request_headers=request_headers)
    contentvalue = json.loads(response.text)
    logging.getLogger().info(contentvalue)
    assert response.ok