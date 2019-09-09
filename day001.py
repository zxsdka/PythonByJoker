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
#     month = (100 + count[i]) * interest
#     count.append(month)
# print('六个月后的账户总额：%.2f'% count[6])


# 8.
number=input('请输入1~1000的一个整数:')
bai =int(number[0])
shi =int(number[1])
ge =int(number[2])
sum =bai+shi+ge
print('%d'%sum)
