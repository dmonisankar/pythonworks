# Method Resolution order



class A:
    def __init__(self):
        super().__init__()
        self.name = 'John'
        self.age = 23

    def getName(self):
        return self.name


class B:
    def __init__(self):
        super().__init__()
        self.name = 'Richard'
        self.id = '32'

    def getName(self):
        return self.name


class C(A, B):
    def __init__(self):
        super().__init__()

    def getName(self):
        return self.name

C1 = C()
print(C1.getName())
print(C.__mro__)

# MRO works in a depth first left to right way. super() in the __init__ method indicates the class that is in the next hierarchy. At first the the super() of C indicates A. Then super in the constructor of A searches for its superclass. If it doesn’t find any, it executes the rest of the code and returns. So the order in which constructors are called here is: C -> A -> B
