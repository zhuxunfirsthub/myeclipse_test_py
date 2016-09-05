from _io import StringIO, BytesIO
f=open('E:/a.txt','r')
for line in f.readlines():
    print(line.strip())
f.close()
#readline 和 readlines 

#像open()函数返回的这种有个read()方法的对象，
#在Python中统称为file-like Object

with open('E:/a.txt','w') as f:
    f.write("en")
    
    
    
f=StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print(f.getvalue())


b=BytesIO()
b.write("中文".encode(encoding='utf_8', errors='strict'))
str=b.getvalue()
print(str)

 
 