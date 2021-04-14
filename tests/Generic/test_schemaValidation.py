import json
import requests

from cerberus import Validator
from config import BASE_URI
from assertpy import assert_that,soft_assertions


schema= {
    "fname":{'type':'string'},
    "lname":{'type':'string'},
    "person_id":{'type':'number'},
    "timestamp":{'type':'string'}
}

def test_readOneOPerationHasExpectedSchema():
    response = requests.get(f'{BASE_URI}/1')
    print (" Response is \n", response)
    person = json.loads(response.text)

    validatorOut = Validator(schema)
    print (" ValidatorOut is \n", validatorOut)
    
    isValid = validatorOut.validate(person)
    print (" isValid is \n", validatorOut)
     
    assert_that(isValid,description=Validator.errors).is_true()


def test_readAllOperations():
     response = requests.get(BASE_URI)   
     presonsObj = json.loads(response.text)

     validatorOut= Validator(schema, require_all = True)

     with soft_assertions():
         for person in presonsObj:
             isValid = validatorOut.validate(person)
             assert_that(isValid, description=validatorOut.errors).is_true()