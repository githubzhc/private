class A():
    def __init__(self):
        print("sad")

class B(A):
    def __init__(self):
        print("asd")

class C(B):
    pass

c=C()
print("*"*30)
class A():
    def __init__(self):
        print("sad")

class B(A):
    def __init__(self,name):
        print("asd")
        self.name=name

class C(B):
    pass

c=C()

