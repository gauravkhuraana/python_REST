import json 
from pathlib import Path



BASE_PATH = Path.cwd().joinpath('.','resources')

def readFile(fileName):
    path = getFileWithJsonExtension(fileName)

    with path.open(mode='r') as f:
         return json.load(f)


def getFileWithJsonExtension(fileName):
    if '.json' in fileName:
        path=BASE_PATH.joinpath(fileName)
    else:
        path=BASE_PATH.joinpath(f'{fileName}.json')
    return path    


def test_jsonFileRead():
    fileName='addStudentDetails'

    print("Original File")
    jsonObj=readFile(fileName)

    print(jsonObj)
    jsonObj['id']=randomNumber(10000,99999)

    print("Modified File")
    print(jsonObj)
    