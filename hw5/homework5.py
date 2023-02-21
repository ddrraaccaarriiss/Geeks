class Class1:

    def __init__(self, name):
        self.name = name

class Class2:

    def __init__(self, age):
        self.age = age

class Class3:
    def hello(self):
        print('Hello i am Class3')

class Class4:
      def goodbay(self):
        print('goodbay i am Class4')


class Class5(Class1,Class2,Class3,Class4):
    def __init__(self,name,age):
        Class1.__init__(self,name)
        Class2.__init__(self,age)

    def class5(self):
        print('Ooo i am Class5')


class5 = Class5("Azat",12)
print(class5.name,class5.age)
class5.hello()
class5.goodbay()
class5.class5()













