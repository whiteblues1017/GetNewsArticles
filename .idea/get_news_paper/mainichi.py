# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import re
homepath=os.path.expanduser('~')

#Chromeを操作
driver = webdriver.Chrome(executable_path=homepath+"/driver/chromedriver")

def get_text(urls,fw):
    for url in urls:
        driver.get(url)
        #print(driver.find_element_by_class_name("post").text)
        try:
            post = driver.find_element_by_class_name('post').text
            title=driver.find_element_by_xpath('//h1').text
            texts=driver.find_element_by_class_name("main-text").find_elements_by_class_name("txt")
            tags = driver.find_element_by_xpath('//ul[@class="channel-list inline-list"]').text.split('\n')
            print(post)

            if post.find('会員限定有料記事')!= -1:
                continue
            else:
                date =driver.find_element_by_class_name('post').find_element_by_xpath('//time').text
                print(title)
                print(date)
                print(tags)

                fw.write('"'+title+'","'+date+'","')
                for i in range(len(tags)):
                    if i==len(tags)-1:
                        fw.write(tags[i]+'","')
                    else:
                        fw.write(tags[i]+',')
                for text in texts:
                    print(text.text)
                    fw.write(text.text.replace('\n',''))
                fw.write('"\n')
        except:
            continue

class mainichi():
    def mainichi():
        with open(homepath+'/_university/nikkei/data/mainichi/africa.csv','w') as fw:
            fw.write('"title","date","tags","article"\n')
            for i in range(1,21):
                driver.get('https://mainichi.jp/africa/'+str(i))

                articles=driver.find_elements_by_xpath("//a[contains(@href,'articles')]")

                print(articles)
                urls=[]
                for article in articles:
                    url = article.get_attribute('href')
                    print(url)
                    if url.find('sports')!=-1:
                        continue
                    urls.append(url)


                get_text(urls,fw)



