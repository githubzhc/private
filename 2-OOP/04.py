class Student():
    '''
    :return 0
    '''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.setName(name)
    def intrd(self):
        print("我的名字是%s"%(self.name))

    def setName(self,name):
        self.name=name.upper()

s=Student("zs",14)
s.intrd()
print(s.__dict__)
print(s.__doc__)
print(s.__bases__)

class P():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def int(self):
        print("我的名字是：%s，我%d了"%(self.name,self.age))
    def setName(self,name):
        self.name=name.upper()

