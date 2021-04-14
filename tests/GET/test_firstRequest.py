import requests
import json
import jsonpath 
import pytest
from assertpy import assert_that



def test_GetAPI():
 
 #Arrange
 url = "https://reqres.in/api/users?page=2"

 #Act
 response = requests.get(url)

 #Assert
 print (" \n status_code")
 print (response.status_code)
 
 print (" \n content")
 print (response.content)
 
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
     assert_that(4).is_equal_to(add(1,5))
     assert 5==add(1,3)

def add(a,b):
     return a+b
