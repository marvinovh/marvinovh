from datetime import date


class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)

    def info(self):
        print(f'title = {self.title}')
        print(f'author = {self.author}')
        print(f'year = {self.year}')

    def __str__(self):
        return f'"{self.title}" — {self.author} ({self.year})'

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)

    @property
    def age(self):
        return date.today().year - self.year

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age must be >= 0')
        self.year = date.today().year - int(value)

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(', ')
        return cls(title, author, year)
