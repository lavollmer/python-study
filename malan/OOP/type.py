# class methods - instance of a class
#functionality the same for each item
# @classmethod = this is a class method and knows what class it is inside

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    def sort(self, name):
        print(name, "is in", "some house")

# instantiating an object
hat = Hat()
hat.sort("Harry")