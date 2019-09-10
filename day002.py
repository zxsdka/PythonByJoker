# 1.
# import math
# a = float(input('请输入a：'))
# b = float(input('请输入b：'))
# c = float(input('请输入c：'))
# x  = b*b-4*a*c
# if x> 0:
#     r1 = (-b+math.sqrt(x))/(2*a)
#     r2 = (-b-math.sqrt(x))/(2*a)
#     print(r1,r2)
# elif x==0:
#     r1 = -b/2*a
#     print(r1) 
# else:
#     print("The equation has no real roots")

# 2.
# import random
# x = int(input('请输入两个随机数的和：'))
# a = random.randint(0,100)
# b = random.randint(0,100)
# if x == a + b:
#     print('True')
# else:
#     print('False')
#  3.

# def main():
#     t = int(input('Enter today is day（Sunday=0，Monday=1...Saturday=6):'))
#     f= int(input('Enter the number of days elapsed since today:'))
#     tday = mathtoday(t)
#     fday = mathfday(t,f)
#     print('Today is %s and the future day is %s'%(Nday,Fday))

# def mathtoday(Fday):
#     if Fday == 0:
#         today = 'Sunday'
#     elif Fday == 1:
#         today = 'Monday'
#     elif Fday == 2:
#         today = 'Tuesday'
#     elif Fday == 3:
#         today = 'Wednesday'
#     elif Fday == 4:
#         today = 'Thursday'
#     elif Fday == 5:
#         today = 'Friday'
#     elif Fday == 6:
#         today = 'Saterday' 
#     return today
# def mathFday(Nday,Fday):
#     Fuday = (Nday + Fday) % 7
#     return mathtoday(Fuday)

# main()
# 4.
# num1,num2,num3 = input('请输入三个数：').split(',')
# num1 = float(num1)
# num2 = float(num2)
# num3 = float(num3)
# if num1 > num2:
#     if num1 > num3:
#         if num2 > num3:
#             print(num3,num2,num1)
#         else:
#             print(num2,num3,num1)
#     else:
#         print(num2,num1,num3)
# else:
#     if num1 > num3:
#         print(num3,num1,num2)
#     elif num2 > num3:
#         print(num1,num3,num2)
#     else:
#         print(num1,num2,num3)
# 5.

# weight1 = float(input('第一种重量是:')) 
# price1 = float(input('第一种价格是:'))
# weight2 = float(input('第二种重量是:'))
# price2 = float(input('第二种价格是:'))
# num1 = float(price1)/float(weight1)
# num2 = float(price2)/float(weight2)
# if num1 < num2:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')
# 6.

# import calendar 
# def num(year,month):
# 	print(calendar.monthrange(year, month)[1])
# def start():
# 	year = int(input('Enter year: ')) 
# 	month = int(input('Enter month number: '))
# 	num(year,month)
# start()
# 7.

# import random
# x = int(input('请输入你的猜测（1为正，2为反）：'))
# a = random.randint(1,2)
# if x == a:
#     print('你猜对了')
# else:
#     print('你猜错了')


# 8.
# import random
# U_res = int(input('0:石头,1:剪刀,2:布>>>'))
# C_res = random.randint(0,2)
# if C_res == U_res:
#     print('平局')
# else:
#     if C_res == 0 and U_res == 1:
#         print('电脑赢了 ')
#     elif C_res == 1 and U_res == 2:
#         print('电脑赢了 ')
#     elif C_res == 2 and U_res == 0:
#         print('电脑赢了 ')
#     else:
#         print('你赢了 ')
# 9.
# year = int(input('输入哪一年:'))
# m = int(input('输入月份1-12:'))
# d = int(input('输入月份第几天1-31:'))
# a = ['周六','周日','周一','周二','周三','周四','周五']
# if m == 1:
#     m = 13
#     year = year - 1
# if m ==2:
#     m = 14
#     year = year - 1
# h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
# day = a[h]
# print('那一天是一周中的:%s' %day)


# 10.

# import random
# number = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
# flower = ['Plum','Heart','block','Spade']

# choice1 = random.choice(['Ace','2','3','4','5','6','7','8','9','10','J','Q','K'])
# choice2 = random.choice(['Plum','Heart','block','Spade'])

# print('The card you picked is the\000'+choice1+'\000of\000'+choice2)

# 
# 11.
# num = input('输入一个三位数：')
# if int(num[0])==int(num[2]):
#     print('是回文数')
# else:
#     print("不是回文数")

# 12.
# a,b,c = map(float,input('enter three edge:').split(','))
# if a+b>c and a+c>b and b+c>a:
#     L = a+b+c
#     print("其周长为",L)
# else:
#     print("不是三角形三条边") 

# 13.
# x = 1
# zheng = 0
# fu = 0
# i = 0
# sum1 = 0
# while x!=0:
#     x = int(input('输入一个整数，以输入值0来结束：'))
#     if(x>0):
#         zheng += 1
#     elif(x<0):
#         fu += 1
#     i += 1
#     sum1 = sum1 + x
# if sum1 != 0:
#     xxx = sum1/(i-1)
#     print('输入的正数有%d个，输入的负数有%d个，这组数的和为%d，这组数的平均数为%.2f'%(zheng,fu,sum1,xxx))
# else:
#     print('结束')
# 14.
# money = 10000
# sum1 = 0
# for i in range(1,14):
#     money = money * 0.05 + money
#     if i ==10:
#          print('十年之后的学费：%.2f'%money)
#     if i >= 10: 
#         sum1 += money
# print('十年后大学四年的总学费为：%.2f'%sum1)
# 16.
# geshu = 0
# for i in range(100,1001):
#     if i%5 == 0 and i%6 == 0:
#         print(i,end=' ')
#         geshu += 1
#         if geshu % 10 == 0:
#             print('\n')
# 17.
# n = 0
# m = 0
# while n**2 <= 12000:
#     n += 1
# print('n的平方大于12000的最小整数n为：%d'%n)

# while m**3 < 12000:
#     m += 1
# print('n的立方大于12000的最大整数n为：%d'%(m-1))
# 18.
# sum1 = 0
# sum2 = 0
# for i in range(1,50001):
#     sum1 += 1/i
#     i += 1
# print('从左向右计算为：',sum1)
# for i in range(50000,0,-1):
#     sum2 += 1/i
#     i -= 1
# print('从右向左计算为：',sum2)

# 19.
# sum1 = 0
# for i in range(3,100,2):
#     sum1 += (i-2)/i
# print('数列的和为：',sum1) 
# 20.
# pi = 0
# i = int(input('输入i的值：'))
# for j in range(1,i+1):
#     pi += 4 * ((-1)**(1+j)/(2*j-1))
# print('π的值为：%f'%pi)
# 20.
# for i in range(1,10000):
#     x = 0
#     for j in range(1,i):
#         if i % j == 0:
#             x += j
#     if x == i:
#         print('10000以下的完全数有：%d'%x)
# 21.
# list1 = []
# for i in range(1,8):
#     for j in range(1,8):
#             if i != j and sorted([i,j]) not in list1:
#                 list1.append([i,j])
# print('所有可能的组合为：',list1)
# print('组合总个数为：',len(list1))
