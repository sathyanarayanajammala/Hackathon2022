# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:23:13 2022

@author: jamal
"""
import pandas as pd
from ethnicolr import census_ln,pred_census_ln
import gender_guesser.detector as gender
import pandas as pd
import math
import pandas as pd
from ethnicolr import census_ln,pred_census_ln

from ethnicolr import pred_wiki_ln, pred_wiki_name


gd_detector = gender.Detector(case_sensitive=False)
def get_first_name(name):
    name = name.split('-')
    name = name[0].split(' ')
    return name[0]

def get_last_name(name):
    name = name.split('-')
    name = name[0].split(' ')
    return name[1]

def get_gender(name):
    gender=gd_detector.get_gender(get_first_name(contact))
    if("male"== gender):
        return 0
    else:
        return 1
def get_minority(name):
    namaedf= pred_census_ln(name)
    
    
    
excel_file = 'C:\Hackathon\HackathonDataMinorityWomenOwned2022v1.xlsx'
df = pd.read_excel(excel_file)

isWomanOwned=[]
MinorityOwnedDesc=[]

# get the iswomanowned data using gender-guesser model
for index, row in df.iterrows():
    contact = str(row["executiveContact1"])
    #print(contact)
    if(pd.isnull(contact)): 
        contact = row["executiveContact2"]
        firstName=get_first_name(contact)
        lastName=get_last_name(contact)
        isWomanOwned.append(get_gender(lastName))
    else:
        firstName=get_first_name(contact)
        lastName=get_last_name(contact)
        isWomanOwned.append(get_gender(firstName))
        MinorityOwnedDesc.append(get_minority(lastName))
        
df["isWomanOwned"]=isWomanOwned

df["MinorityOwnedDesc"]=MinorityOwnedDesc

