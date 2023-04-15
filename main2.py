# this class contain general attributes of animals.
class Animal:
    default_msg = 'this is a default message that shows your created-object is a kind of animal'

    def __init__(self, age, name, color, food):
        self.age = age
        self.name = name
        self.color = color
        self.food = food

    def call_age(self):
        print(f'my age is {self.age}')

    def call_name(self):
        print(f'my name is {self.name}')

    def call_color(self):
        print(f'my color is {self.color}')

    def call_food(self):
        print(f'my food is {self.food}')


class Vertebrate(Animal):
    def __init__(self, age, name, color, food):
        super().__init__(age, name, color, food)
        self.__parentClsName = 'Animal'

    def call_bodystructure(self):
        print('skeleton structure')


class Invertebrate(Animal):
    def __init__(self, age, name, color, food):
        super().__init__(age, name, color, food)
        self.__parentClsName = 'Animal'

    def call_bodystructure(self):
        print('not skeleton structure')


class Worm(Invertebrate):
    _lifetime = 10

    def __init__(self, length, skinType, weight, *args):
        super().__init__(*args)
        self.length = length
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Invertebrate'

    def move(self):
        print('I am crawling')

    def introduction(self):
        print('this is a kind of invertebrate animal names Worm')

    def remained_ages(self):
        print(f'{Worm._lifetime - self.age} years of my life remains')

    def call_length(self):
        print(f'my length is {self.length}')


class Sponge(Invertebrate):
    _lifetime = 65

    def __init__(self, density, skinType, weight, *args):
        super().__init__(*args)
        self.density = density
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Invertebrate'

    def move(self):
        print('I cant move!')

    def introduction(self):
        print('this is a kind of invertebrate animal names sponge')

    def remained_ages(self):
        print(f'{Sponge._lifetime - self.age} years of my life remains')

    def call_density(self):
        print(f'my density is {self.density} gram per milliliter')


class Fish(Vertebrate):
    _lifetime = 8

    def __init__(self, balletNum, skinType, weight, *args):
        super().__init__(*args)
        self.balletNum = balletNum
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Vertebrate'

    def move(self):
        print('I am swimming')

    def introduction(self):
        print('this is a kind of vertebrate animal names fish')

    def remained_ages(self):
        print(f'{Fish._lifetime - self.age} years of my life remains')

    def call_balletnum(self):
        print(f'my ballet number is {self.balletNum}')


class Bird(Vertebrate):
    _lifetime = 4

    def __init__(self, speed, skinType, weight, *args):
        super().__init__(*args)
        self.speed = speed
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Vertebrate'

    def move(self):
        print('I am flying')

    def introduction(self):
        print('this is a kind of vertebrate animal names bird')

    def remained_ages(self):
        print(f'{Bird._lifetime - self.age} years of my life remains')

    def call_speed(self):
        print(f'my speed is {self.speed} meter per minute')


class Reptile(Vertebrate):
    _lifetime = 12

    def __init__(self, livingPlace, skinType, weight, *args):
        super().__init__(*args)
        self.livingPlace = livingPlace
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Vertebrate'

    def move(self):
        print('I am crawling')

    def introduction(self):
        print('this is a kind of vertebrate animal names reptile')

    def remained_ages(self):
        print(f'{Reptile._lifetime - self.age} years of my life remains')

    def call_livingPlace(self):
        print(f'my living place is {self.livingPlace}')


class Amphibian(Vertebrate):
    _lifetime = 18

    def __init__(self, isToxic: bool, skinType, weight, *args):
        super().__init__(*args)
        self.isToxic = isToxic
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Vertebrate'

    def move(self):
        print('I am jumping')

    def introduction(self):
        print('this is a kind of vertebrate animal names amphibian')

    def remained_ages(self):
        print(f'{Amphibian._lifetime - self.age} years of my life remains')

    def Is_toxic(self):
        if self.isToxic is True:
            print('this amphibian is toxic')
        else:
            print('this kind of amphibian is not toxic')


class Mammal(Vertebrate):
    _lifetime = 15

    def __init__(self, childNum, skinType, weight, *args):
        super().__init__(*args)
        self.childNum = childNum
        self.skinType = skinType
        self.weight = weight
        self.__parentClsName = 'Vertebrate'

    def move(self):
        print('I am walking')

    def introduction(self):
        print('this is a kind of vertebrate animal names mammal')

    def remained_ages(self):
        print(f'{Mammal._lifetime - self.age} years of my life remains')

    def call_childnum(self):
        print(f'my child number is {self.childNum}')


############################################################
# goldfish example


goldfish = Fish(10, 'pool', 1.2, 2, 'GoldenBoy', 'red', 'grass')


a = list(goldfish.__dict__)
print(a)
goldfish.call_bodystructure()
goldfish.call_food()
goldfish.call_age()
goldfish.call_color()
goldfish.call_name()
goldfish.call_balletnum()
goldfish.introduction()
goldfish.move()
goldfish.remained_ages()
print(goldfish.default_msg)
print(goldfish.balletNum)
print(goldfish.skinType)
print(goldfish.weight)
##############################################################
# spongebob example

spongebob = Sponge(0.3, 'no skin type', 200, 21, 'spongebob', 'yellow', 'plankton')
spongebob.call_density()
spongebob.remained_ages()
print(spongebob.skinType)
##############################################################


Worm1 = Worm(10, 'no skin', 21, 10, 'bad worm', 'red', 'ant')
a = list(Worm1.__dict__)
print(a)
##############################################################

