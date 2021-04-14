import requests

from domainSpecific.people_client import PeopleClient
from tests.assertionsGeneric.peopleAssertion import *
from tests.helpers.people_helpers import *
from assertpy import assert_that

client = PeopleClient()

def test_read_all_has_kent():
    response = client.read_all_persons()
    
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    assert_people_have_person_with_first_name(response,first_name='Kent')

def test_new_person_can_be_added():
    last_name,response = client.create_person()
    assert_that(response.status_code, description = 'Person not created').is_equal_to(requests.codes.no_content)

    peoples = client.read_all_persons().as_dict
    is_new_user_created = search_created_user_in(peoples,last_name)
    print ( " is new user created ", is_new_user_created)
    assert_person_is_present(is_new_user_created)

def test_created_person_can_be_deleted():
    persons_last_name, _ = client.create_person()

    peoples = client.read_all_persons().as_dict
    new_person_id = search_created_user_in(peoples,persons_last_name)    
    
    response  = client.delete_person(new_person_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

def test_person_can_be_added_With_a_json_Template(created_data):
    client.create_person(created_data)

    response = client.read_all_persons()
    peoples = response.as_dict

    result = search_nodes_using_json_path(peoples, json_path="$.[*].lname")

    expected_last_name = created_data['lname']
    assert_that(result).contains(expected_last_name)





