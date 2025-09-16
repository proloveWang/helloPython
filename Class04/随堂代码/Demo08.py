"""
解释：如果在一个函数的内部定义了另一个函数，外部的我们叫他外函数，内部的我们叫他内函数。
闭包：在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。
"""


def outer():
    a = 10

    def inner():
        print("我是内函数")
        return a + 10

    return inner


fn = outer()
# 内函数的地址
print(fn)
# 外函数的地址
print(outer)
# 调用了一下内函数
result = fn()
print(result)

# 在闭包中外函数把临时变量绑定给内函数
"""
一个函数结束的时候，会把自己的临时变量都释放还给内存，之后变量都不存在了。一般情况下，确实是这样的。但是<font color=red>闭包是一个特别的情况。外部函数发现，自己的临时变量会在将来的内部函数中用到，自己在结束的时候，返回内函数的同时，会把外函数的临时变量送给内函数绑定在一起。</font>所以外函数已经结束了，调用内函数的时候仍然能够使用外函数的临时变量。
"""


def outer2(num):
    a = num

    def inner():
        print("我是内函数")
        return a + 10

    return inner


fn1 = outer2(10)
fn2 = outer2(20)
print(fn1)
print(fn2)

print(fn1())
print(fn2())


def outer3(num):
    a = num

    def inner():
        print("我是内函数")
        # 假如在内函数中，需要修改外函数的全局变量，需要添加关键字 nonlocal,如果不添加也不报错 ，只是此 a 非彼 a
        nonlocal a
        a = a + 10
        return a

    return inner


fn3 = outer3(10)
# 闭包变量实际上只有一份，每次调用一份闭包变量
print(fn3())  # a = 20
print(fn3())  # a = 30
print(fn3())  # a = 40

# fn4 = outer3(20)
# print(fn4())