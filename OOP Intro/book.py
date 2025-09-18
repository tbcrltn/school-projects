class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def __str__(self):
        return f"{self._title} by {self._author}"
    
    def get_title(self):
        return self._title

    def set_title(self, new):
        if isinstance(new, str):
            if not new == "":
                self._title = new
            else: 
                raise ValueError("Title: string cannot be empty")
        else: 
            raise TypeError("Title needs to be string")   
        
        
    title = property(get_title, set_title)


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new):
        if isinstance(new, str):
            if not new == "":
                self._author = new
            else:
                raise ValueError("Author: string cannot be empty")
        else: 
            raise TypeError("Author needs to be string")
        
    @property
    def description(self):
        return f"{self._title}is a book written by {self._author}"



def main():
    my_book = Book("Book", "Author")
    my_book.title = "Business of the 21st Century"
    my_book.author = "Robert Kiyosaki"
    print(my_book)
    print(my_book.description)
    


if __name__ == "__main__":
    main()