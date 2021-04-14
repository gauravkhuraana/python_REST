import pytest
from utils.file_reader import readFile
import random
from  uuid import uuid1
from json import dumps
import requests 
from config import BASE_URI
from assertpy import assert_that
import json
from jsonpath_ng import parse

@pytest.fixture
def createData():
    payLoad= readFile('createPerson.json')
    print ( "First Payload is ", payLoad)
    randomNbr = random.randint(0,1000)
    lastName = f'Olabini{randomNbr}'
    payLoad['lname'] = lastName
    print ( "Final Payload is ", payLoad)
    yield payLoad


def test_PersonCanBeAddedWithJsonTemplate(createData):
    print ("createData --- >",createData)
    createPersonWithUniqueLastName(createData)

    response = requests.get(BASE_URI)
    peoplesObj = json.loads(response.text)

    jsonpathXpr = parse ( " $.[*].lname")
    result = [match.value for match in jsonpathXpr.find(peoplesObj)]

    expectedLastName = createData['lname']
    assert_that(result).contains(expectedLastName)


def createPersonWithUniqueLastName(body=None):
    if body is None:
        uniqueLastName = f'User {str(uuid1())}'
        payload = dumps({
            'fname':'New',
            'lname': uniqueLastName
        })
    else:
        uniqueLastName = body['lname']
        payload = dumps(body)

    headers= {
        'Content-Type' : 'application/json',
        'Accept' : 'application/json'
    }    
     
    print("BASE URI is ", BASE_URI) 
    print("Payload is ", payload)
    print("headers is ", headers)
    
  
    response = requests.post(url=BASE_URI, data=payload , headers=headers)
    print (response.content)


    assert_that(response.status_code, description = 'Person not created ').is_equal_to(requests.codes.no_content)
    return uniqueLastName