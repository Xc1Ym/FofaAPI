# -*- coding: utf-8 -*-
# author: Xc1Ym
# github: https://github.com/Xc1Ym/FofaAPI
# If you have any problems, please give feedback to https://github.com/Xc1Ym/FofaAPI/issues
import requests
import json
import argparse

'''
该fofa_API回返回头像、邮箱、fofa币、fofa版、fofa会员类型、用户名
分别对应avatar、email、fcoin、version、vip、username

请输入API身份认证参数，email为登录邮箱，key为个人资料中的API key
'''

email = ""
key = ""

class fofa:

    # 获取api信息
    @staticmethod
    def Get_api(email_get_api, key_get_api):
        try:
            api = "https://fofa.so/api/v1/info/my?email={}&key={}".format(email_get_api, key_get_api)
            # print(api)
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

    # 获取相关版本信息

    @staticmethod
    def Get_version(r):
        print("API版本：v1.0")
        print("Fofa版本：" + r['fofacli_ver'])









# main
print()
ff = fofa()
request,request_json = ff.Get_api(email,key)

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
    """
print(bn)

parser = argparse.ArgumentParser()
parser.add_argument("--version", "-V", help="获取相关版本信息")
parser.add_argument("--search", help("普通搜索"))
parser.parse_args()
