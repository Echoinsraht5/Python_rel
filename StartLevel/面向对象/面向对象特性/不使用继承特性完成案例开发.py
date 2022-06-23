# 类中的方法通常被单独定义,如 class cat:
                                # def catch(self)
# 之后调用方法时只需创建对象 pet_1 = cat()
#                         pet_1.catch()即可
# 类中的属性采取初始化函数定义,如 class student:
                                   # def __init__(self, name, gender, age, height, weight)
# 之后调用属性时需创建对象 stu_1 = student('小天', '男', 18, 178, 75)
#                        print(stu_1.name, stu_1.gender, stu_1.age)
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
class dog:
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

pet1 = animal()
pet1.eat()
pet1.sleep()



