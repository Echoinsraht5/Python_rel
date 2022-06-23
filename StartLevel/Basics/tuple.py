#元组性质、用法与列表类似，区别在于不可进行修改/增加/删除操作类指令
t_1 = (1)
print(t_1)
print(type(t_1))
t_1 = (1,)
print(t_1)
print(type(t_1))

p = 'naiad'
t_2 = (1, 3, 5, 14, 2, 'nono', p, 5, 5)
print(t_2.index('nono')) # 定位元素索引
print(t_2.count(5)) # 统计元素出现次数

a = int(input('输入：'))
print(type(a))

type(list(t_2))
print(type(t_2))
print(type(list(t_2))) # 元组转列表
