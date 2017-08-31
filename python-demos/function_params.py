#  位置参数

#  默认参数

'''

def add_end(L=[]):
    L.append("END")
    return L

print(add_end())  # ['END']
print(add_end())  # ['END', 'END']
print(add_end())  # ['END', 'END', 'END']

#  默认参数在定义函数的时候就已经计算好了

#  默认参数必须指向不变对象，不然会有问题

def add_end_2(L=None):
    if L is None:
        L=[]
    L.append("END")
    return L

print(add_end_2())  # ['END']
print(add_end_2())  # ['END']
print(add_end_2())  # ['END']

'''

#  可变参数  可以接收任意长度的参数序列 将参数序列在内部组装成tuple

'''
def calc(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


print(calc())  # 0
print(calc(1, 2, 3))  # 6

alist = [2, 3, 4, 5]
#  用星号将list或tuple解析为参数序列，然后传递给可变参数
print(calc(*alist))  # 14

'''

# 关键字参数  接收任意个指定参数名的参数序列 在内部组装成dict

'''

def receive_params(name, age, **kw):
    print("name=" + name)
    print("age=" + str(age))
    print("**kw=" + repr(kw))


receive_params("Jack", 18, hobby='running', job='cooker')
# name=Jack
# age=18
# **kw={'hobby': 'running', 'job': 'cooker'}

param_dict = {'hobby': 'running', 'job': 'cooker'}
# 可以用两个星号将dict解析为指定参数名的参数序列，传递给关键字参数
receive_params("Rose",22,**param_dict)
# name=Rose
# age=22
# **kw={'hobby': 'running', 'job': 'cooker'}
# 内部封装得到的dict和实参dict没有关系

'''

'''
# 命名关键字参数 限定传入关键字参数的名称
def name_kw(name, age, *, job, address):  # 传且仅传job和address两个关键字参数
    print(name)
    print(str(age))
    print(job)
    print(address)

name_kw("Jack", 22, job='dancer', address='Chengdu')

# 可变参数后的命名关键字参数不需要指定特殊的星号分隔符
def name_kw2(param1,param2,*param3,param4,param5):
    print(param1)
    print(param2)
    print(param3)
    print(param4)
    print(param5)
name_kw2("one","two","three","four",param4="five",param5="six")

'''


# 五种参数类型：必选参数，默认参数，可变参数，关键字参数，命名关键字参数
# 定义顺序必须是：必选参数，默认参数，可变参数，命名关键字参数，关键字参数

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
# 使用*args和**kw是Python的习惯写法
