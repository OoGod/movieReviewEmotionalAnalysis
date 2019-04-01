from selenium import webdriver
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from snownlp import SnowNLP
from pylab import mpl
import numpy as np
import csv
import jieba
import sys


class reviewsAnalysis(object):

    def __init__(self,url):
        self.url = url
        pass

    def parse_save(self):
        '''
        爬取评论并且保存到test-douban.csv中
        :return:
        '''
        # 写入文件
        c = open("test-douban.csv", "w")  # 写文件
        # c.write(codecs.BOM_UTF8)          #防止乱码
        writer = csv.writer(c)  # 写入对象
        writer.writerow(['序号', '用户名', '链接', '评分', '评分标题', '有用数', '日期', '评论'])
        # 打开Firefox浏览器 设定等待加载时间 访问URL
        driver = webdriver.PhantomJS()
        i = 0
        while i < 10:
            num = i * 20
            # url = "https://movie.douban.com/subject/1292052/comments?start=" + str(
            #     num) + "&limit=20&sort=new_score&status=P"
            url = self.url.format(str(num))
            print(url)
            driver.get(url)
            # 用户姓名 超链接
            elem1 = driver.find_elements_by_xpath("//div[@class='avatar']/a")
            # 用户评分
            elem2 = driver.find_elements_by_xpath("//span[@class='comment-info']/span[2]")
            # 有用数
            elem3 = driver.find_elements_by_xpath("//span[@class='comment-vote']/span[1]")
            # 日期
            elem4 = driver.find_elements_by_xpath("//span[@class='comment-time ']")
            # 评论
            elem5 = driver.find_elements_by_xpath("//span[@class='short']")
            # 循环写入20行评价
            tlist = []
            k = 0
            while k < 20:
                # 序号
                num = i * 20 + k + 1
                print(num)
                # 用户姓名
                name = elem1[k].get_attribute("title")
                print(name)
                # 超链接
                href = elem1[k].get_attribute("href")
                print(href)
                # 用户评分及内容
                score = elem2[k].get_attribute("class")
                print(score)
                content = elem2[k].get_attribute("title")
                print(content)
                # 有用数
                useful = elem3[k].text
                print(useful)
                # 日期
                date = elem4[k].text
                # 评论
                shortcon = elem5[k].text
                print(shortcon)

                # 写入文件
                templist = []
                templist.append(num)
                templist.append(name)
                templist.append(href)
                templist.append(score)
                templist.append(content)
                templist.append(useful)
                templist.append(date)
                templist.append(shortcon)
                writer.writerow(templist)

                k = k + 1

            i = i + 1

        c.close()
        pass

    def save(self):
        '''
        从csv文件中爬取评论数据，并且保存到data.txt中
        :return:
        '''
        filename = 'test-douban.csv'

        data = ''
        with open(filename) as f:
            reader = csv.reader(f)
            for i in reader:
                data += i[-1]
                data += "\n"
        with open('data.txt', 'w') as f:
            f.write(data)

        print(data)

    def fenci(self):
        '''
        根据data.txt中的评论数据并且进行分词和词云展示
        :return:
        '''
        with open('data.txt','r',encoding='utf-8') as f:
            text = f.read()
        print(type(text))

        # 结巴分词 cut_all=True 设置为精准模式
        wordlist = jieba.cut(text, cut_all=False)
        # 使用空格连接 进行中文分词
        wl_space_split = " ".join(wordlist)
        print(wl_space_split)

        # 对分词后的文本生成词云
        font = 'C:\Windows\Fonts\simhei.ttf'
        my_wordcloud = WordCloud(font_path = font).generate(wl_space_split)

        # 显示词云图
        plt.imshow(my_wordcloud)
        # 是否显示x轴、y轴下标
        plt.axis('off')
        plt.show()

    def analysis(self):
        '''
        读取data.txt中的评论数据，根据评论数据统计情感分数段并绘制对应的柱状图
        :return:
        '''
        with open("data.txt", "r", encoding='utf-8') as f:
            line = f.readlines()
        sentimentslist = []
        for i in line:
            s = SnowNLP(i)
            print(s.sentiments)
            sentimentslist.append(s.sentiments)

        plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
        plt.xlabel('Sentiments Probability')
        plt.ylabel('Quantity')
        plt.title('Analysis of Sentiments')
        plt.show()

    def analysis_wave(self):
        '''
        功能：情感波动分析
        读取data.txt中的评论数据，根据评论数据统计情感分数段并绘制对应的曲线图
        :return:
        '''
        source = open("data.txt", "r", encoding='utf-8')
        line = source.readlines()
        sentimentslist = []
        for i in line:
            s = SnowNLP(i)
            print(s.sentiments)
            sentimentslist.append(s.sentiments)

        result = [i - 0.5 for i in sentimentslist]

        # plt.plot(sentimentslist, 'k-')
        plt.plot(result, 'k-')
        plt.xlabel('Number')
        plt.ylabel('Sentiment')
        plt.title('Analysis of Sentiments')
        plt.show()
        pass

    def run(self):
        '''
        对评论相关数据进行爬取，并保存到文件中
        :return:
        '''
        self.parse_save()
        self.save()
        pass


if __name__ == '__main__':

    # url = sys.stdin.readline().strip()
    url = "https://movie.douban.com/subject/1292052/comments?start={}&limit=20&sort=new_score&status=P"
    xiaoShenKe = reviewsAnalysis(url)
    #xiaoShenKe.fenci()
    #xiaoShenKe.analysis()
    xiaoShenKe.analysis_wave()
