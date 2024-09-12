class StrTools:
    pass


s1 = StrTools()
s2 = StrTools()
print(s1) # <__main__.StrTools object at 0x0000020B4A094D48>
print(s2) # <__main__.StrTools object at 0x0000020B4A09C248>

"""
单例模式就是对一个类, 只获取它唯一的类对象, 持续复用它(地址相同)
"""