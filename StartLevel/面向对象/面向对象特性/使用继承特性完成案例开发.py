


class animal:
    # def __init__(self, eat, drink, poo, pee, sleep):
    #     self.eat = eat
    #     print('吃')
    #     self.drink = drink
    #     print('喝')
    #     self.poo = poo
    #     print('拉')
    #     self.pee = pee
    #     print('撒')
    #     self.sleep = sleep
    #     print('睡')
    # def __repr__(self):
    #     return f'{self.eat} {self.drink} {self.poo} {self.pee} {self.sleep}'
    def eat(self):
        print('吃')
    def drink(self):
        print('喝')
    def poo(self):
        print('拉')
    def pee(self):
        print('撒')
    def sleep(self):
        print('睡')
class dog(animal): # 继承父类‘animal’的所有属性与方法
    # def __init__(self, eat, drink, poo, pee, sleep, bark):
    #     self.eat = eat
    #     print('吃')
    #     self.drink = drink
    #     print('喝')
    #     self.poo = poo
    #     print('拉')
    #     self.pee = pee
    #     print('撒')
    #     self.sleep = sleep
    #     print('睡')
    #     self.bark = bark
    #     print('叫')
    def eat(self):
        print('1吃') # 注意:继承父类后若在'dog'类中继续对eat(self)重新print('1吃'),最后pet1.eat()则输出:1吃
    def drink(self):
        print('2喝')
    def poo(self):
        print('3拉')
    def pee(self):
        print('4撒')
    def sleep(self):
        print('5睡')
    def bark(self):
        print('6叫')

class XiaoTianQuan(dog):
    def fly(self):
        print('🛫')
pet1 = dog()
pet1.eat() # 注意:继承父类后若在'dog'类中继续对eat(self)重新print('1吃'),最后pet1.eat()则输出:1吃
pet1.sleep()
pet1.bark()
pet2 = XiaoTianQuan()
pet2.fly()



