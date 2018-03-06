class Animal:

    def run(self,chen):
        raise AttributeError('子类必须实现这个方法')



class People(Animal):
    def run(self):
        print('人正在走')


class Pig(Animal):
    def run(self):
        print('pig is walking')


class Dog(Animal):
    def run(self):
        print('dog is running')


peo1 = People()
pig1 = Pig()
d1 = Dog()

peo1.run()
pig1.run()
d1.run()