from dataclasses import dataclass

import requests


# def get(address,               # URL for the request
#         params=None,           # URL params dict
#         headers=None,          # HTTP headers
#         cookies=None,          # request cookies
#         data=None,             # raw request data
#         json=None,             # attach JSON object as request body
#         encrypted_cert=None,   # certificate to use with request 
#         allow_redirects=True,  # automatically follow HTTP redirects
#         timeout=30)            # request timeout, by default it's 30 seconds


@dataclass
class Response:
    status_code:int
    text: str
    as_dict: object
    headers: dict

class APIRequest:
    def get(self,url):
        response = requests.get(url)
        return self.__get_responses(response)

    def post(self,url,payload,headers):    
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response)
    
    def delete(self,url):
        response = requests.delete(url)
        return self.__get_responses(response)


    def __get_responses(self,response):
        status_code=response.status_code
        text=response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers= response.headers
        # print("Response status_code ", status_code)
        # print("Response text ", text)
        # print("Response as dict ", as_dict)
        # print("Response headers ", headers)
        
        return Response(
            status_code,text,as_dict,headers
        )        