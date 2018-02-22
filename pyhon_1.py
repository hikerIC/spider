import json
import requests


def readweb(url):
    """从指定网址读取关注者列表

       注意：一定要使用User-Agent
    """
    html = requests.get(url, headers = {
        'User-Agent': "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"})

    print(html.text)


def test():
    """测试程序"""

    readweb("https://www.icourse163.org/learn/DLUT-1002083017#/learn/content")


if __name__ == '__main__':
    test()

