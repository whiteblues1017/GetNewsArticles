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

def get_text():
    driver.get('https://www.nikkei.com/economy/economic/')
    articles=driver.find_elements_by_xpath("//a[contains(@href,'article')]")

    for article in articles:
        url = article.get_attribute('href')
        print(url)


class nikkei():
    def nikkei(ID,PASSWORD):
        driver.get('https://www.nikkei.com/economy/')
        driver.find_element_by_class_name('l-miH02_loginBtn').click()
        login(driver.current_url,ID,PASSWORD)
        get_text()