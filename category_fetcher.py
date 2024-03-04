import pandas as pd
import numpy as np
from colorama import *
import json
import requests


with open ('competitor_list.json','r') as file :
    competitor_list = json.load(file).get("competitor_list")
    
    # print(competitor_list)
    
row_data = {}    

for competitor in competitor_list :
    row_data.update({competitor.get('name'):[]})
    
for competitor in competitor_list :
    print(Fore.GREEN + "fetching data from " +competitor.get('name')+ "...")
    URL = competitor.get('cat_url')
    cookie = competitor.get('cookie')
    HEADERS = {

        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': cookie
        }
    
    
    try :
        responses = requests.get(URL,headers=HEADERS)
        if responses.status_code == 200 :
            data = responses.json()
            items = data.get("items")
            for item in items :
                row_data[competitor.get('name')].append(item.get('name'))
            print(Style.BRIGHT + Fore.GREEN + "category data fetched\n")  
        else :
            print(Style.BRIGHT + Fore.RED + "Failed to fetch data from " + competitor.get('name'))  
            
            exit()
            
    except :
        print("not getting data") 
maxlength = max(len(arr) for arr in row_data.values())
# print(maxlength)      

for key,value in row_data.items() :
    print(f"name is : {key} length {len(value)}") 
    if len(value) < maxlength :
        row_data [key] = value + [np.nan] * (maxlength - len(value))
        
print(row_data)
df = pd.DataFrame(row_data)
output = df.to_excel("output_xlsx/category.xlsx",index=False)        
print(df) 
print(output)           
                    