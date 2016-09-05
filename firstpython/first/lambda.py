#关键字lambda表示匿名函数，冒号前的x表示函数参数
#匿名函数只能有一个表达式，不用return，返回值是表达式的结果
def build(x,y):
    return lambda:x*x+y*y
