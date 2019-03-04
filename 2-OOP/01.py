
class Person():
    name="ly"
    age=18

    def __init__(self):

        self.name="zs"
        self.age=18
    def do(self):
        #print("%s是%d岁"%(self.name,self.age))
        print(self.name)
p=Person()
p.do()
Person.do(p)
Person.do(Person)

