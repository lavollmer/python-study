class Package:
    # dunder init = dunder means double underscores
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


def main():
    # list, contains two strings
    # store ID, sender, receiver, weight
    # strings are too flexible, want something more rigid
    # Package() is calling the def init
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Charlie", recipient="Joe", weight=12),
    ]


main()
