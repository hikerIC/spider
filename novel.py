from bs4 import BeautifulSoup as bs
import re
import requests

kv = {'user-agent':'Mozilla/5.0'}
url='https://www.zwdu.com/book/26073/'
#url = 'https://www.zwdu.com/book/26073/8164202.html'
try:
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("失败")

soup = bs(r.text, 'lxml')
print(soup.find_all('div', 'list'))

#print(soup.select('a[href=/book/26073]'))
