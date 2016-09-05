g = (x * x for x in range(10))
print( next(g))
print( next(g))

for index in g:
    print(index)
    
#带有yield的函数也是generator

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))


#凡是可作用于for循环的对象都是Iterable类型；list、dict、str

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；



