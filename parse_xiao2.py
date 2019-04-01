# coding=utf-8
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import selenium.webdriver.support.ui as ui  
from selenium.webdriver.common.action_chains import ActionChains  
from bs4 import BeautifulSoup as bs
import time      
import re      
import os
import csv

#打开Firefox浏览器
driver = webdriver.PhantomJS()
driver1 = webdriver.PhantomJS()
i = 0
reviews = ''
while i<1:
    num = i*20
    url ="https://movie.douban.com/subject/1292052/reviews?start="+str(num)
    print(url)
    driver.get(url)
    #用户姓名 超链接
    elem1 = driver.find_elements_by_xpath("//div[@class='main-bd']/h2/a")
    for n in elem1:
        print(n.text) 
        link = n.get_attribute("href")
        print(link,type(link))
        driver1.get(str(link))
        soup = bs(driver1.page_source,'lxml')
        con = soup.find_all("div",{"class":"review-content clearfix"})
        reviews += con
        print(con)

    i = i + 1

with open('review.txt','w') as f:
    f.write(con)
    print("评论已写入文件review.txt")
