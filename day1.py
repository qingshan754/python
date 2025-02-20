#第一天学习python，练习了输入输出
# """use py design a game"""
# temp=input("不妨猜一下小甲鱼现在心里想的是哪个数字？")
# guss=int(temp)
# if guss==8:
#     print ("你是小甲鱼心里的蛔虫吗？")
#     print("哼，猜对了也没有奖励")
# else:
#     print("猜错了,我想的是8")
# print("游戏结束")

# 第二天学习python，练习了变量交换，反斜杠的用法，字符串的格式化输出
# x=3
# y=5
# x,y=y,x
# print(x,y)
# print ("Life is short,let's learn python.")
# print (r"D:\code\Py\day1.py")

#游戏改进
#获取随机数
# import random
# num=random.randint(1,10)
# print(num)
# #随机数的重现
# x=random.getstate()
# random.setstate(x)

#数字类型（包含实例化一个对象）
# import decimal 
# a=decimal.Decimal('0.3')
# b=decimal.Decimal('0.1')
# print(a+b)
####复数的表示
# x=1+2j
# print(x.real)
# print(x.imag)
#数字之间的运算
# a=3
# b=2
# a+b
# a-b
# a*b
# a/b
# a//b##地板除，向下取整
# a%b
# divmod(a,b)#返回商和余数
# abs(-250)##绝对值，abs复数等于模
# pow(2,3)##幂运算
# pow(2,3,5)##幂运算，第三个参数为模