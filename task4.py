class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("-" * 30)

book1 = Book("Howl's Moving Castle", "Diana Wynne Jones", 1986)
book2 = Book("I Love You Ara", "Jumille Fumah", 2015)
book3 = Book("Tantei High", "Purpleyhan", 2019)

book1.describe()
book2.describe()
book3.describe()