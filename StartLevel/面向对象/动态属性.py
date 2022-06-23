

class student:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def __repr__(self):
        return f'{self.name} {self.age}'

stu1 = student('小泽', 22)
print(stu1)

# 动态添加gender属性
stu1.gender = '男'
print(stu1.gender)