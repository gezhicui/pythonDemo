# 为了保证所有的函数都能够正确使用到全局变量，应该 将全局变量定义在其他函数的上方
a = 10
num = 10

# !!!!!!!111如果想在函数中改变全局变量的值，那么可用 global +变量名
def demo1():

    print("demo1" + "-" * 50)

    # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
    num = 100
    print(num)


def demo2():

    print("demo2" + "-" * 50)
    print(num)

demo1()
demo2()

print("over")

