#map函数接收两个参数，一个函数，一个是Iterable，map将传入的函数依次作用于序列的每个元素上，把结果当作一个新的Iterator返回
from functools import reduce

def f(x):
    return x*x

r=map(f,[1,2,3,4,5])
print(next(r))
print(next(r))

#返回iterator 延迟计算

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def fn(x,y):
    return x*10+y

f=reduce(fn,[1,2,3,4,5])
print(f)


