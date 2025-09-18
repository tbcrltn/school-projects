class Person:
    def __init__(self, first, last, age = 20):
        self._first = first
        self.__last = last
        self.__age = age

    def __str__(self):
        return f"first name: {self._first}, last name: {self.__last}, age: {self.__age}"
    

    @property
    def last_name(self):
        return self.__last
    
    @last_name.setter
    def last_name(self, name):
        if isinstance(name, str):
            self.__last = name
        else:
            raise TypeError("Name has to be string")
        

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new):
        if isinstance(new, int) and new >= 0:
            self.__age = new
        else:
            raise TypeError("Age has to be int >= 0")

    
p1 = Person("jimmy", "green")
p1.last_name = "Black"
print(p1.last_name)

p1.age = 21
print(p1.age)