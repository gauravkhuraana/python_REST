import random
import pytest

from utils.file_reader import readFile

@pytest.fixture
def created_data():
    payload = readFile('createPerson.json')

    random_no= random.randint(0,1000)

    last_name = f'Olabini{random_no}'

    payload['lname']=last_name
    yield payload