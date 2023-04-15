this python codes are all for problem 1 in sharif university technology advanced programming course.
other useful informations are available in code comments and class diagram.
attribute and method names are obviously defined to help you understand every part of the code.
written by Erfan Dehghan.
________________________________________________________________
in general, there is four level of classes that makes inheritance. for shorter description it has been defined:
level 1: [Animal] class
level 2: [Vertebrate, Invertebrate] classes
level 3: [Fish, Bird, Reptile, Amphibian, Mammal, Worm, Sponge] classes
level 4: [Dog, Cat, Cow] classes
as you know, each of these class levels are a child of one of the classes in upper level.
________________________________________________________________
in each level of classes, there are some methods:
in level 2, [call_bodystructure(), help()] are in common between classes.
in level 3, [move(), introduction(), remained_ages(), help()] are in common between classes.
in level 3, [call_bulletNum(), call_speed(), call_livingPlace(), Is_toxic(), call_childnum(), call_lenght(), call_density()] are defined specefic for one class.
in level 4, [make_sound(), help()] are in common between classes.
________________________________________________________________
in each level of classes, there are some attributes:
in level 2, [parentClsName, _ClsName] are in common between classes.
in level 3, [parentClsName, _ClsName, _lifetime, skinType, weight] are in common between classes.
in level 3, [bulletNum, speed, livingPlace, isToxic, childNum, length, density] are defined specific.
in level 4, [parentClsName, _ClsName] are in common between classes.
________________________________________________________________
to avoide more repetition method definitaion, it has been defined these two classes:
class 1: [Guide] class include [guide(), subclass()] methods. these two functions are used in all other class with the name [help()].
class 2: [Check] class include [check_age()] method. this function is used in [remained_ages()] method in level3 classes.
________________________________________________________________