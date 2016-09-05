#class后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
#通过定义一个特殊的__init__方法，在创建实例的时候，把属性绑上去
#__init__方法的第一个参数永远是self，表示创建的实例本身
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数


class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print(self.score)
        
stu=Student("zhuxun","100")
stu.print_score()


#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
#就变成了一个私有变量（private），只有内部可以访问



class Animal(object):
    name="Animal"
    def run(self):
        print("animal")
        
class Dog(Animal):
    def run(self):
        print("dog")
        
dog=Dog()
dog.run()
print(dog.name)





