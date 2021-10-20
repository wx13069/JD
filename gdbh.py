##软件：赚多多
# 下载链接：http://sd.bhrax.com/inviter/i4557E?userid=5803127
# 邀请码：1H9N65 感谢支持
# 感谢TOM大佬的sign算法支持，第一次写毛，水平有限，日志输出还没优化，有时间在去优化一下，脚本有不足的地方望大佬指导
# 使用方法，小黄鸟抓包搜索关键字coins
# 点开一条数据点击请求然后点RAW从从host开始一下的全部复制
# 再把复制的内容到这个网站转化一下http://www.songluyi.com/ChangeHeaderToDict/
# 复制右边的内容添加到青龙添加环境变量，转换完的内容注意一下每个 :" 后面可能有空格要手动去一下，还有最后 } 的前面加个这个“
# export userid=''
# export platform=''
# export gdbhtoken=''
# export UA=''
#
# #以上需要添加的变量都可以在header里面找到，添加完之后，添加任务每天运行一次就行
#

import requests
import time
import os
import hashlib


if "gdbhtoken" in os.environ and os.environ["gdbhtoken"]:
    gdbhtoken = os.environ["gdbhtoken"]
if "userid" in os.environ and os.environ["userid"]:
    userid = os.environ["userid"]
if "platform" in os.environ and os.environ["platform"]:
    platform = os.environ["platform"]
if "UA" in os.environ and os.environ["UA"]:
    UA = os.environ["UA"]

data = {"Host":"proxy.guodongbaohe.com","x-userid":userid,"x-appid":"2102202714","x-devid":"No-dev","x-nettype":"WIFI","x-agent":UA,"x-platform":platform,"x-devtype":"no","x-token":gdbhtoken,"accept-encoding":"gzip","user-agent":"okhttp/3.14.9"}

print(data)
timestamp = int(time.time())
a = timestamp
a = str(a)
##获取sign
sign = 'member_id='+userid+'&platform='+platform+'&timestamp='+a+'&faf78c39388faeaa49c305804bbc1119'
sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
print(sign)

r = requests.get(url='https://proxy.guodongbaohe.com/coins/checkin?member_id='+userid+'&platform=android&timestamp='+a+'&signature='+sign+'&',headers=data)

print(r.text,flush=True)
time.sleep(2)

i = 1
while i <= 6:
    timestamp = int(time.time())
    a = timestamp
    a = str(a)
    ##获取sign
    sign = 'member_id=' + userid + '&platform=' + platform + '&timestamp=' + a + '&faf78c39388faeaa49c305804bbc1119'
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
    print(sign)
    r = requests.get(url='https://proxy.guodongbaohe.com/coins/award?member_id='+userid+'&platform='+platform+'&timestamp='+a+'&signature='+sign+'&',headers=data)

    print(r.text,flush=True)
    print('执行第%d次广告任务' % i, flush=True)
    print('每个视频30秒，等待93秒',flush=True)
    time.sleep(93)
    i = i+1
