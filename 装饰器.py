# 装饰器也是一种闭包
# 不破坏函数原有的代码和功能下, 为函数增加新功能

"""
在调用sleep()前后输出"我要睡觉了", "起床了"
"""
# def sleep():
#     import random
#     import time
#     print("睡眠中")
#     time.sleep(random.randint(1, 5))

# print("我要睡觉了")
# sleep()
# print("我起床了")

# 以上方法太普遍, 使用装饰器
"""装饰器的一般写法(闭包), 不破坏原有代码的情况下新增功能"""
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我起床了")
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中")
#     time.sleep(random.randint(1, 5))
# fn = outer(sleep)
# fn()

"""装饰此快捷写法"""

def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

# 装饰器
@outer
def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint(1, 5))

sleep()

"""
装饰器是创建一个闭包函数, 在闭包函数内部调用目标函数
在目标函数前 @闭包函数 , 增加额外功能
"""