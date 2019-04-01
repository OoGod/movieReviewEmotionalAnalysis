import requests
import json
import sys

url = 'https://movie.douban.com/j/subject_suggest?q={}'

def search(name):
    response = requests.get(url.format(name))
    namelist = json.loads(response.text)
    return namelist

if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except Except as e:
        print("错误原因：",e)
        print("请按照python search.py [name] 格式查询电影")
    else:
        namelist = search(name)
        x = 0
        print('id\tname')
        for i in namelist:
            print('%s\t%s'%(x,i['title'])) 
            x += 1
        print("您想要的查询结果可能是可能是这些，请输入id进行查询")
        movie_id = sys.stdin.readline().strip()
        print(movie_id,type(movie_id),len(movie_id))
        print(namelist[int(movie_id)]['id'])  
