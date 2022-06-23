
# 调用静态方法时无需像调用普通方法那样对当前类实例化而可直接使用类名.方法进行调用

# 静态方法传入参数均是普通参数而类方法参数第一位必须是cls
# 静态方法不与当前类绑定可看作一个单独的函数，类方法则与当前类绑定

class triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    # 装饰器
    @staticmethod
    def p2(d, e, f):
        '''判断三条边是否构成三角形(静态方法)'''
        if d + e > f and e + f > d and f + d > e:
            print(f'三角形周长 = {d + e + f}')
            p = d + e + f / 2
            print(f'三角形面积 = {(p * (p - d) * (p - e) * (p - f)) ** 0.5}')
        else:
            print('False')
    # def perimeter(self):
    #     '''计算周长'''
    #     return self.a + self.b + self.c
    #     print(f'三角形周长 = {self.a + self.b + self.c}')

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     '''判断三条边是否构成三角形(类方法)'''
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        '''计算周长'''
        return self.a + self.b + self.c


    def area(self):
        '''计算面积'''
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# 调用普通方法计算三角形边长和面积
tri1 = triangle(3, 4, 5)
print(tri1.perimeter())
print(tri1.area())

# 通过调用静态方法判断是否为三角形(是则计算其周长,不是则返回False)
triangle.p2(5, 6, 2) # 调用静态方法时,无需对当前类进行实例化,可直接使用类名.方法


