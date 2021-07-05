import requests

class API:

    def __init__(self):
        self.APIResponse = None   

    def GET(self,endpoint , request_headers=None,request_params=None):
        response = requests.get(url=endpoint, headers=request_headers, params=request_params)
        return self.__get_response('GET',endpoint,response, request_headers,request_params)
    
    def POST(self,endpoint , requestBody=None, requestBodyAsJson=None,request_headers=None):
        response = requests.post(url=endpoint, data=requestBody, json=requestBodyAsJson, headers=request_headers)
        return self.__get_response('POST',endpoint,response, requestBody,requestBodyAsJson,request_headers)
    
    def PUT(self,endpoint , requestBody=None, requestBodyAsJson=None,request_headers=None):
        response = requests.put(url=endpoint, data=requestBody, json=requestBodyAsJson, headers=request_headers)
        return self.__get_response('PUT',endpoint,response, requestBody,requestBodyAsJson,request_headers)
    
    def PATCH(self,endpoint , requestBody=None, requestBodyAsJson=None,request_headers=None):
        response = requests.patch(url=endpoint, data=requestBody, json=requestBodyAsJson, headers=request_headers)
        return self.__get_response('PATCH',endpoint,response, requestBody,requestBodyAsJson,request_headers)

    def DELETE(self,endpoint , requestBody=None, requestBodyAsJson=None,request_headers=None):
        response = requests.delete(url=endpoint, data=requestBody, json=requestBodyAsJson, headers=request_headers)
        return self.__get_response('DELETE',endpoint,response, requestBody,requestBodyAsJson,request_headers)    

    def __get_response(self,method, endpoint, response, requestBody=None , request_headers=None, requestBodyAsJson=None, request_params=None ):
        # try:
        #     response=response.json()
        # except Exception:
        #     response=response   
        if(response.status_code!=200 and response.status_code!=201):
            print("Method is  ", method)
            print("URL is              ",endpoint)
            print("Request Headers are ", request_headers)
            print("Request Params are  ", request_params)
        
        
            if(requestBody != None):
             print("Request Body is     ", requestBody)
            if(requestBodyAsJson != None):
             print("Request Body is     ", requestBody)
            print("Response status code is  ", response.status_code)
            print("Response Body is         ", response.content)
        
        # To get Formatted json
        # json_object = json.loads(response.content)
        # json_fomatted_str = json.dumps(json_object,indent=2)
        return response
        

         
    
     

    