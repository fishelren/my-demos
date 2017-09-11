from functools import reduce

# 函数式编程 允许把函数本身作为参数传入另一个函数，还允许将函数作为返回值

'''
print(abs(-10))
print(abs)
f = abs
print(f(-2))
'''

# 变量可以指向函数并当作函数使用
# 函数名是指向函数的变量

# 高阶函数：可以接收函数作为参数的函数

# map 将函数作用与可迭代对象的每一个元素上，并产生一个新的可迭代对象

# eg
'''
myList=[1,2,3,4,5]
def f(x):
    return x*x
print(list(map(f,myList)))
'''

# reduce 将带两个参数的函数作用在可迭代对象上，对可迭代对象作累积计算

# eg
'''
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5]))
'''

# eg
'''
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))
'''

# eg
'''
def fn2(x,y):
    return x*10+y

def char2int(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(fn2,map(char2int,'2468')))
'''

# filter 将函数作用于可迭代对象中的每一个元素，根据返回的布尔值判断是否保留元素，返回新的可迭代对象

# eg
'''
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))
'''

# eg
'''
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['a',' ','b',' c','','d'])))
'''

# eg
'''
# 回数
def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

'''


# 内建函数sorted将可迭代对象中的元素排序后返回一个新的列表，
# 第二个参数key可选，是一个带一个参数的函数，用来将元素进行转换后再比较
# 第三个参数reverse可选，若设为True则将排序后的结果逆序后返回
'''
print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper,reverse=True))

'''

'''
# eg 按名字进行比较
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)
'''

'''
# 按成绩从高到低进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return t[1]

L2 = sorted(L,key=by_score,reverse=True)
print(L2)
'''


