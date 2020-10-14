
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>公主連接</h2>
<p>抽報.</p>
<a id="link1" href="/my_link1">刀表1</a>
<a id="link2" href="/my_link2">刀表2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())


# In[2]:


title_tag = soup.title
print(title_tag)


# In[5]:


a_tags = soup.find_all('a')
for tag in a_tags:
    print(tag.get('href'))
    print(tag.get('a'))

