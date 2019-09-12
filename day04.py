# 1.
# score = int(input('enter score：'))
# if score >= 100-10:                                         
#     print("student  is %d and grade is A"%score)
# elif score >= 100-20:
#     print('student is %d and grade is B'%score)
# elif score >= 100-30:
#     print('student is %d and grade is c'%score)
# elif score >= 100-40:
#     print('student is %d and grade is D'%score)
# else:
#     print('student is %d and grade is f'%score)

# 2.
# def main():
#     a = [1,2,3,4,5,6,7,8,9]
#     for _ in a[::-1]:
#         print(_)
# main()



# 3.统计数字个数
# list=[5,6,9,8,2,4,1,5,5,5,2,6,3]
# a = set(list)
# def main():
#     for i in a:
#         count = list.count(i)
#         print(i,'出现的次数：',count)
# main()


# 4.大于平均数小于平均数
# def average(list):
#    pinjun = sum(list)/(len(list)*1.0)
#    return pinjun
# num1 = 0
# num2 = 0
# def fenshu(list_):
#    pinjun = average(list_)
#    for i in range(len(list_)):
       
#        global num1
#        global num2
#        if list_[i] > pinjun: 
#            num1 += 1
#        elif list_[i] < pinjun:
#            num2 += 1
#        else:
#            pass
#    print(num1)
#    print(num2)
#    print(pinjun)
# fenshu([2,4,2,4,8])


#5.随机产生100个0到9的整数，然后显示每个数的整数

#import numpy
#def suiji():
#    a = numpy.random.choice(range(1000))
#    return a
#for i in range(1000):
#    str1 = [suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji()]
#    print(str1)



#6. 返回最小元素的下标
# def indexOFSmallestElement(lst):
#    lst1 = lst
#    lst2 = sorted(lst)
#    zuixiao = lst2[0]

#    for i in range(len(lst1)):
#        if lst1[i] == zuixiao:
#            print('最小元素的下标再第%d个>>'%(i+1))
           
# indexOFSmallestElement([3,4,2,7,5,4,1,4,3,4])











    

    