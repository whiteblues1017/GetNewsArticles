# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
homepath=os.path.expanduser('~')

#Chromeを操作
driver = webdriver.Chrome(executable_path=homepath+"/driver/chromedriver")

def login(ID,PASSWORD):
    driver.find_element_by_name("login_id").send_keys(ID)
    driver.find_element_by_name("login_password").send_keys(PASSWORD)

    driver.find_element_by_class_name("LoginBtn").click()

def filewrite(url,fw):
        driver.get(url)

        titles=driver.find_element_by_class_name("ArticleTitle").text
        text=driver.find_element_by_class_name("ArticleText").text
        try:
            tags=driver.find_element_by_class_name("Tag").text.split('\n')
        except:
            tags=''
        title=titles.split('\n')
            #date=titles[title.find('\n'):-1]
        print(title[0])
        print(tags)
        print(text)

        fw.write('"'+title[0]+'","')
        fw.write(title[len(title)-1]+'","')
        if len(tags)==0:
            fw.write('","')

        for i in range(len(tags)):
            if i==len(tags)-1:
                fw.write(tags[i]+'","')
            else:
                fw.write(tags[i]+',')
        fw.write(text.replace('\n','')+'"\n')


def get_articles():
    driver.get("http://www.asahi.com/eco/list/nature.html")
    #articles=driver.find_element_by_class_name("Section SectionFst").get_attribute('href')
    articles=driver.find_elements_by_xpath("//a[contains(@href,'articles')]")
    with open(homepath+'/_university/nikkei/data/asahi/nature.csv','w') as fw:
        fw.write('"title","date","tags","article"\n')
        urls =[]
        for article in articles:
            url = article.get_attribute('href')
            print(url)
            urls.append(url)
        for url in urls:
            filewrite(url,fw)
            #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'Btn')))
            #driver.get("http://www.asahi.com/national/list/incident.html")



class asahi():
    def asahi(ID,PASSWORD):
        driver.get('https://www.asahi.com/')
        driver.find_element_by_class_name("LoginGuest").click()
        login(ID,PASSWORD)
        get_articles()