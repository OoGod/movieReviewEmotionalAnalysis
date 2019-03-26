import csv

filename = 'test-douban.csv'

data = ''
with open(filename) as f:
    reader = csv.reader(f)
    for i in reader:
        data += i[-1]
        data += "\n"
with open('data.txt','w') as f:
    f.write(data)

print(data)
