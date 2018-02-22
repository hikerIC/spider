from bs4 import BeautifulSoup as bs
import re
from urllib.request import urlopen


def savebook(url, num, text):
    url = 'https://www.zwdu.com' + url
    html = urlopen(url)
    soup = bs(html, 'lxml')
    print(soup.find_all('content'))


url='https://www.zwdu.com/book/26073/'
#url = 'https://www.zwdu.com/book/26073/8164202.html'
html = urlopen(url)
soup = bs(html, 'lxml')
i = 3070

savebook('/book/26073/11992875.html', i, '飞仙门主')
