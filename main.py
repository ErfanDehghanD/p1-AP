##############################################################
# General info
# Advanced programming => problem 1
# coded by: Erfan Dehghan, 400103346


##############################################################
# this part contain animal classes.
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
        self._parentClsName = 'Animal'
        self._ClsName = 'Vertebrate'

    def call_bodystructure(self):
        print('skeleton structure')

    def help(self):
        print(Guide.guide(self))


class Invertebrate(Animal):

    def __init__(self, age, name, color, food):
        super().__init__(age, name, color, food)
        self._parentClsName = 'Animal'
        self._ClsName = 'Invertebrate'

    def call_bodystructure(self):
        print('not skeleton structure')

    def help(self):
        print(Guide.guide(self))


class Worm(Invertebrate):
    _lifetime = 10

    def __init__(self, length, skinType, weight, *args):
        super().__init__(*args)
        self.length = length
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Invertebrate'
        self._ClsName = 'Worm'

    def move(self):
        print('I am crawling')

    def introduction(self):
        print('this is a kind of invertebrate animal names Worm')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Worm._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')
    def call_length(self):
        print(f'my length is {self.length}')

    def help(self):
        print(Guide.subclass(self))


class Sponge(Invertebrate):
    _lifetime = 65

    def __init__(self, density, skinType, weight, *args):
        super().__init__(*args)
        self.density = density
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Invertebrate'
        self._ClsName = 'Sponge'

    def move(self):
        print('I cant move!')

    def introduction(self):
        print('this is a kind of invertebrate animal names sponge')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Sponge._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')
    def call_density(self):
        print(f'my density is {self.density} gram per milliliter')

    def help(self):
        print(Guide.subclass(self))


class Fish(Vertebrate):
    _lifetime = 8

    def __init__(self, balletNum, skinType, weight, *args):
        super().__init__(*args)
        self.balletNum = balletNum
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Vertebrate'
        self._ClsName = 'Fish'


    def move(self):
        print('I am swimming')

    def introduction(self):
        print('this is a kind of vertebrate animal names fish')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Fish._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')
    def call_balletnum(self):
        print(f'my ballet number is {self.balletNum}')

    def help(self):
        print(Guide.subclass(self))


class Bird(Vertebrate):
    _lifetime = 4

    def __init__(self, speed, skinType, weight, *args):
        super().__init__(*args)
        self.speed = speed
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Vertebrate'
        self._ClsName = 'Bird'

    def move(self):
        print('I am flying')

    def introduction(self):
        print('this is a kind of vertebrate animal names bird')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Bird._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')
    def call_speed(self):
        print(f'my speed is {self.speed} meter per minute')

    def help(self):
        print(Guide.subclass(self))


class Reptile(Vertebrate):
    _lifetime = 12

    def __init__(self, livingPlace, skinType, weight, *args):
        super().__init__(*args)
        self.livingPlace = livingPlace
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Vertebrate'
        self._ClsName = 'Reptile'

    def move(self):
        print('I am crawling')

    def introduction(self):
        print('this is a kind of vertebrate animal names reptile')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Reptile._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')

    def call_livingPlace(self):
        print(f'my living place is {self.livingPlace}')

    def help(self):
        print(Guide.subclass(self))


class Amphibian(Vertebrate):
    _lifetime = 18

    def __init__(self, isToxic: bool, skinType, weight, *args):
        super().__init__(*args)
        self.isToxic = isToxic
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Vertebrate'
        self._ClsName = 'Amphibian'

    def move(self):
        print('I am jumping')

    def introduction(self):
        print('this is a kind of vertebrate animal names amphibian')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Amphibian._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')

    def Is_toxic(self):
        if self.isToxic is True:
            print('this amphibian is toxic')
        else:
            print('this kind of amphibian is not toxic')

    def help(self):
        print(Guide.subclass(self))


class Mammal(Vertebrate):
    _lifetime = 15

    def __init__(self, childNum, skinType, weight, *args):
        super().__init__(*args)
        self.childNum = childNum
        self.skinType = skinType
        self.weight = weight
        self._parentClsName = 'Vertebrate'
        self._ClsName = 'Mammal'

    def move(self):
        print('I am walking')

    def introduction(self):
        print('this is a kind of vertebrate animal names mammal')

    def remained_ages(self):
        if Check.check_age(self) == True:
            print(f'{Mammal._lifetime - self.age} years of my life remains')
        else:
            print('over aged!')

    def call_childnum(self):
        print(f'my child number is {self.childNum}')

    def help(self):
        print(Guide.subclass(self))


class Dog(Mammal):

    def __init__(self, *args):
        self._parentClsName = 'Mammal'
        self._ClsName = 'Dog'

    def make_sound(self):
        print('hup!!')

    def help(self):
        print(Guide.subclass(self))


class Cat(Mammal):

    def __init__(self, *args):
        self._parentClsName = 'Mammal'
        self._ClsName = 'Cat'

    def make_sound(self):
        print('meow!!')

    def help(self):
        print(Guide.subclass(self))


class Cow(Mammal):

    def __init__(self, *args):
        self._parentClsName = 'Mammal'
        self._ClsName = 'Cow'

    def make_sound(self):
        print('mou!!')

    def help(self):
        print(Guide.subclass(self))
##############################################################
# Guide class definition


class Guide:

    def guide(self):
        if self._ClsName == 'Vertebrate':
            msg1 = 'Vertebrate animals are those have skeleton body structure.'
            msg2 = 'you can define an object Vertebrate but I recommend to define your object by more details.'
            msg3 = 'in this case: Vertebrate subclasses are fish, birds, reptiles, amphibians and mammals.'
            return msg1 + '\n' + msg2 + '\n' + msg3
        elif self._ClsName == 'Invertebrate':
            msg1 = 'Invertebrate animals are those have not skeleton body structure.'
            msg2 = 'you can define an object Invertebrate but I recommend to define your object by more details.'
            msg3 = 'in this case: Invertebrate subclasses are worms and sponges'
            return msg1 + '\n' + msg2 + '\n' + msg3

    def subclass(self):
        return f'{self._ClsName} class is a subclass of {self._parentClsName} class'
##############################################################
# Check class definition


class Check:

    def check_age(self):
        if self.age > (self.__class__._lifetime):
            return False
        else:
            return True


##############################################################
# spongebob example


spongebob = Sponge(0.3, 'no skin type', 200, 21, 'spongebob', 'yellow', 'plankton')


spongebob.call_density()
print(spongebob.skinType)
##############################################################
# class dict check
Worm1 = Worm(10, 'no skin', 21, 10, 'bad worm', 'red', 'ant')
a = list(Worm1.__dict__)
print(a)
############################################################
# goldfish example


goldfish = Fish(10, 'pool', 1.2, 2, 'GoldenBoy', 'red', 'grass')


print(Check.check_age(goldfish))
print(type(Fish._lifetime))
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
goldfish.help()
print(goldfish.default_msg)
print(goldfish.balletNum)
print(goldfish.skinType)
print(goldfish.weight)

##############################################################
# Guide class test


v = Vertebrate(1, 'v1', 'red', 'vary')
v.help()

dog1 = Dog()
dog1.help()
##############################################################