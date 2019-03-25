# coding=utf-8
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import selenium.webdriver.support.ui as ui  
from selenium.webdriver.common.action_chains import ActionChains  
import time      
import re      
import os
import csv

#打开Firefox浏览器
driver = webdriver.Firefox()
i = 0
while i<1:
    num = i*20
    url = "https://movie.douban.com/subject/1292052/comments?start=" + str(num) +"&limit=20&sort=new_score&status=P"
    print url
    driver.get(url)
    #用户姓名 超链接
    elem1 = driver.find_elements_by_xpath("//div[@class='avatar']/a")
    for n in elem1:
        print n.get_attribute("title"), 
        print n.get_attribute("href")
        
    #用户评分
    elem2 = driver.find_elements_by_xpath("//span[@class='comment-info']/span[2]")
    for n in elem2:
        print n.get_attribute("class"), 
        print n.get_attribute("title")

    #有用数
    elem3 = driver.find_elements_by_xpath("//span[@class='comment-vote']/span[1]")
    for n in elem3:
        print n.text
        
    #日期
    elem4 = driver.find_elements_by_xpath("//span[@class='comment-time ']")
    for n in elem4:
        print n.text

    #评论
    elem5 = driver.find_elements_by_xpath("//span[@class='short']")
    for n in elem5:
        print n.text
        
    i = i + 1
