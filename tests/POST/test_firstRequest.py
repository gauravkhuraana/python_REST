import requests
import os
import json
import jsonpath

def test_firstPost():
    url='https://reqres.in/api/users'


   
    current_working_dir = os.getcwd()
   
    print("current_working_dir -->", current_working_dir)
    
    fileObject= open(current_working_dir+'/resources//firstRequest.json','r')

    requestBody = fileObject.read()
    jsonRequestBody = json.loads(requestBody)
    
    response = requests.post(url,jsonRequestBody)


    print("\n Content is as follow \n ",response.content)

    print("\n Content in headers \n",response.headers)

    print("\n Specific headers \n",response.headers.get('Content-Length'))

    jsonResponse = json.loads(response.text)
    # Get a particular element
    createdAt = jsonpath.jsonpath(jsonResponse,'createdAt')
    print("\n createdAt is \n ",createdAt)

   
    
    assert response.status_code == 201

