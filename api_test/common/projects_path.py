
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     projects_path.py  
   Description :  
   Author :        luoyunan
   date：          2019/03/27
   Copyright:      (c) luoyunan 2019
-------------------------------------------------
   Change Activity:
                   2019/03/27: 
-------------------------------------------------
"""
import os

#文件的路劲放在这里
project_path= os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


#测试用例的路径
case_path=os.path.join(project_path,"test_case","test_api.xlsx")

print(case_path)

if __name__ == '__main__':
   pass