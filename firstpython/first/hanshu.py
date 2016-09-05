
#默认参数

def first(x=2):
    return  print(x*x)

first(1)
first()
#可变参数

def second_1(numbers):
    for part in numbers:
        print(part)
    return

second_1([1,2,3])

def second_2(*numbers):
    for part in numbers:
        print(part)
    return

a=[1,2,3]

second_2(1,2,3)
second_2(*a)


#关键字参数

def third_1(name,gende,**others):
    if 'home'  in others:
        print("有home为%s"%others['home'])
    else:
        pass
    return

third_1("朱迅","男",  home="邹城",father='hello')

def third_2(name,gender,*,home,father="hello",mather="hi"):
    print(father)
    print(mather)
    print(home)
    print(mather)
    return

third_2("朱迅", "男",home="邹城")