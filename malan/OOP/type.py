# class methods - instance of a class
#functionality the same for each item
# @classmethod = this is a class method and knows what class it is inside

import random

class Hat:
    # init function intialization of the object
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    # accessing the same list but acessing randomly
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

# instantiating an object
hat = Hat()
hat.sort("Harry")