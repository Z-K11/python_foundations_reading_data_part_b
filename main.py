import pandas.io.sql as pds 
import pandas as pd 
import sqlite3 as sq 
import requests
import os 
url ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/baseball.db"
destination_folder = "data"
os.makedirs(destination_folder,exist_ok=True)
file_path = os.path.join(destination_folder,"base_ball.db")
response = requests.get(url)
if os.path.exists(file_path):
    print(f'File exists at {file_path}')
else:
    with open(file_path,"wb") as file:
        file.write(response.content)
    print(f'Download Complete Saved at {file_path}')
path='data/base_ball.db'
con =sq.Connection(path)
