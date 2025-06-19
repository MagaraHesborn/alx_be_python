class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, file_size: int):
        super().__init__(self.title, self.author)
        self.file_size: int = file_size

class PrintBook(Book):
    def __init__(self,page_count: int):
        super().__init__(self.title, self.author)
        self.page_count: int = page_count

class Library:
    pass