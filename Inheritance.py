# Single Inheritance
# In Single inheritance it consists only one class
class A():
    def method1(self):
        print("Class A is Single inheritance")


Obj1 = A()
Obj1.method1()


# Single Inheritance
class B():
    def method2(self):
        print("Class B is Single inheritance")


Obj2 = B()
Obj2.method2()


# Multi Inheritance
# In Multi inheritance it derives from two classes
class F(A):
    def method3(self):
        print("Class F is Multi inheritance")


Obj3 = F()
Obj3.method3()


# Single Inheritance
class C():
    def method4(self):
        print("Class C is Single inheritance")


Obj4 = C()
Obj4.method4()


# Single Inheritance
class D():
    def method5(self):
        print("Class D is Single inheritance")


Obj5 = D()
Obj5.method5()


# Multiple Inheritance
# In Multiple inheritance it derives from Three classes
class E(C, D):
    def method6(self):
        print("Class E is Multiple inheritance")


Obj6 = E()
Obj6.method6()
