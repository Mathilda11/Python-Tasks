import itchat
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from itchat.content import *


def lc():
    print("Finish Login!")


def ec():
    print("exit")


itchat.auto_login(hotReload=True, loginCallback=lc, exitCallback=ec)  # 登录微信（二维码）

#UserName = itchat.search_friends(name='宝')[0]["UserName"]
UserName = itchat.search_friends(name='公主裙·')[0]["UserName"]
def send_news():
    itchat.send_msg('YEEZY西安',UserName)
sched = BackgroundScheduler()
sched.add_job(send_news, 'date', run_date='2018-11-26 12:00:00')
sched.start()


# 6种格式的个人信息
ans = [['6123**************','181********','C'],
       ['6123**************','C','181********'],
       ['181********','6123**************','C'],
       ['181********','C','6123**************'],
       ['C','6123**************','181********'],
       ['C','181********','6123**************']
       ]


@itchat.msg_register(TEXT)   #这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
def simple_reply(msg):
    #这个是向发送者发送消息
    #itchat.send_msg('已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
    s = "%s" % msg["Text"]     #返回的给对方的消息，msg["Text"]表示消息的内容

    # 发送个人信息
    start = s.find('例如')
    if(start>0):
        temp = s[start+3:start+35]
        list = temp.split('，')
        if(len(list[0])==18):
            if(len(list[1])==11):
                return ",".join(ans[0])
            else:
                return ",".join(ans[1])
        if(len(list[0])==11):
            if(len(list[1])==18):
                return ",".join(ans[2])
            else:
                return ",".join(ans[3])
        if(len(list[0])==1):
            if(len(list[1])==18):
                return ",".join(ans[4])
            else:
                return ",".join(ans[5])

    # 发送问题答案
    begin = s.find('：')
    end = s.find('？')
    if(begin>0 and end>0):
        s = s[begin+1:end-1]
        try:
            s= eval(s) #将字符串s当成有效的表达式来求值并返回计算结果
        except SyntaxError:
            if(s.find('加')>0):
                s= s.replace('加','+')
            if(s.find('减') > 0):
                s = s.replace('减', '-')
            if(s.find('乘以') > 0):
                s = s.replace('乘以', '*')
            if(s.find('乘') > 0):
                s = s.replace('乘', '*')
            if(s.find('乘以') > 0):
                s = s.replace('乘以', '*')
            if (s.find('除以') > 0):
                s = s.replace('除以', '*')
            s = eval(s)
        finally:
            return "%d" %s

    # 完成
    if(s.find('恭喜')>0):
        sys.exit(1)

itchat.run()



