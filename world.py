class World:
    def __init__(self, world_name):
        self.name = world_name

    def hello(self):
        print("Hello, " + self.name + "!")

def say_hello(people):
    for person in people:
        print("Hello, " + person + "!")



