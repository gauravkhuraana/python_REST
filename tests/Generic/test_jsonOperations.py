# from utils.file_reader import jsonOps.readFile
# def test_jsonRead():
#     obj=jsonOps()
#     obj.readFile("addStudentDetails")
import json
import os
import getpass
import copy
from jsonpath_ng import jsonpath, parse

def createJsonfiles(jsonContent, path, fileName):
        json_object = json.dumps(jsonContent,indent=4)
        dirname = os.path.dirname(__file__)
        print ("ddfsdfsfsfsfs",dirname)
        fileNameWithPath = dirname + path + fileName + ".json"
        print ("ddfsdfsfsfsfs",fileNameWithPath)
        #file = path.join(fileNameWithPath)
        #print ("ddfsdfsfsfsfs",file)
        with open (fileNameWithPath,"w") as outfile:
          outfile.write(json_object)

def test_createJson():
    createJsonfiles("{'name':'gk'}","\\temp\\","requestHeaders")

def keyPresence(jsonStr,key):
    json1=json.loads(jsonStr)
  
    #print ("oyes " ,getpass.getuser())
    try: 
       if json1.get(key):
         return True
    except:
       return False   


# this function checks if a paritular value is present at a particular path in json or not 
# stackoverflow credits to Elinaldo Monteiro
# https://stackoverflow.com/a/66275899/2986279

def filter_dict(data:dict, extract):
    data = json.loads(data)
    try:
        if isinstance(extract, list):
            for i in extract:
                result = filter_dict(data, i)
                if result:
                    return result
        keys = extract.split('.')
        shadow_data = data.copy()
        for key in keys:
            if str(key).isnumeric():
                key = int(key)
            shadow_data = shadow_data[key]
        return shadow_data
    except IndexError:
        return None


## possible via jsonpath_ng 

def keyPresenceInJson(jsonVal,key):
    jsonObj  = json.loads(jsonVal)
    jsonpath_expr=parse(key)
    match = jsonpath_expr.find(jsonObj)
    try:
     if match[0].value:
       return True 
     else:
       return False  
    except AssertionError:
      print("**** Error **** ",key, " does not exist in passed JSON ********" )
      return False

def keyValuePresenceInJson(jsonVal,key,value):
    jsonObj  = json.loads(jsonVal)
    jsonpath_expr=parse(key)
    match = jsonpath_expr.find(jsonObj)
    try:
     try:
       if match[0].value:
          print(key, " Key exists in json, we will check for value existence now ",)
     except:
       print("**** Error **** ",key, " does not exist in passed JSON ********" )
       return False    

     if match[0].value == value:  
       return True
     else:
       return False  
    except AssertionError:
      print("**** Error **** ",key, " does not have the value ", value, " in passed JSON ********" )
      return False

def keyCountInJson(jsonVal,key,value):
    jsonObj  = json.loads(jsonVal)
    jsonpath_expr=parse(key)
    match = jsonpath_expr.find(jsonObj)
    try:
     try:
       if match[0].value:
          print(key, " Key exists in json, we will check for value existence now ",)
     except:
       print("**** Error **** ",key, " does not exist in passed JSON ********" )
       return False    

     if len(match) == value:  
       return True
     else:
       return False  
    except AssertionError:
      print("**** Error **** ",key, " does not have the value ", value, " in passed JSON ********" )
      return False

def listOffValuesForKeyInJson(jsonVal,key):
    jsonObj  = json.loads(jsonVal)
    jsonpath_expr=parse(key)
    match = jsonpath_expr.find(jsonObj)
    
    try:
       if match[0].value:
          return [match.value for match in jsonpath_expr.find(jsonObj)]
                 

    except:
       print("**** Error **** ",key, " does not exist in passed JSON ********" )
       return False    

def firstValueForKeyInJson(jsonVal,key):
    jsonObj  = json.loads(jsonVal)
    jsonpath_expr=parse(key)
    match = jsonpath_expr.find(jsonObj)
    
    try:
       if match[0].value:
          return match[0].value
    except:
       print("**** Error **** ",key, " does not exist in passed JSON ********" )
       return False    



     
def test_keyPresence():
    
    #assert keyPresence('{"name":"gk"}',"name")
    
    sample = '''
{"menu": {
    "header": "SVG Viewer",
    "items": [
        {"id": "Open"},
        {"id": "OpenNew", "label": "Open New"},
        null,
        {"id": "ZoomIn", "label": "Zoom In"},
        {"id": "ZoomOut", "label": "Zoom Out"},
        {"id": "OriginalView", "label": "Original View"},
        null,
        {"id": "Quality"},
        {"id": "Pause"},
        {"id": "Mute"},
        null,
        {"id": "Find", "label": "Find..."},
        {"id": "FindAgain", "label": "Find Again"},
        {"id": "Copy"},
        {"id": "CopyAgain", "label": "Copy Again"},
        {"id": "CopySVG", "label": "Copy SVG"},
        {"id": "ViewSVG", "label": "View SVG"},
        {"id": "ViewSource", "label": "View Source"},
        {"id": "SaveAs", "label": "Save As"},
        null,
        {"id": "Help"},
        {"id": "About", "label": "About Adobe CVG Viewer..."}
    ]
}}

''' 
    #sample = json.loads(sample)
    #jsonpath_expr = parse('$.menu.items.1.id')
    #jsonpath_expr = parse('$.menu.items.[1].id')
    # jsonpath_expr = parse('menu.items.[*].id')
    # match = jsonpath_expr.find(sample)
    # print("length is " , len(match))
    # #print()
    #assert keyCountInJson(sample,'menu.items.[*].id',18)
    
    value= listOffValuesForKeyInJson(sample,'menu.items.[*].id')
    assert value, 'Passed key is not present in '
    print("Value for the key passed is ",value )
    value= firstValueForKeyInJson(sample,'menu.items.[*].id')
    print("Value for the key passed is ",value )
    assert keyValuePresenceInJson(sample,"menu.items.[1].id","OpenNew")
    assert keyValuePresenceInJson(sample,"menu.items.[1].id","shouldFail")==False
    assert keyPresenceInJson(sample,"menu.items.[18].id")


def keyValuePresence(jsonStr,key,value):
    json1=json.loads(jsonStr)
  
    #print ("oyes " ,getpass.getuser())
    try: 
       if json1[key]==value:
         return True
    except:
       return False   

def keyPresenceJson():
    pass