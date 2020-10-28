
# coding: utf-8

# In[7]:


import csv 
import requests
import pandas as pd

prefix="新竹市"
url="http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv"

download = requests.get(url)
decoded_content = download.content.decode("utf-8")
cr = csv.reader(decoded_content.splitlines(), delimiter=",")

original_list = list(cr)
#print(original_list)

mask_df = pd.DataFrame(original_list)
mask_df.head()

