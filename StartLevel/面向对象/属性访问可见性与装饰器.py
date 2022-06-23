
# __name表示一个私有属性，不可直接访问与修改
# _name表示一个受保护属性，可直接访问与修改

class student:
    def __init__(self, name, age) : # 添加‘姓名’‘年龄’属性
        self.__name = name
        self._age = age

    # 装饰器获取私有属性
    # @property
    # def name(self):
    #     return self.__name
    # # 修改私有属性
    # @name.setter
    # def name(self, name):
    #     self.__name = name or '无名氏'
    #
    # @property
    # def age(self):
    #     return self.__age
    # @age.setter
    # def age(self, age):
    #     self.__age = age

stu1 = student('小明', 18)
stu1._age = 12
# print(stu1._age, stu1._student__name)
stu1.__name = '小明'
print(stu1.__name)
# print(stu1._student__name) # 可通过修改名称方式绕开限制从而访问__name私有属性


