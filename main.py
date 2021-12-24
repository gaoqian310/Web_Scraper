#!/usr/bin/env python
# coding: utf-8

# Import build in module urllib.

# In[1]:


import urllib.request
from bs4 import BeautifulSoup


# __init__ use a website to extract as a parameter
# Scraper class have a method called scrape that will be called everytime retrieving data

# In[3]:

class Scraper:
    def __init__(self, site):
        self.site = site


# In[ ]:


def scrape(self)
    r = urllib.request.urlopen(self.site)
    html = r.read()


# urlopen() returns a Response object from HTML code along with additional data. 
# function.read() returns the HTML of the Response object. 

# BeautifulSoup object pass the html variable and the "html.parser" string as a parameter.

# In[ ]:


def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)


# In[ ]:


pass "a" and the method will return all the URLs the website is linked to in the HTML


# In[4]:


def scrape(self):
    r = urllib.request.urlopen(self.site)
    html = r.read()
    parser = "html.parser"
    sp = BeautifulSoup(html,parser)
    for tag in sp.find_all("a"):
        url = tag.get("href")
        if url is None:
            continue
        if "articles" in url:
            print("\n" + url)


# In[ ]:


calling the get method and passing “href” as a parameter
verify that the URL variable contains data
if it contains the string “articles”  and then print.


# In[5]:


import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()


# In[ ]:




