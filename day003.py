# 导入模块
# from wxpy import Bot
# 初始化机器人，扫码登陆
# bot = Bot()
# my_friend = bot.friends().search('游否', sex=MALE, city="深圳")[0]
#my_friend.send('Hello WeChat!')
# 发送图片
# my_friend.send_image('my_picture.jpg')
#1.五角数
# def getPentagonalNumber(n):
#     COUNT = 0
#     for i in range(1, n+1):
#         num = i*(3*i-1)/2
#         print("%d"%num,end= '  ')
#         COUNT += 1
#         if COUNT % 10==0:
#             print('\n')
        
# getPentagonalNumber(100)


# 2.求一个整数各个数字的和
# word = input('请输入整数：')
# j =len(word)
# list_num = []
# def sumDigits (word):
#     global j
#     global list_num
#     for i in range(len(word)):
#         a=int(word)%10
#         word = str(int(word)//10)
#         list_num.append(a)
#         j -= 1
#         if j == 0:
#             sum_ =sum(list_num)
#             print(sum_)
# sumDigits(word)
# 3.升序
# num1,num2,num3 = eval(input('请输入三个数(用逗号隔开)：'))
# def displaySortedNumbers(num1,num2,num3):

#     list = [num1,num2,num3]
#     a = sorted(list)
#     return a
# print('排序后为：',displaySortedNumbers(num1,num2,num3))    
# 4. 显示字符
# COUNT=0
# ch1 = 73
# ch2 = 91
# def printChars(ch1,ch2):
#     global COUNT
#     for i in range(ch1,ch2):
#         COUNT += 1
#         print(chr(i),end = " ")
#         if COUNT % 10 == 0:
#             print("\n")
            
# print(printChars(ch1,ch2))
# 5. 一年的天数
# year1 = 2010
# year2 = 2021
# def numberOfDaysInAYear(year1,year2):
#     for i in range(year1,year2):
#         if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#             print(i,"年有366天,是闰年")
#         else:
#             print(i,"年有365天")

# print(numberOfDaysInAYear(year1,year2))
# 6.两点距离
# def distance(x1,x2,y1,y2):
#     d=((x1-x2)**2+(y1-y2)**2)**0.5
#     print("两点间距离为：",'%.2f'%d)
# distance(2,3,4,5)
# 7.素数 gou
# i = 2
# c = []
# d = []
# def sushu(i,c,d):
#     while i <=31:
#         j = 2
#         while j <= i:
#             if i % j ==0:
#                 if i == j:
#                     c.append(i)
#                 break
#             j += 1
#         i += 1
#     print('P:',c) 
#     for p in c:
#         d.append(2**p-1) 
#     print('2^P-1:',d)  
# 
# 
# 
#9.
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("Current date and time is :", localtime)
# main()
# 
# 
# 
# 
# 10.
# import random
# def shaizi():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你输了')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你输了')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('你赢了')
# shaizi()























