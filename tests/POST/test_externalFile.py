import requests
import os
import json
import jsonpath
import random

def test_firstPost():
    url='https://reqres.in/api/users'


   
    current_working_dir = os.getcwd()
   
    print("current_working_dir -->", current_working_dir)
    
    fileObject= open(current_working_dir+'/resources//firstRequest.json','r')
    requestBody = fileObject.read()
    jsonRequestBody = json.loads(requestBody)
    print ("jsonRequestBody is ",jsonRequestBody)
    
    print("Update json's existing node if it exists")
    if('middle_name' in jsonRequestBody):
        jsonRequestBody['middle_name']=random.randrange(100000,999999)
        print ("jsonRequestBody is now ",jsonRequestBody)
        exit()
    
    exit()
    response = requests.post(url,jsonRequestBody)



    print("\n Content is as follow \n ",response.content)

    print("\n Content in headers \n",response.headers)

    print("\n Specific headers \n",response.headers.get('Content-Length'))

    jsonResponse = json.loads(response.text)
    # Get a particular element
    createdAt = jsonpath.jsonpath(jsonResponse,'createdAt')
    print("\n createdAt is \n ",createdAt)

   
    
    assert response.status_code == 201

def test_valueExistInJson():
    print("test")
  