"""
Complete Lab 4 and update the following information:

Author: [Your Name]
Date: [Date]
"""
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def __str__(self):
        return f"{self._title} by {self._author}"
    
    title = property()

def main():
    my_book = Book("Book", "Author")

if __name__ == "__main__":
    main()