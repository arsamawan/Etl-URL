import requests
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.engine import URL

def extract():
    # Public API to extract university Data
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    response = requests.get(API_URL).json()
    return response

def transform(response):
    df = pd.DataFrame(response)
    print(f"TOTAL NO OF UNIVERSITIES: {len(df)}")
    df = df[df["name"].str.contains("California")]
    print(f"Number of universities in california {len(df)}")
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    df = df.reset_index(drop=True)
    return df[["domains", "web_pages", "country" , "name"]]

def load(df):
    disk_engine = create_engine('postgresql://postgres:admin@localhost:5432/university')
    df.to_sql(name = 'uni_data1', con=disk_engine, if_exists='replace', index=False)
    print(disk_engine)


data = extract()
df = transform(data)
load(df)
