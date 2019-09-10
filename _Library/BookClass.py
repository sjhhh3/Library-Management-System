import sys
sys.path.append('..')

import datetime
from enums import BookSubject, BookStatus, BookFormat


class Book:
    def __init__(self, isbn: str, title: str, author: str, publisher: str,
                 language: str, subject: BookSubject, format: BookFormat, number_of_pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.language = language
        self.subject = subject
        self.format = format
        self.number_of_pages = number_of_pages

    def get_book_info(self):
        return self.__dict__


class BookItem:
    # def __init__(self, isbn, title, author, publisher, language, subject, format, number_of_pages, id):
    #     super().__init__(isbn, title, author, publisher, language, subject, format, number_of_pages)
    def __init__(self, book: Book, id: str):
        self.book = book
        self.id = id
        self.isbn_id = f'{self.book.isbn}-{id}'
        self.status = BookStatus.Available
        self.borrowed_date = None
        self.due_date = None
        self.date_of_purchase = datetime.date.today()

    def checkout(self) -> bool:
        self.status = BookStatus.Loaned
        self.borrowed_date = datetime.date.today()
        self.due_date = self.borrowed_date + datetime.timedelta(days=10)
        return True


class BookSet:
    def __init__(self, book: Book, location):
        self.book = book
        self.quantity = 0
        self.location = location
        self.bookitems = dict()

    def get_book_item_by_id(self, id) -> BookItem:
        assert 0 < int(id) <= self.quantity
        return self.bookitems[id]

    def create_book_item(self, amount):
        for _ in range(amount):
            self.quantity += 1
            self.bookitems[self.quantity] = BookItem(self.book, id=str(self.quantity))
        return True

    def check_availability(self):
        counter = 0
        for bookitem in self.bookitems.values():
            if bookitem.status == BookStatus.Available:
                counter += 1
        return counter

if __name__ == '__main__':

    pass