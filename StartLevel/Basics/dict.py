# 列表：有序对象集合 字典：无序对象集合
# 字典使用键（key：索引）值（value：数据）存储数据
# 增类操作无法放入print()、带赋值改类操作无法放入print()，删/查类操作可直接放入print()


d_1 = {'Name': '小明',
       'gender': '男',
       'age': 21,
       'height': 182
       }
print(type(d_1))

# add & modify
d_1['Name'] = ('小张')
d_1['Weight'] = ('70')
print(d_1)

#delete
print(d_1.pop('Name'))
#d_1.pop('Name') # 只能选取key而非value进行删除，且最后删除的为键值对
print(d_1)

#key
print(d_1.get('age')) # 只能从键取值而无法由值取键



