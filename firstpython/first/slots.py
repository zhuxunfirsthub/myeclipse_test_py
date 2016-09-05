from types import MethodType
class Student(object):
    pass

s=Student()
s.name="Michael"
print(s.name)

def set_age(self,age):
    self.age=age
    print(self.age)
s.set_age= MethodType(set_age, s)
s.set_age(30)


def set_score(self,score):
    self.score=score
    print(self.score)

Student.set_score=set_score

s.set_score(20)

#可以随时给类或者实例设置属性和方法，给类设置的方法。对其所有属性均有效，对单个
#属性设置的属性和方法，仅对当前实例有效

#使用__slots__限制类和其属性任意添加属性和方法，但该类的子类仍然可以添加

class Student_2(object):
    __slots__=('1','2','3')
    

