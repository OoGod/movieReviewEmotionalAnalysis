import requests
import json
import sys

search_url = 'https://movie.douban.com/j/subject_suggest?q={}'

def search(name):
    response = requests.get(search_url.format(name))
    namelist = json.loads(response.text)
    x = 0
    print('id\tname')
    list_a = []
    for i in namelist:
        print('%s\t%s'%(x,i['title']))
        dict_a = {x:i['title']}
        list_a.append(dict_a)
        x += 1
    print(list_a)
    print("您想要的查询结果可能是可能是这些，请输入id进行查询")
    input_id = sys.stdin.readline().strip()
    movie_id = namelist[int(input_id)]['id']
    return movie_id


if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except Exception as e:
        print("错误原因：",e)
    else:
        movie_id = search(name)
        print(movie_id)

    pass