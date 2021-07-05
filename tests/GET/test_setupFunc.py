import pytest
import logging
import subprocess
logging.basicConfig(format='%(message)s')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True, scope='session')
def my_fixture():
   subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
   subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
   logging.warning('setup function')
   print(" i will be called only once i am one time")
   options = webdriver.ChromeOptions() 
   #options.add_argument('--profile-directory=Default')
   options.add_argument("--user-data-dir=c:\\Users\\gakhuran\\AppData\\Local\\Google\\Chrome\\User Data")
   driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
   driver.get("https://gmail.com")
   driver.close()
   subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
   subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
   

def test_one():
    logging.warning('test_a')

    print(" i am first function")

def test_two():
    logging.warning('test_b')

    print(" i am second function")