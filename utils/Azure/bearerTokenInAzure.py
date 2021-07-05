
# # For Generating token 
# scope="scope"
# client_id="client_id"
# client_secret="client_secret"
# username="username"
# password="password"
# grant_type="grant_type"
# resource="resource"
# tenant="tenant"

# Does not Require tenant
auth_url_token='https://login.microsoftonline.com/organizations/oauth2/v2.0/token'

# Does not Require resource
def getAccessToken_AnotherMethod(self):

     payload = f'client_id={client_id}&scope={scope}&client_secret={client_secret}&username={username}&password={password}&grant_type={grant_type}'
     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
     tokenResponse = APIObj.POST(endpoint=auth_url_token, requestBody=payload, request_headers=headers)
     access_token = json.loads(tokenResponse.text.encode('utf8'))['id_token']
     assert tokenResponse.ok
     return access_token

# Requires Tenant id 
auth_url_token=f'https://login.microsoftonline.com/{tenant}/oauth2/token'     
def getAccessToken(self):

     payload = f'client_id={client_id}&scope={scope}&client_secret={client_secret}&username={username}&password={password}&grant_type={grant_type}&resource={resource}'
     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
     tokenResponse = APIObj.POST(endpoint=auth_url_token, requestBody=payload, request_headers=headers)
     access_token = json.loads(tokenResponse.text.encode('utf8'))['access_token']
     assert tokenResponse.ok
     return access_token

def generateHeaders(self,access_token):
     global request_headers
     request_headers = {
        'Accept': '*/*',
        'Authorization':f'Bearer {access_token}'
        }
     return request_headers