class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not Found"
        
book1 = Book("Lord of the Boots", "Joke Rolling", 340)
book2 = Book("Fantasia Banana", "Rolling Metal", 584)

print(book1['title'])