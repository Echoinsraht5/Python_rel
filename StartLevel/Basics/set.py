# 集合同列表类似，区别在于：1无序性 2互异性
# 交并差、比较运算、增删操作
# 集合中增删操作不可直接放入print()


# set1 = {'123', '135', '246', '456', '10', 'ekko', 'NS-5'}
# set2 = {'246', '123', '789', '233', 'nice', 'echo', 'TP-9'}
# list1 = ['2', '5', '5', '19', '5', '7']
#
# print(set1)
# print(list(set1))
# print(set(list1))
#
# print(set1 & set2)
# print(set1.intersection(set2))
#
# print(set1 | set2)
# print(set1.union(set2))
#
# print(set1 - set2)
# print(set2 - set1)
# print((set1 ^ set2) == (set1 | set2) - (set1 & set2))
#
# print(set1 < set2)

# 增删
s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)
s2.add(4)
print(s2)
s2.discard(1)
print(s2)
# print(s2.pop())
# print(s2)
print(s2.discard(2))
s2.clear()
print(s2)