
# s1 = set()
# print(s1.add(1))

# a = 'hello'
# c = int(input('请输入重复次数：'))
# t = 0
# while t <= c:
#     print('分割线'.center(50, '-'))
#     t += 1

# def line(char, num):
#     c = int(input('请输入重复次数：'))
#     t = 0
#     while t < c:
#         print(char * num)
#         t += 1
# line('^', 20)

# def sum1(n1, n2):
#     return n1 + n2
# res = sum1(11, 22)
# # print('计算结果：%d' %res)
# print(f'{11} + {22} = {res}')


# class student:
#     def __init__(self, name, age) : # 添加‘姓名’‘年龄’属性
#         self.name = name
#         self.age = age
#
# stu1 = student('小明', 18)
# stu1.age()
#
#
# @staticmethod
# def is_valid(a, b, c):
#     '''判断三条边是否构成三角形(静态方法)'''
#     return a + b > c and b + c > a and a + c > b

# areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
#          "bedroom", 10.75, "bathroom", 10.50]
# areas_1 = areas + ['poolhouse24.5']
# print(areas_1)

# list_2 = [9, 3, 6, 12, 234624, 4364, 34763]
# list_2.sort(4364)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# # Paste together first and second: full
# full = first + second
#
#
# # Sort full in descending
# #full_sorted = sorted(full, reverse = True)
# full.sort(reverse = True)
#
# # Print out full_sorted
# print(sorted(full, reverse = True))
# print(full)

# # Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
#
# # Use append twice to add poolhouse and garage size
# areas.append(24.5)
# areas.append(15.45)
#
#
# # Print out areas
# print(areas)
#
# # Reverse the orders of the elements in areas
# # areas.reverse()
#
# # Print out areas
# # print(areas)
# print(reversed(areas))
#
#
# # Definition of radius
# r = 192500
#
# # Import radians function of math package
# from math import radians
#
# # Travel distance of Moon over 12 degrees. Store in dist.
# dist = r * radians(12)
# # print(f'长度为：{r} * {radians(12)} = {r * radians(12)}') 可直接print
#
# # Print out dist
# print(dist)
#
#
# x = [4 , 9 , 6, 3, 1]
# x[1]
# print(x)

# import numpy as np
# np.array_1 = np.array([True, 1, 2]) + np.array([3, 4, False])
# print(np.array_1)
#
# list_1 = [True, 1, 2]
# list_2 = [3, 4, False]
# list_3 = list_1 + list_2
# print(list_3)


# list_1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# print(list_1[1])
#
# import numpy as np
# np_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# np_2 = np.array(([1, 2, 3, 4], [5, 6, 7, 8]))
# print(type(np_1[0, 1:]))
# print(np_1.shape)
# print(np_1[0:, -2:])
# print(type(np_2[0, 1:]))
# print(np_2.shape)
# print(np_2[0:, -2:]) # 最后结果与np_1一样，但细节上的区别在哪？？？


# baseball = [[180, 78.4],
# #             [215, 102.7],
# #             [210, 98.5],
# #             [188, 75.2]]
# #
# # import numpy as np
# # np_baseball = np.array(baseball)
# # height = np_baseball[:, 0]
# # weight = np_baseball[:, 1]
# # np_baseball_bmi = height / weight ** 2
# # print(height)
# # print(weight)
# # print(np_baseball_bmi)
# #
# #
# # np_baseball_3d = np.concatenate([np_baseball, np_baseball_bmi], axis = 1)
# # print(np_baseball_3d)


print( 8 + bool(1))
print(bool(0))