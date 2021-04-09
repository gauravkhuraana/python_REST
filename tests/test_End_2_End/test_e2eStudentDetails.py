import pytest 
import json 
import jsonpath 
import os
import requests

def test_Add_new_Data():

    url = 'http://www.thetestingworldapi.com/api/studentsDetails'
    currentLocation = os.getcwd() 
    fileObj = open(currentLocation+'/resources/addStudentDetails.json','r')
    reqBody = fileObj.read()
    reqBodyJson = json.loads(reqBody)
   
    # Add details for users
    response = requests.post(url,reqBodyJson)
    print("\n Student Response is \n ",response.content)
    responseJson = json.loads(response.content)
    id = jsonpath.jsonpath(responseJson,'id')
    print("\n Id is \n ",id[0])
    assert response.status_code == 201


    urlTechnical = 'http://www.thetestingworldapi.com/api/technicalskills'
    fileObj = open(currentLocation+'/resources/addTechnicalDetails.json','r')
    reqBody = fileObj.read()
    reqBodyJson = json.loads(reqBody)
    reqBodyJson['id']=int(id[0])
    reqBodyJson['st_id']=id[0]
    # Add details for users
    response = requests.post(urlTechnical,reqBodyJson)
    print("\n Technical Response is \n ",response.content)
    # responseJson = json.loads(response.content)
    # id = jsonpath.jsonpath(responseJson,'id')
    # print("\n Id is \n ",id[0])
    # assert response.status_code == 201

    
    urlAddress = 'http://www.thetestingworldapi.com/api/addresses'
    fileObj = open(currentLocation+'/resources/addAddressDetails.json','r')
    reqBody = fileObj.read()
    reqBodyJson = json.loads(reqBody)
    reqBodyJson['stid']=id[0]
    # Add details for users
    response = requests.post(urlAddress,reqBodyJson)
    print("\n Address Response is \n ",response.content)

       







