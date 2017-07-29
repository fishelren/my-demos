"""
所谓“装饰器”，就是在程序运行期间，在不修改函数定义的情况下，
动态增加函数功能的，返回函数的高阶函数
"""
import functools


# 1.不带参数的装饰器
# 装饰器要放在被增强函数的前面，否则就相当于未定义先使用
def log(func):
    @functools.wraps(func) # 将原函数的属性传递给装饰器返回的函数
    def wrapper(*args,**kwargs):
        print("不带参数的装饰器 start")
        func(*args,**kwargs)
        print("不带参数的装饰器 end")
    return wrapper

# 用装饰器log对hello进行增强
@log
def hello():
    print("hello world")

# [decorated]hello() => log(hello) => wrapper() => [real]hello()
hello()



print("===================华丽分割线===================")



"""
当装饰器带参数，装饰器应返回的还是一个装饰器，外层装饰器用来接收参数，内层
装饰器用来返回函数
"""
# 2.带参数的装饰器
def log2(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print("带参数的装饰器 start")
            print("%s;%s"%(text,func(*args,**kwargs)))
            print("带参数的装饰器 end")
        return wrapper
    return decorator

@log2("this is a param")
def hello2():
    return "good good study,day day up"

hello2()
# [decorated]hello2() => log2("this is a param")(hello2) =>
# decorator(hello2) => wrapper() =>[real]hello2()



print("===================华丽分割线===================")



# 3.同时支持带参数和不带参数的装饰器
def log3(params):
    if hasattr(params,"__call__"): # 装饰器不带参数，直接传入函数
        def wrapper(*args,**kwargs):
            print("同时支持带参数和不带参数的装饰器 start")
            params(*args,**kwargs)
            print("同时支持带参数和不带参数的装饰器 end")
        return wrapper
    else: # 装饰器带参数，外层装饰器接收装饰器参数，内层装饰器接收待增强函数
        def wrapper1(func):
            @functools.wraps(func)
            def wrapper2(*args, **kwargs):
                print("同时支持带参数和不带参数的装饰器 start")
                print("%s;%s" % (params, func(*args,**kwargs)))
                print("同时支持带参数和不带参数的装饰器 end")
            return wrapper2
        return wrapper1


@log3
def hello3():
    print("hello decorator")
# [decorated]hello3 => log3(hello3) => wrapper() => [real]hello3

@log3("execute")
def hello4():
    return "hello decorator"
# [decorated]hello4 => log3("execute")(hello4) => wrapper1(hello4)
# => wrapper2() => [real]hello4


hello3()
print("===================华丽分割线===================")
hello4()






