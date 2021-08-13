# -*- coding: utf-8 -*-
# exercise 1
# print('请依次选取6个红球（注意不能重复）')
# list1 = []
# list2 = []
# k=1
# while True:
#     if k < 7:
#         x = input('请输入您选取的第'+str(k)+'个红球：')
#         if x in list1:
#             print('选取重复，请重新选取:')
#             continue;
#         else:
#             list1.append(x)
#             k += 1
#     elif k < 9:
#         x = input('请输入您选取的第'+str(k-6)+'个蓝球:')
#         if x in list2:
#             print('选取重复，请重新选取:')
#             continue;
#         else:
#             list2.append(x)
#             k += 1
#     else:
#         break
# print(f'您选择的红球为： {" ".join(list1)} \n您选择的蓝球为： {" ".join(list2)}')

# exercise 2


# def howheight(n):
#     starthei = float(n)
#     x = 0
#     while True:
#         x += starthei *1.5
#         starthei /= 2
#         yield x
#
#
# f = howheight(100)
# x = int(input("输入你想计算第几次落地时的高度与行进总路程："))
# for i in range(x-1):
#     next(f)
# print(f"行进总路程为：{next(f)} \n当前高度为：{100 / pow(2,x)}")

# exercise 3
# import csv
# with open('data.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["username", "password", "age", "position", "department"])
#     writer.writerow(["alex", "abc123", "24", "Engineer", "IT"])
#     writer.writerow(["rain", "df2@432", "25", "Teacher", "Teching"])


# def changeid(n):
#     with open('data.csv', 'w') as file:
#         writer = csv.writer(file)
#         a = 0
#         for row in writer:
#             if a == n:
#                 row[2] = input("请输入新年龄：")
#                 row[3] = input("请输入新职位：")
#                 row[4] = input("请输入新部门：")
#                 break
#             a += 1
#
#
# def printid(n):
#     with open('data.csv') as file:
#         reader = csv.reader(file)
#         a = 0
#         for row in reader:
#             if a == n:
#                 print(row)
#             a += 1
#
#
# def pwdchange(n):
#     with open('data.csv', 'w') as file:
#         writer = csv.writer(file)
#         a = 0
#         for row in writer:
#             if a == n:
#                 row[1] = input("请输入新密码：")
#                 break
#

# def menu():
#     while True:
#         print(f'1:修改个人信息 \n2:打印个人信息：\n3:修改个人密码 \n4:按其它键退出系统')
#         x = input()
#         if x == '1':
#             changeid(a)
#         elif x == '2':
#             printid(a)
#         elif x == '3':
#             pwdchange(a)
#         else:
#             break
#
#
# n, k, a = 3, 0, 0
# while n>0:
#     with open('data.csv') as file:
#         reader = csv.reader(file)
#         x = input("用户名：")
#         y = input("密码：")
#         a = 0
#         for row in reader:
#             if x == row[0]:
#                 if y == row[1]:
#                     print("密码正确")
#                     k = 1
#                     break
#                 else:
#                     continue
#             a += 1
#         if k == 0:
#             a -= 1
#             if a != 0:
#                 print("密码错误,请重新输入：")
#             else:
#                 print("输错三次，退出程序。")
#         else:
#             break

# if k == 1:
#     menu()

# method 2 of the exercise 3

# import json
# from pathlib import Path


# # id = [
# #     {"username": "alex", "password": 'abc123', "age": "24", "position": "Engineer", "department": "It"},
# #     {"username": "rain", "password": 'df2@432', "age": "25", "position": "Teacher", "department": "Teching"}
# # ]
# # data = json.dumps(id)
# # Path("id.json").write_text(data)

# data = Path('id.json').read_text()
# id = json.loads(data)
# n = len(id)
# a, k, v = 3, 0, 0
# while a > 0:
#     x = input("用户名：")
#     y = input("密码：")
#     for i in range(n):
#         if x == id[i]["username"]:
#             if y == id[i]["password"]:
#                 print("密码正确")
#                 k = 1
#                 break
#             else:
#                 continue
#         v += 1
#     if k == 0:
#         a -= 1
#         if a != 0:
#             print("密码错误,请重新输入：")
#         else:
#             print("输错三次，退出程序。")
#     else:
#         break


# def menu():
#     while True:
#         print(f'1:修改个人信息 \n2:打印个人信息：\n3:修改个人密码 \n4:按其它键退出系统')
#         x = input()
#         if x == '1':
#             changeid(v)
#         elif x == '2':
#             printid(v)
#         elif x == '3':
#             pwdchange(v)
#         else:
#             break


# def changeid(v):
#     id[v]["age"] = input("请输入新年龄：")
#     id[v]["position"] = input("请输入新职位：")
#     id[v]["department"] = input("请输入新部门：")


# def printid(v):
#     print(id[v])


# def pwdchange(v):
#     id[v]["password"] = input("请输入修改后的密码：")


# if k == 1:
#     menu()

# import json
# from pathlib import Path
# id = [{"username": "alex", "password": 'abc123'}]
# data = json.dumps(id)
# Path("practice.json").write_text(data)
# id1 = [{"username": "ale", "password": 'abc123'}]
# data1 = json.dumps(id1)
# Path("practice.json").write_text(data1)
import csv
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "title", "content"])
#     name = 'alex'
#     title = 'alex的第一篇文章'
#     content = 'abcde'
#     writer.writerow([name, title, content])

# with open("data.csv", "a", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "title", "content"])
# f= open('data.csv', 'w')
# f.close()
# username = 'data'
# with open("data.csv", "a", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["nam", "title", "content"])
#
# with open(username + '.csv', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



# with open('data.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row[0] == 'alex':
#             print(row)

import os
# print(os.path.exists('data'+'.csv'))
# with open("new.txt",'w') as file:
#     print("hello")
# data = 'alex'
# f = open(data + '.csv', 'w')
# f.close()
# a=['1','2','3']
# b = a
# print(b)

# a = {
#         "username": "alex",
#         "password": "abc123",
#         "email": "123456@gmail.com",
#         "phonenum": "123456"
#     }
# b = a
# print(b['username'])


import json
from pathlib import Path
data = Path('id.json').read_text()
reader = json.loads(data)
newdata = []
# newdata1 ={}
n=len(reader)
for i in range(n):
    # newdata1 = reader[i]
    newdata.append(reader[i])

for i in range(n):
    if newdata[i]['username'] == 'alex':
        newdata[i]['username'] = 'rain'

print(newdata)


# import csv
# x=[]
# with open('data.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         x=row
#     print(len(reader))