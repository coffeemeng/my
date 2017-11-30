# -*- coding:utf-8 -*-
'''
时间:20171128
作者：恶作剧
备注：我的第一个函数
'''
def user():
    num = ["tom", "joy", "jack"]
    people = {
        "tom": {  # 逗号后面用空格
            "age": "14",
            "high": "172",
            "sex": "boy"
        },
        "joy": {
            "age": "12",
            "high": "172",
            "sex": "boy"
        },
        "jack": {
            "age": "13",
            "high": "175",
            "sex": "boy"
        },
    }
    for key in num:
    # print(people[key])
        print("姓名：%s,年龄：%s,身高:%s,性别:%s" %
            (key, people[key]["age"], people[key]["high"], people[key]["sex"]))
            
user()
