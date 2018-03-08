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

def timestamp(date):
    dates=date.split(' ')
    print(dates[0])
    year = dates[0][0:4]
    month=dates[0][5:dates[0].rfind('/')]
    date=dates[0][dates[0].rfind('/')+1:len(dates[0])]

    if len(month) ==1:
        month='0'+month
    if len(date) == 1:
        date='0'+date

    hour = dates[1][0:dates[1].find(':')]
    minitus = dates[1][dates[1].find(':')+1:len(dates[1])]

    if len(hour)==1:
        hour='0'+hour
    if len(minitus)==1:
        minitus='0'+minitus

    timestamp=year+'年'+month+'月'+date+'日'+hour+'時'+minitus+'分'
    return timestamp

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

def get_one_article(fw):
    html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("head").find("title").text.replace('　　：日本経済新聞','')
    date = driver.find_element_by_class_name("cmnc-publish").text

    date=timestamp(date)
    print(date)
    print(title)
    fw.write('"'+title+'","'+date+'","')
    tags=driver.find_elements_by_xpath("//dd[contains(@class,'cmnc-tag')]")
    for i in range(len(tags)):
        print(tags[i].text)
        if i!=len(tags)-1:
            fw.write(tags[i].text+',')
        else:
            fw.write(tags[i].text+'","')

    texts = driver.find_elements_by_xpath("//div[@class='cmn-article_text a-cf JSID_key_fonttxt m-streamer_medium']/p")
    for text in texts:
        print(text.text)
        fw.write(text.text.replace('\n',''))
    fw.write('"\n')
    #print(text.text)




def get_text():
    driver.get('https://www.nikkei.com/economy/economic/')
    size_articles=driver.find_element_by_class_name("m-pageNation").text
    size_articles=int(size_articles[0:size_articles.find('中')-1])
    print(size_articles)
    articles=driver.find_elements_by_xpath("//a[contains(@href,'article')]")

    urls =collect_articles(articles)
    with open(homepath+'/_university/nikkei/data/nikkei/economic.csv','w') as fw:
        fw.write('"title","date","tags","article"\n')
        for url in urls:
            driver.get(url)
            get_one_article(fw)

        for i in range(1,int(size_articles/20)):
            driver.get('https://www.nikkei.com/economy/economic/?bn='+str(i*20+1))
            articles=driver.find_elements_by_xpath("//a[contains(@href,'article')]")
            urls =collect_articles(articles)
            for url in urls:
                driver.get(url)
                get_one_article(fw)







class nikkei():
    def nikkei(ID,PASSWORD):
        driver.get('https://www.nikkei.com/economy/')
        driver.find_element_by_class_name('l-miH02_loginBtn').click()
        login(driver.current_url,ID,PASSWORD)
        get_text()