
import json
from os import path
import os
class jsonOps:
    
    def __init__(self):
      pass
      #self.requestDataObj = requestData()

    def readJsonfiles(self,fileName):
       dirname = os.path.dirname(__file__)
       file = path.join(dirname, "../test_data/" + fileName + ".json")
       with open(file, mode='r', encoding='utf-8') as f:
         file_content = f.read()

       #updatedPayLoad=self.requestDataObj.updatePayload(json.loads(file_content))    
       return json.loads(file_content)

# pass the fileName only without json Extension
    def createJsonfiles(self,jsonContent, path, fileName):
        json_object = json.dumps(jsonContent,indent=4)
        dirname = os.path.dirname(__file__)
        fileNameWithPath = dirname + path + fileName + ".json"
        #file = path.join(fileNameWithPath)
        with open (fileNameWithPath,"w") as outfile:
          outfile.write(json_object)
        
    def readJsonfilesWithPath(self,path,fileName):
       dirname = os.path.dirname(__file__)
       file = dirname + path + fileName + ".json"
       with open(file, mode='r', encoding='utf-8') as f:
         file_content = f.read()

       #updatedPayLoad=self.requestDataObj.updatePayload(json.loads(file_content))    
       return json.loads(file_content)        


################################################################################################

    def elementPresence 
