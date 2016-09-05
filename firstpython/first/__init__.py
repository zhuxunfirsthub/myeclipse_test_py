from _ast import List
print('hello python')
a=100
if a>20:
    print(a)
else:
    print(200)
    
print("I'm ok")

print(ord('中'))

print(chr(66))

print(len("中文".encode(encoding='utf_8', errors='strict')))

print("hello %s"%("world"))
#list是一种有序的集合，可以随时添加和删除其中的元素

list_colors=['red','green','yello']
print(len(list_colors))

list_colors.append('black')
print(len(list_colors))
list_colors.pop()
print(list_colors)
list_colors.pop(-1)
print(list_colors)
print(len(list_colors))

s=['first','second','third']
p=['1','2',s]
print(p)
print(p[2][2])

#tuple的内容无法改变，但可以改变其中嵌套list的值

tuple_1=(1,2,3,s)
print(tuple_1)

s.pop()

print(tuple_1)
'''
birthyear=input("请输入出生年份")

if int(birthyear)>2000:
    print("00后")
'''
for color in list_colors:
    print(color)

n=1

while n<100:
    n=n+1
    print(n)
    
 #python中的键值对dict，实际上是两个list
 
scores={'zhangsan':70,'lisi':80,'wanger':90}
print(scores['zhangsan'])

print(scores.get('zhuxun','no'))

#键值对中的键必须是不可变对象，比如常数，字符串









