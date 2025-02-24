# class methods - instance of a class
#functionality the same for each item
# @classmethod = this is a class method and knows what class it is inside

import random

class Hat:
    # one copy of that variable inside hat Class, houses variable (class variable), I can you use that list in any function
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # accessing the same list but acessing randomly
    # cls means class - use cls to access the class variable
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# don't need to instantiating - class methods (Class.method name)
Hat.sort("Harry")