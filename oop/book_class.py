#!/usr/bin/python3
"""
Book class demonstrating Python magic methods
"""


class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

