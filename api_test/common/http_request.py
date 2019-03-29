
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     http_request.py  
   Description :  
   Author :        luoyunan
   date：          2019/03/27
   Copyright:      (c) luoyunan 2019
-------------------------------------------------
   Change Activity:
                   2019/03/27: 
-------------------------------------------------
"""
import requests
import json


class HttpRequest:
   """该类完成http get/post的请求，以及返回请求的结果"""

   def http_request(self,method,url,data,headers):
         # """根据请求方法来决定发起get请求还是post请求
         # method: get post
         # http的请求方式
         # url: 发送请求的接口地址
         # param: 随接口发送的请求参数
         # 以字典格式传递
         # rtype: 有返回值，返回结果是
         # 响应报文
         # """

      if method.upper()=="GET":

         try:
            resp=requests.get(url, data=data)
         except Exception as e:
            print("get请求出错了:{}".format(e))

      elif method.upper()=="POST":
         try:
            resp=requests.post(url, data=json.dumps(data), headers=headers)
         except Exception as e:
            print("post请求出错了：{}".format(e))
      else:
         resp = None
         print("请求出错了")

      return resp


#测试代码
if __name__ == '__main__':
   url="http://10.10.5.100:8876/com/scmDept/copyScmDept"
   headers={"Content-Type": "application/json", "Accept": "text/html", "X-PH-TOKEN": "27adbbbcd1ae4910966ec4888d4055cd"}
   method="POST"
   data={"id": "559731043574218752"}
   resp=HttpRequest().http_request(method, url, data, headers)
   print(resp.headers)
   print(resp.text)



