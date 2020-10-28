
# coding: utf-8

# In[40]:


import csv 
import requests
import pandas as pd

prefix='高雄市'
url="http://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D50001-001&l=https://data.nhi.gov.tw/resource/mask/maskdata.csv"
prefix_list = []
row_count = 0

with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode("utf-8")
    cr = csv.reader(decoded_content.splitlines(), delimiter=",")
    original_list = list(cr)

    print("original_list len = %d" % (len(original_list)-1))
    
    
    for row in original_list:
        row_count = row_count + 1
        if row_count != 1:
            if prefix == '':
                prefix_list.append(row)
            elif row[2].startswith(prefix):
                prefix_list.append(row)
    print("prefix_list len= %d" % len(prefix_list))
 


# In[41]:


def myFunc(row):
    return int(row[4])
prefix_list.sort(key=myFunc, reverse=True)

prefix_list.insert(0,original_list[0])

mask_df = pd.DataFrame(prefix_list)
with pd.option_context('display.max_rows',None,"display.max_columns", None):
    display(mask_df)

