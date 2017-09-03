# python中一边循环一边推算的机制称为生成器

# eg
'''
g=(x*x for x in range(1,10)) # 如果为[]包围，则是列表推导式
# 调用next方法从可迭代对象中取下一个元素，当取尽且没有指定默认值的时候会抛出StopIteration异常
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # 抛出异常

# 一般都不会用next方法来迭代生成器中的元素
'''

# eg
'''
# 通常使用for循环来迭代生成器generator中的元素
g=(x*x for x in range(1,10))
for y in g:
    print(y)
'''

# eg
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    print("done")

fib(6)
'''

# eg
# 当函数中有关键字yield，它就不是普通的函数，而是一个生成器
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
g=fib(6) # 创建生成器对象
for y in g:
    print(y)
'''

# eg
'''
# 单次调用generator，都是遇到yield作为终止的
def p():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3

g_p=p()
print(next(g_p))
# step 1
# 1
print(next(g_p))
# step 2
# 2
print(next(g_p))
# step 3
# 3
'''

# 杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
        L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]

n=0
for L in triangles():
    n=n+1
    print(L)
    if n==10:
        break

# 可以把列表推导式改成生成器，也可以将函数改成生成器