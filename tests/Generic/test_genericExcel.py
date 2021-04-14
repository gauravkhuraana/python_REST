import numpy as np
import pandas as pd
from uuid import uuid1



def test_addition():
    a = '' 
    b = "is" 
    c = "cool"
    print(a + b + c) 

def test_colorCell():
    #df = pd.DataFrame(np.random.rand(4,3))

    df = pd.DataFrame({'A':['fg','fg','th','th','k','k','k','k'],'B':['ramesh','Ramesh','sam','sam','gau','gau','sam','ramesh'],'C':['ram','Ram','sm','sm','gu','gu','sam','ramesh']})  
    #  data = {'Name':['Tom', 'nick', 'krish', 'jack'],        'Age':[20, 21, 19, 18]

    print(df) 
  
    col_loc_1 = df.columns.get_loc('A') + 2
    col_loc_2 = df.columns.get_loc('B') + 2
    col_loc_3 = df.columns.get_loc('C') + 2


    df.style.apply(highlight, axis = 1).set_table_styles(
     [{'selector': f'th:nth-child({col_loc_1})',
       'props': [('background-color', '#ff0')]},
     {'selector': f'th:nth-child({col_loc_2})',
       'props': [('background-color', '#00F')]}])


    print(df)
    fileName = f'{str(uuid1())}' +'.xlsx'
    #fileName='ou1.xlsx'
    print(fileName)
  
    # df.style.\
    # applymap(color_negative_red).\
    # apply(highlight_max, axis=0).\
    # to_excel(fileName, engine='openpyxl')
    
    df.style.apply(highlight_greaterthan_1, axis=1).to_excel(fileName, engine='openpyxl')

def highlight_max(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return [('background-color: yellow')*3 if v else '' for v in is_max]

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    if val == 'k':
      color = 'red'  
    else:
      color = 'yellow'
    return ['color: %s' % color]*3

def highlight_greaterthan_1(s):
    if s.B == "gau":
        return ['background-color: yellow']*3
    else:
        return ['background-color: red']*3   

def highlight(s): 
    if s.Points == 10 or s.Points == 15:
     return ['background-color : #d9ead3']*3
    elif s.Points == 8 or s.Points == 6:
     return ['background-color : #cfe2f3']*3
    elif s.Points == 5:
     return ['background-color : #f4cccc']*3
    elif s.Points == 4:
     return ['background-color : #fff2cc']*3
    elif s.Points == 3:
     return ['background-color : #d9d2e9']*3
    elif s.Points == 2:
     return ['background-color : #c9daf8']*3
    elif s.Points == 1:
     return ['background-color : #ead1dc']*3
    else:
     return ['background-color : white']*3         