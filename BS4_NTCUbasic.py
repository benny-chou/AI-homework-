
# coding: utf-8

# In[1]:


import requests
url = "https://dct.ntcu.edu.tw/news.php"
html = requests.get(url)
html.encoding="utf-8"
print(html.text)


# In[3]:


htmllist = html.text.splitlines()
print(htmllist)


# In[4]:


n=0
for row in htmllist:
    if "數位" in row: n+=1
print("找到{}次". format(n))

