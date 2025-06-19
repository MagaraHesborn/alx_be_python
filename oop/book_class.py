class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def __del__(self):
        print(f"Deleating {self.title}")