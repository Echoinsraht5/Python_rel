


class animal:
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
    def bark(self):
        print('叫')

class dog(animal):
    def eat(self):
        print('1吃')
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
    def bark(self):
        print('猛叫')
        #super().bark() # 子类中当前方法调用父类方法
        animal.bark(self) # 调用父类方法的第二种方式

class cat():
    def catch(self):
        print('抓老鼠')

pet1 = dog()
pet1.eat()
pet1.sleep()
pet1.bark()

pet2 = XiaoTianQuan()
pet2.bark()
pet2.fly()
# pet2.catch() # 因为XiaoTianQuan并未继承cat这个类,故无法调用cat中的catch行为



