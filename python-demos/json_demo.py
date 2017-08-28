import json
import importlib
'''
#  1.基本类型
data=[{'a':"A",'b':(2,4),'c':3.0}]

print("data="+repr(data))  # data=[{'a': 'A', 'b': (2, 4), 'c': 3.0}]
dataJson=json.dumps(data)
print("dataJson="+dataJson)  # data=[{"a": "A", "b": [2, 4], "c": 3.0}]
print("type(dataJson)="+repr(type(dataJson)))  # type(dataJson)=<class 'str'>

newData=json.loads(dataJson)
print("newData="+repr(newData))  # newData=[{'a': 'A', 'b': [2, 4], 'c': 3.0}]
print("type(newData)="+repr(type(newData)))  # type(newData)=<class 'list'>
print("newData[0]['a']="+newData[0]['a'])  # newData[0]['a']=A
'''

'''
str和repr函数相似，都是返回字符串表现形式；str返回易于阅读的形式，repr返回易于解释器处理的形式；
repr返回的字符串可以通过eval函数转换为原对象，repr返回的字符串可能包含引号和反斜杠
'''

'''
#  2.额外参数
data=[{'a':"A",'b':(2,4),'c':3.0,'d':"D",'e':"E",'f':"F",'g':"G",'h':"H"}]
# print(json.dumps(data))
print(json.dumps(data,sort_keys=True,indent=4,separators=(',',':')))
'''

'''
json.dumps函数中sort_keys指定字典按键排序；indent指定缩进；
separators=(item_separator, key_separator)去除分隔符后的空格；
skipkeys为True，则字典的键不是基本类型（str, int, float, bool, None）时会被跳过，
而不是抛出异常
'''
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Jack", 22)
'''
#  3.自定义类型的编码与解码
def convert_to_builtin_type(obj):
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__
    }
    d.update(obj.__dict__)
    # dict.update 用其它字典或可迭代的键值对来升级当前字典，重写已经存在的键
    # object.__dict__ 用于存储对象属性的字典
    return d

print(json.dumps(p, default=convert_to_builtin_type))
# default 用于指定将自定义类型转换为可以序列化为JSON字符串的Python内置类型的函数

def dict_to_object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')  # dict.pop 删除键并返回对应的值
        module_name = d.pop('__module__')
        module = importlib.import_module(module_name)  # 导入一个模块
        class_ = getattr(module, class_name)
        obj = class_(**d)
    else:
        obj = d
    return obj

encoded_object = '{"__class__": "Person", "__module__": "__main__", "name": "Jack", "age": 22}'
newObj=json.loads(encoded_object, object_hook=dict_to_object)
print(type(newObj))
'''

'''
# JSONEncoder.iterencode方法将对象的各个部分分别进行编码
encoder=json.JSONEncoder()
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
for part in encoder.iterencode(data):
    print('PART:'+part)
'''
'''
PART:[
PART:{
PART:"a"
PART:: 
PART:"A"
PART:, 
PART:"b"
PART:: 
PART:[2
PART:, 4
PART:]
PART:, 
PART:"c"
PART:: 
PART:3.0
PART:}
PART:]
'''

class MyEncoder(json.JSONEncoder): # 自定义编码器
    def default(self, obj):
        d = {
            '__class__': obj.__class__.__name__,
            '__module__': obj.__module__
        }
        d.update(obj.__dict__)
        # dict.update 用其它字典或可迭代的键值对来升级当前字典，重写已经存在的键
        # object.__dict__ 用于存储对象属性的字典
        return d

result=json.dumps(p,cls=MyEncoder)
print(result)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=self.dict_to_object)

    def dict_to_object(self,d):
        if '__class__' in d:
            class_name = d.pop('__class__')  # dict.pop 删除键并返回对应的值
            module_name = d.pop('__module__')
            module = importlib.import_module(module_name)  # 导入一个模块
            class_ = getattr(module, class_name)
            obj = class_(**d)
        else:
            obj = d
        return obj
t='{"__class__": "Person", "__module__": "__main__", "name": "Jack", "age": 22}'
r=MyDecoder().decode(t)
print(r)