# 闭包: 解决全局变量不被修改
'''
内部函数依赖外部变量
'''
def outer1(logo):

    def inner1(msg): # 内部函数: 闭包函数
        print(f"<{logo}><{msg}><{logo}>")

    return inner1

f1 = outer1("lc")
# f1("python")

# 使用nonlocal关键字修改外部函数的值

def outer2(num1):

    def inner2(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner2

fn = outer2(10)
# fn(20)
# fn(20)

# 闭包实现ATM
def account_add(account_amonut=0):

    def atm(num, desposit=True):
        nonlocal account_amonut
        if desposit:
            account_amonut += num
            print(f"存款{num}, 余额为{account_amonut}")
        else:
            account_amonut -=num
            print(f"取款{num}, 余额为{account_amonut}")

    return atm

# 初始余额
account_num = account_add(1500)
account_num(500, False)
account_num(800, False)
account_num(1500)


"""
闭包: 定义双层嵌套函数, 内部函数可以访问外部函数的变量
     将内层函数作为外层函数的返回, 此内层函数就是闭包函数
关键字: nonlocal, 声明可以修改外部函数的值
优点: 
    1. 无需定义全局变量即可通过函数持续的引用和修改值
    2. 闭包使用的变量在函数内部, 难以被调用修改
缺点: 
    1. 由于内部函数持续引用外部函数的值, 导致一部分内存空间不被释放, 占用内存
"""