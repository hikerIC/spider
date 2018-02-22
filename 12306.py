import requests
import json
import datetime
import time
"""
data各字段：
1 预订
3 车次
6 出发站
7 到达站
8 开车时间
9 到达时间
10 历时

23 软卧
26 无座
28 硬卧
29 硬座
31 一等座
32 二等座

"""

def stations():
    favorite_names = '@bji|北京|BJP|0@sha|上海|SHH|1@tji|天津|TJP|2@cqi|重庆|CQW|3@csh|长沙|CSQ|4' \
                     '@cch|长春|CCT|5@cdu|成都|CDW|6@fzh|福州|FZS|7@gzh|广州|GZQ|8@gya|贵阳|GIW|9' \
                     '@hht|呼和浩特|HHC|10@heb|哈尔滨|HBB|11@hfe|合肥|HFH|12@hzh|杭州|HZH|13' \
                     '@hko|海口|VUQ|14@jna|济南|JNK|15@kmi|昆明|KMM|16@lsa|拉萨|LSO|17' \
                     '@lzh|兰州|LZJ|18@nni|南宁|NNZ|19@nji|南京|NJH|20@nch|南昌|NCG|21' \
                     '@sya|沈阳|SYT|22@sjz|石家庄|SJP|23@tyu|太原|TYV|24@wlq|乌鲁木齐南|WMR|25' \
                     '@wha|武汉|WHN|26@xni|西宁|XNO|27@xan|西安|XAY|28@ych|银川|YIJ|29' \
                     '@zzh|郑州|ZZF|30@szh|深圳|SZQ|shenzhen|sz|31@xme|厦门|XMS|xiamen|xm|32'

    f = favorite_names.split('@')
    for i in f:
        print(i)


def get12306(start, end, startdate):
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
    data = {'leftTicketDTO.train_date': startdate,
            'leftTicketDTO.from_station': start,
            'leftTicketDTO.to_station': end,
            'purpose_codes': 'ADULT'}

    try:
        response = requests.get(url, params=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        if response is None:
            print("网站错误，请重试")
            return

        #print(response.text)

        r = response.json()
        stations = r['data']['map']
        found = False
        for result in r['data']['result']:
            data = result.split('|')
            if data[28]!='无' and data[28]!='':
                found = True
                print(startdate, '车次:{:5s} 出发站:{:8s} 到达站：{:8s} 硬卧：{:4s} 硬座：{:4s}'.format(
                                 data[3], stations[data[6]], stations[data[7]], data[28], data[29]))
        if not found:
            print(startdate, "全部票已经卖光了")


sdate0 = datetime.datetime.strptime('2018-02-17', '%Y-%m-%d')
for i in range(10):
    sdate = sdate0 + datetime.timedelta(days=i)
    startdate = sdate.strftime("%Y-%m-%d")
    get12306('SHH', 'HBB', startdate)
    time.sleep(5)

