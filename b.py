class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class AnimalFactory:
    def create_animal(self, animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            return None





class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()


class AbstractProductA:
    pass


class AbstractProductB:
    pass


class ProductA1(AbstractProductA):
    pass


class ProductA2(AbstractProductA):
    pass


class ProductB1(AbstractProductB):
    pass


class ProductB2(AbstractProductB):
    pass





class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_wheels()
        self._builder.add_engine()
        self._builder.add_body()

    def get_car(self):
        return self._builder.car


class Builder:
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class CarBuilder(Builder):
    def add_wheels(self):
        self.car.wheels = 4

    def add_engine(self):
        self.car.engine = "V8"

    def add_body(self):
        self.car.body = "Sedan"


class Car:
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.body = None


