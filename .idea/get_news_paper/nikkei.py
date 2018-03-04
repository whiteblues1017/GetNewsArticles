import sys
import json
import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import codecs

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


homepath=os.path.expanduser('~')

# Selenium settings
driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
def login(url,ID,PASSWORD):
    # get a HTML response
    driver.get(url)
    html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    # parse the response
    soup = BeautifulSoup(html, "lxml")
    # extract
    ## title
    header = soup.find("head")
    title = header.find("title").text
    print(title)
    #print(soup)
    driver.find_element_by_name("LA7010Form01:LA7010Email").send_keys(ID)
    driver.find_element_by_name("LA7010Form01:LA7010Password").send_keys(PASSWORD)
    driver.find_element_by_class_name('btnNext').click()

    html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    # parse the response
    soup = BeautifulSoup(html, "lxml")
    #print(soup)

def collect_articles(articles):
    urls = []
    i=0
    for article in articles:
        url = article.get_attribute('href')
        if url not in urls:
            urls.append(url)
            i=1+i
            print(str(i),url)
        if i==20:
            break
    return urls


def get_text():
    driver.get('https://www.nikkei.com/economy/economic/')
    size_articles=driver.find_element_by_class_name("m-pageNation").text
    size_articles=int(size_articles[0:size_articles.find('中')-1])
    print(size_articles)
    articles=driver.find_elements_by_xpath("//a[contains(@href,'article')]")

    urls =collect_articles(articles)

    driver.get(urls[1])
    html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("head").find("title").text
    date = driver.find_element_by_class_name("cmnc-publish").text.replace(' ','@')
    date_str_list=list(date)
    print(date)
    year=date[0:4]
    month=date[5:date.rfind('/')]
    date=date[date.rfind('/')+1:date.find('@')]
    hour=date[date.find('@'):-1]
    minitus=date[date.find(':')+1:-1]

    print(year+month+date+hour+minitus)
    print(hour)
    print(minitus)

    month_changed=False
    for i in range(len(date_str_list)):
        if date_str_list[i]=='/':
            date_str_list[i]='月'
            month_changed=True
        elif date_str_list[i]=='/' and month_changed==True:
            date_str_list[i]='日'




    print(date_str_list)
    print(title)

    tags=driver.find_elements_by_xpath("//dd[contains(@class,'cmnc-tag')]")



class nikkei():
    def nikkei(ID,PASSWORD):
        driver.get('https://www.nikkei.com/economy/')
        driver.find_element_by_class_name('l-miH02_loginBtn').click()
        login(driver.current_url,ID,PASSWORD)
        get_text()