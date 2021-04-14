from tests.POST.test_CreateNewPerson import create_new_person
from tests.POST.test_CreateNewPerson import search_created_user_in
from config import BASE_URI
from assertpy import assert_that
import requests

def test_created_person_can_be_deleted():
    persons_last_name = create_new_person()

    peoples = requests.get(BASE_URI).json()

    newly_created_user = search_created_user_in(peoples,persons_last_name)

    personId=newly_created_user[0]["person_id"]
    print ("BASE_URI = ", BASE_URI)
    print ("newly created person id is ", personId)
    delete_url = f'{BASE_URI}/{newly_created_user[0]["person_id"]}'
    response = requests.delete(delete_url)
    print("Response is --> ",response.content)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)