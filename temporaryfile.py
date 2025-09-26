class Flyer:
    def __init__(self, wingspan):
        self.wingspan = wingspan
    
    def move(self):
        print("flying through the sky")

class Swimmer:
    def __init__(self, swim_speed):
        self.swim_speed = swim_speed

    def move(self):
        print("swimming through the water")


class Duck(Swimmer, Flyer):
    def __init__(self, wingspan, swim_speed, name):
        Swimmer.__init__(self, swim_speed)
        Flyer.__init__(self, wingspan)

        self.name = name

    def __str__(self):
        return f"Swim speed:{self.swim_speed}  Wingspan: {self.wingspan}  Name: {self.name}"

    def sound(self):
        print("Quack")

duck = Duck(40, 5, "donald")

print(duck)
