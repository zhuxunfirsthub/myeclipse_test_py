L=[1,2,3,4,5]
print(L[1:len(L)-1])

print(L[0::2])

#String也可以看成是一种list，每个元素当作一个字符，也可以进行切片

print("asdfgh"[0::2])

list_1=[1,2,3,4,5]
tuple_1=(1,2,3,4,5)
dict_1={'a':1,'b':2,'c':3,'d':4,'e':5}

for key in list_1:
    print(key)
    
for key in tuple_1:
    print(key)

for key in dict_1:
    print(key)
    
for key in dict_1.values():
    print(key)
    
for key in dict_1.items():
    print(key[0])
    
    
#列表生成式
a=[x*x for x in range(1,11)if x%2==0]
print(a)

b=[m+n for m in range(1,11) for n in range(1,11) if n%3==0 if m%4==0 ]
print(b)
