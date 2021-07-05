import requests


def test_testFunc():


   url = "https://exmaple.com/api/"

   payload={}
   headers = {
   'Authorization': 'Bearer eyJg'
   }

   response = requests.request("GET", url, headers=headers, data=payload)
   assert response.ok
   print(response.text)
