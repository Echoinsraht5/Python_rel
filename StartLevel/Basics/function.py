# 函数

# def sum1():
#     num1 = input('请输入数字：')
#     num2 = input('请输入数字：')
#     print(f'{num1} + {num2} = {num1 + num2}')
# sum1()
#

# n1 = int(input('请输入数字：'))
# n2 = int(input('请输入数字：'))
# print(f'{n1} + {n2} = {n1 + n2}')

# def sum1(n1, n2):
#     res = n1 + n2
#     #print(f'{n1} + {n2} = {n1 + n2}')
#     print('%d + %d = %d' % (n1, n2, res))
# sum1(1, 2)

# def sum1(n1, n2):
#     return n1 + n2
# res = sum1(11, 22)
# print('计算结果：%d' %res)

# s = 'love Faye'
# print(s.rjust(50, '#'))

def asd():
    print('分割线'.center(51, '#'))
asd()

# a = 'hello'
# c = int(input('请输入重复次数：'))
# t = 0
# while t <= c:
#     print('分割线'.center(50, '-'))
#     t += 1

def line(char, num):
   #c = int(input('请输入重复次数：'))
    t = 0
    while t < 5:
        print(char * num)
        t += 1
line('^', 20)


