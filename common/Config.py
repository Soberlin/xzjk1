# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 9:32
# @Author  : Sober
# @Site    : 
# @File    : Config.py
#IP+端口 生产环境
Host_name1='10.0.0.32:9080'            #线上环境商城32
Host_name2='10.0.0.35:9080'            #线上环境商城35
#测试环境
Test_name='192.168.20.2:9080'         #测试环境商城
#域名访问
MoreAdd='https://m.outdoorclub.com.cn'   #线上环境商城域名地址
MoreTestAdd='http://testm.outdoorclub.com.cn'

#邮箱配置
sender='liuguo@agleroc.com'
psw='qiq8aC9ddhTLLnNS' #授权码
receiver=['liuguo@agleroc.com','wuxianyang@agleroc.com','mingzhenlin@agleroc.com','xuhonghui@agleroc.com','huangyan@agleroc.com','zhangxiaoke@agleroc.com','jingjing@agleroc.com']
port=25
smtp_server = 'smtp.exmail.qq.com'


# 接口
html='/html'  #h5的接口
api='api'    #app的接口
appId='xingzhuang'    #appId
resultCode='2000 '   #返回码
userId='7129685'     #userId

#H5商城首页所有接口
index='/index/loadLayout'                 #首页接口
getNavBar='getindex/getNavBar'           #首页导航栏
getNo='/sCart/getNo'                    #获得卡片
getQRCode='/html/app/getQRCode'        #获取个人中心二维码
wxConf='/wechat/getWxConf'            #获得微信授权
share='/share/lockfansurl'           #微信分享锁粉
notification='api/notification/getUnreadCount'  #获得消息通知

#搜索关键词
search='/goods/selectGoodsByWords'  #搜索关键词









