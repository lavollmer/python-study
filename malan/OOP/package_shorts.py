class Package:
    # dunder init = dunder means double underscores
    # self new instance of the class we are creating
    def __init__(self, number, sender, recipient, weight):
        # variables belong to the instance of the class
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return (
            f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}"
        )

    def calculate_cost(self, cost_per_kg):
        return cost_per_kg * self.weight


def main():
    # list, contains two strings
    # store ID, sender, receiver, weight
    # strings are too flexible, want something more rigid
    # Package() is calling the def init
    packages = [
        # creating a new instance
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Charlie", recipient="Joe", weight=5),
    ]

    # print the dunder str
    for package in packages:
        print(f"{package}, costs: {package.calculate_cost(cost_per_kg=2)}")


main()
