

class A:
    def __init__(self):
        # 公用属性
        self.num1 = 100
        # 私有属性
        self.__num2 = 200
    # 私有方法
    def __test(self):
        print(f'共有属性与私有属性的值: {self.num1}, {self.__num2}')
    # 公有方法
    def test(self):
        # print(f'父类中公有方法输出私有属性的值: {self.__num2}')
        # 在共有方法中调用私有方法
        self.__test()

class B(A):
    def demo(self):
        # pass # 占位符表示结束
        super().test()

b = B()
print(b.num1)
print(b._A__num2) # 继承后无法直接访问父类中的私有属性,可通过修改名称或调用父类中公用方法来输出私有属性
b.demo() # 同样无法直接调用父类中的私有方法,但可通过先调用父类中公有方法再间接调用其私有方法的方式实现