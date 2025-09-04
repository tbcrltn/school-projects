class Person:
    def __init__(self, first, last, age = 20):
        self._first = first
        self.__last = last
        self.age = age

    def __str__(self):
        return f"First name is {self._first}, last name is {self.__last}"
    
    def get_last(self):
        return self.__last
    
    def set_new_last(self, new):
        self.__last = new
    
p1 = Person("Jim", "Green")

print(p1.get_last())
p1.set_new_last("Brown")
print(p1.get_last())