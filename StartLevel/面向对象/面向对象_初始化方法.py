
# 初始化方法添加属性__init__

class student:
    def __init__(self, name, age) : # 添加‘姓名’‘年龄’属性
        self.name = name
        self.age = age

    def study(self, courese_name): # 添加‘学习’行为
        # 属性使用self进行调用 参数直接调用
        print(f'{self.name}正在学习{courese_name}')
    def play(self, game_name): # 添加‘玩耍’行为
        #print(f'{self.name}正在玩{game_name}')
        print('%s正在玩%s' % (self.name, game_name))
    def __repr__(self):
        return f'{self.name}: {self.age}'

# 实例化
stu1 = student('小明', 17)
print(stu1)
stu1.study('数控机床的维修与保护')
stu1.play('茶杯头')







