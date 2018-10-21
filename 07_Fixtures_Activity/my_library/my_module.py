"""
The super cool data science code you're working on
"""
import time


class SingleObject:

    already_instantiated = False

    def __init__(self, number):
        """You can only make one of these!"""
        if self.already_instantiated is True:
            print("This test is going to take a really really long time")
            time.sleep(60)

        self.mark_instantiated()
        self.number = number
        return

    @classmethod
    def mark_instantiated(cls):
        cls.already_instantiated = True

    def add_more(self, another_number):
        """Adds a number"""
        return another_number + self.number


if __name__ == "__main__":
    print("Using a single object only once")
    s = SingleObject(4)
    print(s.add_more(2))
