import requests
import pandas as pd
from sqlalchemy import create_engine

def extract():
    # response = requests.get(url)
    API_URL = "http://universities.hipolabs.com/search?country=Pakistan"
    response = requests.get(API_URL).json()
    print(response)
    return response

def transform(response):
    df = pd.DataFrame(response)
    # print{(len(df))}
    print(f"TOTAL NO OF UNIVERSITIES: {len(df)}")
    df = df[df["name"].str.contains("lahore")]
    print(f"TOTAL NO OF UNIVERSITIES in lahore: {len(df)}")
    df['domains'] = [','.join(map(str,1)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str,1)) for l in df['web_pages']]
    df = df.reset_index(drop=True)
    return df[["domains", "web_pages", "country" , "name"]]

data = extract()
df = transform(data)