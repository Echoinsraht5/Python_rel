

class A:
    def test(self):
        print('A --- test')
    def demo(self):
        print('A --- demo')

class B:
    def test(self):
        print('B --- test')
    def demo(self):
        print('B --- demo')

class C(A, B): # 类C继承(类A类B)的所有属性与方法
    pass

print(C.__mro__) # 查询类C的属性,方法的调用路径
c = C()
c.test()
c.demo()
