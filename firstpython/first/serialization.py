import pickle
import json
d=dict(name="Bob",age=20,score=88)
str=pickle.dumps(d)
print(str)

f=open("E:/a.txt","wb")
pickle.dump(d,f)

f.close()
#dump函数直接将对象序列化后写入文件
r=open("E:/a.txt","rb")
d=pickle.load(r)
r.close()
print(d)


first_dict=dict(name="zhu",age="20",score="88")
str_json=json.dumps(first_dict)

print(str_json)


print(json.loads(str_json))


class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        
s=Student("zhu",20,88)

def student_dict_dump(std):
    return {"name":std.name,"age":std.age,"score":std.score}
json_str=json.dumps(s,default=student_dict_dump)

print(json_str)

def student_dict_load(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(json_str,object_hook=student_dict_load))
