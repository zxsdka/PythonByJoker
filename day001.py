print('你好', '世界')
print('hello', 'world', sep=', ', end='!')
print('goodbye, world', end='!\n')

# 1.

# c = float(input('请输入摄氏温度: '))

# f =  (c*1.8)+32

# print('%.1f摄氏度 = %.1f华氏度' % (c, f))

# 2.

# import math

# radius = float(input('请输入半径：'))

# length = float(input('请输入高：'))

# area = radius * radius * math.pi

# volume = area * length

# print('面积= %.2f' %area)

# print('体积= %.2f' %volume)

# 3.

# feet = float(input('请输入英尺：'))

# meter =feet*0.305

# print('%.2f'%meter)

# 4.

# m = float(input('请输入水量：'))

# initialtemperature=float(input('请输入初始温度：'))

# finaltemperature = float(input('请输入最终温度：'))

# q = m *(finaltemperature-initialtemperature)*4184

# print('%.1f'%q)

# 5.

# cha=float(input('请输入差额：'))

# nian=float(input('请输入年利率：'))

# li = cha * (nian/1200)

# print('利息是%.5f'%li)

# 6.

# v0 =float(input('请输入初始速度：'))

# v1 =float(input('请输入末速度：'))

# t  =float(input('请输入占用时间：'))

# a  =(v1-v0)/t

# print('平均加速度为：%.4f'%a)

# 7.

# number = float(input('请输入每月存款数：'))

# rate =0.05 /12

# interest = 1 +rate

# count =[0]

# for i in range(6):

# month = (100 + count[i]) * interest

# count.append(month)

# print('六个月后的账户总额：%.2f'% count[6])

# 8.

# number=input('请输入1~1000的一个整数:')

# bai =int(number[0])

# shi =int(number[1])

# ge =int(number[2])

# sum =bai+shi+ge

# print('%d'%sum)

9.
# import math

# r = eval(input('请输入半径：'))

# side = 2 * r * math.sin(math.pi/5)

# Area = 5 * side ** 2 / (4 * math.tan(math.pi/5))

# print("面积是：",format(Area,'5.2f'))
10.
import math
x1,y1 = eval(input("请输入第一个点的经度和纬度："))
x2,y2 = eval(input("请输入第二个点的经度和纬度："))
radius = 6371.01
x11 = math.radians(x1) #math.radians()函数将度数转换成弧度数
y11 = math.radians(y1)
x22 = math.radians(x2)
y22 = math.radians(y2)
d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
print("两点之间距离 %fkm"%d)
# #11.五角形的面积
# import math
# s = float(input('请输入五角形的边长：'))
# Area = (5*s*s)/(4*math.tan(math.pi/5))
# print('五角形的面积为：%f'%Area)




# #12.一个正多边形的面积
# import math
# s = float(input('请输入正多边形的边长：'))
# n = float(input('请输入多边形有几条边：'))
# Area = (n*s*s)/(4*math.tan(math.pi/n))
# print('正多边形的面积为：%f'%Area)



# #13.找出ASCII码的字符3
# a = int(input('请输入一个ASSCII码(0-127):'))
# print(chr(a))


# #14.工资表
# name = input('Enter employee\'s name:\000\000') 
# number = int(input('Enter number of hours worked in a week:\000\000')) 
# pay = float(input('Enter hourly pay rate:\000\000')) 
# federal = float(input('Enter federal tax withholding rate:\000\000')) 
# state = float(input('Enter state tax withholding rate:\000\000')) 
# print('Employee Name:\000'+name) 
# print('Hours worked:\000%.1f'%(float(number))) 
# print('Pay Rate:\000$'+str(pay)) 
# print('Gross Pay:\000$'+str(number*pay)) 
# print('Deductions:\n\000Federal Withholding(20.0%):\000$'+str(number*pay*0.2)+'\n\000State Withholding(9.0%):\000$'+ 
# str(number*pay*0.09)+'\n\000Total Deduction:\000$%.2f'%((number*pay*0.2)+(number*pay*0.09))) 
# print('Net Pay:\000$%.2f'%(((number*pay)-((number*pay*0.2)+(number*pay*0.09))))) 



# #15.反向数字
# a = input('请输入一个四位数整数：')
# print(a[::-1])


# #16.加密
# import hashlib
# m = hashlib.md5()
# a = input('请输入字符串：')
# m.update(bytes(a,encoding='utf8'))
# with open('password.txt','w')as file:
#     file.write(m.hexdigest())
# print(m.hexdigest())





















