import json
import requests

from bs4 import BeautifulSoup as bs

class Follower(object):
    """ Follower类，保存每个关注者的信息

    属性:
        id: 关注者的slug
        name: 关注者的名字
    """

    def __init__(self, id, name):
        """使用关注者id和名字初始化对象"""
        self.id = id
        self.name = name

    def get_name(self):
        """获取关注者名字"""
        return self.name

    def get_id(self):
        """获取关注者id"""
        return self.id



class FollowerList(object):
    """"FollowerList类，保存所有follower的列表
    属性:
        fList: follower的列表
    """

    def __init__(self):
        """初始化空列表"""
        self.fList = []

    def insertFollower(self, follower):
        """在列表中增加一个关注者"""
        self.fList.append(follower)

    def displayFollower(self):
        """显示列表中所有关注者"""
        for i, follower in enumerate(self.fList):
            print("No.=", i+1, ", slug=", follower.get_id(), ", name=", follower.get_name(), sep='')

    def saveText(self, filename):
        """以csv格式保存关注者信息到文本文件"""
        f = open(filename, 'w')
        f.write('"id","name"\n')
        for follower in self.fList:
            f.write('"%s","%s"\n' % (follower.get_id(), follower.get_name()))
        f.close()

    def readweb(self, url):
        """从指定网址读取关注者列表

           注意：一定要使用User-Agent
        """
        html = requests.get(url, headers={'User-Agent': "User-Agent:Mozilla/5.0"})

        data = json.loads(html.text)
        for people in data:
            f = Follower(people['slug'], people['name'])
            self.insertFollower(f)


def test():
    """测试程序"""

    #readweb("https://zhuanlan.zhihu.com/wajuejiprince/followers?page=1")
    # 真实url是下面这个，卡了好久
    followerList = FollowerList()
    followerList.readweb("https://zhuanlan.zhihu.com/api/columns/wajuejiprince/followers?limit=20")
    followerList.displayFollower()
    followerList.saveText("follower.txt")


if __name__ == '__main__':
    test()

