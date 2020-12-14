# # a = 1
# # if a == 0:
# #     print("a==0")
# # elif a==1:
# #     print("a==1")
# # elif a==2:
# #     print("a==2")
# # else:
# #     print("a:=0")
#
# """
# 分段函数
#  3x-5(x>1)
#  f(s)=x+2(-1<=x<=1)
#     5x+3 (x<-1)
# """
#
# # 分支结构


#  多重分支

# x = 0
# y = 0
# if x > 1:
#     y = 3 * x - 5
# elif x < -1:
#     y = 5 * x + 3
#
# else:
#     y = x + 2
#
# print("y=",y)


""" 循环结构"""
# result = 0
# for i in range(101):
#     print(i)
#     result=result+i
# print(result)

#2.加入分支结构实现1-100之间的偶数求和

#break 和Continue
# for i in range(1,100):
#     if i==10:
#         # break?
#         continue
#     print(i)

"""猜数字"""
import random
# person_number=0
computer_number=random.randint(0,100)
while 1:
    person_number=int(input("请输入对应值:"))
    if computer_number>person_number:
        print("Too small")
    elif computer_number<person_number:
        print("Too big")
    else:
        print("Congratulation！,Computer_number is:",computer_number)
        break
