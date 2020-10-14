
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
url = "https://dct.ntcu.edu.tw/news.php"
r = requests.get(url)

#確認是否下載成功
if r.status_code == requests.codes.ok:
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    a_tags = soup.find_all('a')
    for tag in a_tags:
        print('網址:'+str(tag.string)+' =>' +tag.get('href'))

