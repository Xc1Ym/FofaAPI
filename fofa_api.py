# -*- coding: utf-8 -*-
# author: Xc1Ym
# github: https://github.com/Xc1Ym/FofaAPI
# If you have any problems, please give feedback to https://github.com/Xc1Ym/FofaAPI/issues
import requests
import json
import argparse
import base64
from prettytable import PrettyTable

'''
该fofa_API利用官方API实现，根据Fofa会员等级返回查询信息
同时还可以查询部分Fofa基础信息


请输入API身份认证参数，email为登录邮箱，key为个人资料中的API key
'''

email = ""
key = ""

class fofa:

    # 获取基础信息
    @staticmethod
    def Get_me(email_get_api, key_get_api):
        try:
            api = "https://fofa.so/api/v1/info/my?email={}&key={}".format(email_get_api, key_get_api)
            r = requests.get(api)
            r_json = json.loads(r.text)
            return r,r_json
        except requests.exceptions as e:
            print(e)


    # 获取基础信息
    @staticmethod
    def Get_information(r):
        print("当前用户昵称：" + r['username'])
        print("当前用户头像：" + r['avatar'])
        print("当前用户邮箱：" + r['email'])
        print("Fofa版本：" + r['fofacli_ver'])


    # 搜索功能
    @staticmethod
    def Get_search(email_get_api, key_get_api, search):
        # 请求FofaAPI
        page = "1"
        size = "100"
        qbase64 = base64.b64encode(search.encode())
        api = "https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&page={}&size={}".format(email_get_api, key_get_api, qbase64.decode(), page, size)
        r = requests.get(api)
        r_json = json.loads(r.text)
        # 判断错误信息
        if r_json['error'] == "true":
            if r_json['errmsg'] == "Internal Server Error!":
                print("服务器错误")
            elif r_json['errmsg'] == "FOFA coin is not enough!":
                print("Fofa币不足")
            elif r_json['errmsg'] == "Result window is too large, page must be less than or equal to...!":
                print("结果窗口过大")
        # 格式化输出
        else:
            print("\n\n")
            print("页码：第{}页  数量：{}个".format(r_json['page'], r_json['size']))
            print("当前显示：{}个".format(size))
            print("查询内容：{}\n".format(r_json['query']))
            len_size = len(r_json['results'])
            r_list = r_json['results']
            table = PrettyTable(['序号', '地址', 'IP', '端口'])# 绘制表格
            # 判断数量和显示
            intsize = int(size)
            if intsize <= len_size:
                for i in range(intsize):
                    table.add_row([i+1, r_list[i][0], r_list[i][1], r_list[i][2]])
            else:
                for i in range(len_size):
                    table.add_row([i+1, r_list[i][0], r_list[i][1], r_list[i][2]])
            print(table)


# main
ff = fofa()
request,request_json = ff.Get_me(email,key)

bn = """
         ______     __               _____ _____ 
        |  ____|   / _|        /\   |  __ \_   _|
        | |__ ___ | |_ __ _   /  \  | |__) || |  
        |  __/ _ \|  _/ _` | / /\ \ |  ___/ | |  
        | | | (_) | || (_| |/ ____ \| |    _| |_ 
        |_|  \___/|_| \__,_/_/    \_\_|   |_____|  
    --------------------------------------------- 
    author: Xc1Ym
    github: https://github.com/Xc1Ym/FofaAPI
    version:v1.1
    """
print(bn)

parser = argparse.ArgumentParser()
parser.add_argument("--version", "-V", help="获取相关版本信息")
parser.add_argument("--search", help="普通搜索")
parser.add_argument("--fcion", help="查询Fofa币余额")
parser.add_argument("--rule", help="查询Fofa语法规则")
parser.parse_args()
word_search = input("请输入查询内容:")
# word_search = "qq.com"
ff.Get_search(email, key, word_search)
