# 修剪、替换、拆分/合并

str_1 = 'love faye'
print(str_1[2:8]) # 左开右闭区间
print(str_1.capitalize()) # 首单词首字母大写
print(str_1.title()) # 所有单词首字母大写
print(str_1.upper()) # 所有单词所有字母大写

x = 'tik tok'
print(x.find('tok'))
y = 'hello, world'
print(y.find('or'))
print(x.find('t')) # 元素第一次出现位置
print(x.rfind('t')) # 元素最后一次出现位置
print(x.find('t', 3)) # 元素在指定索引出现位置

r = 'cowboy bebop 123 123'
print(r.isdigit())
print(r.isalpha())
print(r.isalnum())
print(r)

# 替换
print(r.replace('boy', 'girl'))
print(r.replace('123', '456', 1))

# 拆分合并
s = r.split(' ', 2)
print(s)
print('@'.join(s))


