class Person:
    pass


class Wordker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


# 定义工厂类完成工厂模式
class Person_Factory:
    def get_person(self, p_type):
        if p_type == "w":
            return Wordker()
        elif p_type == "s":
            return Student()
        elif p_type == "t":
            return Teacher()


fn = Person_Factory()
worker = fn.get_person("w")
student = fn.get_person("s")
teacher = fn.get_person("t")

"""
将对象的创建由使用原始的创建方式改为由特定工厂方法创建
优点: 
    1. 大量创建对象有着统一的入口, 易于代码维护
    2. 当类发生修改时, 仅需修改工厂类的创建方法即可
    3. 符合现实世界的模式, 由工厂创建产品
"""
