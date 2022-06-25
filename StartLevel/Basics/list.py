
a = 'ekko'
list_1 = [a, 'b', 3 <= 4, 'b']
print(type(list_1))
for i in list_1: # 循环遍历列表所有元素
    print(i)
print(list_1[0])



#add
list_1.insert(1, 'c') #列表指定索引增加数据
print(list_1)
    #print(list_1.insert(1, 'c')) 增加类指令不可直接放入print()

list_1.append('qwer') # 列表末尾增加数据
print(list_1)



#modify
list_1[0] = 'a'
print(list_1)



#delete
# del list_1[0] #删除列表指定索引数据
# print(list_1)

# list_1.pop(0) #删除列表指定索引数据
    # print(list_1.pop(0)) 删除类指令可直接放入print()
# print(list_1)

# list_1.pop() #删除列表末尾数据
# print(list_1)

# list_1.clear() #清空列表
# print(list_1)



#calculate
len(list_1)
print(len(list_1)) #统计列表长度（从1计数）统计类指令可直接放入print()
print(list_1.count('b')) #统计列表元素出现次数（从1计数）

#sort
list_2 = [9, 3, 6, 12, 234624, 4364, 34763]
list_2.sort()
print(list_2)
list_2.sort(reverse=True)
print(list_2)
list_2.reverse()
print(list_2)

list_3 = [1]
print(list_3)
print(type(list_3))
list_3 = [1,]
print(list_3)
print(type(list_3))

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[-4:] # areas[-4:] == areas[6:10] 使用slicing时列表索引由[0或[:开始，:]结束

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)