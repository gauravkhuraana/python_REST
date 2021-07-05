import random

def randomNumber(min,max):
    number=random.randint(min,max)
    return number

def test_randomNumberGeneration():
    print("Random Number ",randomNumber(10000,99999))
  