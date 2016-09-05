#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
    return n%2==1


f=filter(is_odd,[1,2,3,4,5])

print(next(f))
print(next(f))

l=list(filter(is_odd,[1,2,3,4,5]))
#list()函数将tuple转换成list
print(l)