# !/usr/bin/env python    
# -*-coding:utf-8 -*-

"""
# File       : chapter_09_类.py
# Time       ：2020/10/26 15:34 
# Author     ：Yolanda Yan
# version    ：python 3.6
# Description：
"""

"""9.1"""
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):  # 注意前后都是两个下划线
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# ########## 练习题 ############### #
"""9-1 餐馆"""
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\n餐厅名称: " + self.restaurant_name)
        print("类   型: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " 正在营业！")


restaurant = Restaurant('胡大饭馆', '川菜')
print("餐厅名称: " + restaurant.restaurant_name)
print("类   型: " + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""9-2 在9-1的基础上，创建3个实例"""
restaurant_1 = Restaurant('胡大饭馆', '川菜')
restaurant_2 = Restaurant('很久以前', '烧烤')
restaurant_3 = Restaurant('辣庄', '火锅')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

"""9-3 用户"""
class User():
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight

    def describe_user(self):
        print("first name: " + self.first_name.title())
        print("last name: " + self.last_name.title())
        print("height: " + self.height)
        print("weight: " + self.weight)

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hello！ " + full_name.title())


user = User('tom', 'smith', '185', '140')
user.describe_user()
user.greet_user()

user = User('lily', 'nancy', '165', '94')
user.describe_user()
user.greet_user()
# ############################### #

"""9 car类"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 制造商
        self.model = model  # 型号
        self.year = year  # 生成年份
        self.odometer_reading = 0  # 初始化汽车的里程表为0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it!")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值
           禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage

    def fill_gas_tank():
        pass


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23)  # 通过方法修改属性值
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)  # 创建一辆二手车
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)  # 这辆二手车的里程表读数设置为23500
my_used_car.read_odometer()

my_used_car.increment_odometer(100)  # 从购买到登记期间行驶的100英里
my_used_car.read_odometer()


# ########## 练习题 ############### #
"""9-4 就餐人数"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\n餐厅名称: " + self.restaurant_name)
        print("类   型: " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " 正在营业！")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, inc_num):
        self.number_served += inc_num

    def read_number_served(self):
        print("This restaurant has " + str(self.number_served) + "人就餐")


restaurant = Restaurant('胡大饭馆', '川菜')
print("餐厅名称: " + restaurant.restaurant_name)
print("类   型: " + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.read_number_served()

restaurant.set_number_served(30)
restaurant.read_number_served()

restaurant.increment_number_served(100)
restaurant.read_number_served()
# ############################### #


"""9.3 继承  
       电动汽车
       super()是一个特殊函数，帮助Python将父类和子类关联起来。
       """


class ElectricCar(Car):
    """电动汽车的独特之处
       初始化父类的属性，再初始化电动汽车特有的属性"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):  # 重写父类的方法
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

"""9.3.5 将实例用作属性"""


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            get_range = 240
        elif self.battery_size == 85:
            get_range = 270
        message = "This car can go approximately " + str(get_range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """修改电瓶容量"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

"""9.5 python标准库"""
from collections import OrderedDict  # 记录你添加键—值对的顺序

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# ########## 练习题 ############### #
"""9-14 骰子"""


class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        from random import randint
        for i in range(10):
            x = randint(1, self.sides)
            print(str(self.sides) + "面第 " + str(i) + "次：" + str(x))


die = Die(6)  # 6面骰子
die.roll_die()

die_10 = Die(10)  # 10面骰子
die_10.roll_die()

die_20 = Die(20)  # 20面骰子
die_20.roll_die()
# ############################### #