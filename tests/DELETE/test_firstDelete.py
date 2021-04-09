import requests


def test_firstDeleteUser():
    url='https://reqres.in/api/users/2'
    response = requests.delete(url)
    print("Response status code ---> ",response.status_code)
    assert response.status_code == 204

def test_firstDeleteUserFailure():
    url='https://reqres.in/api/users/2'
    response = requests.delete(url)
    print("Response status code ---> ",response.status_code)
    assert response.status_code != 201