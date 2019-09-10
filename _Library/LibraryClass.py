import sys
sys.path.append('..')
sys.path.append('.')

from enums import Address, BookFormat, BookSubject
from _Library.BookClass import Book, BookSet


class Shelf:
    def __init__(self, shelf_id, rack):
        self.shelf_id = shelf_id
        self.rack = rack
        self.booksets = {}

    def __repr__(self):
        return f'{self.rack.rack_id}-{self.shelf_id}'

    def get_bookset(self):
        return self.booksets

class Rack:
    def __init__(self, rack_id: int, library):
        self.rack_id = rack_id
        self.library = library
        self.shelves_quantity = 0
        self.shelves = dict()

    def add_shelf(self) -> Shelf:
        self.shelves_quantity += 1
        self.shelves[self.shelves_quantity] = Shelf(self.shelves_quantity, self)
        return self.get_shelve_by_id(self.shelves_quantity)

    def get_shelve_by_id(self, shelf_id) -> Shelf:
        assert 0 < shelf_id <= self.shelves_quantity
        return self.shelves[shelf_id]


class Inventory:
    def __init__(self):
        self.book_inventory = dict()

    @staticmethod
    def create_new_book(isbn, title, author, publisher, language, subject, format, number_of_pages):
        return Book(isbn, title, author, publisher, language, subject, format, number_of_pages)

    def create_new_bookset(self, book: Book, shelf: Shelf) -> BookSet:
        bookset = BookSet(book, shelf)
        self.book_inventory[bookset.book.isbn] = bookset
        shelf.booksets[bookset.book.isbn] = bookset
        return self.book_inventory[bookset.book.isbn]

    def get_bookset_by_isbn(self, isbn: str) -> BookSet:
        return self.book_inventory[isbn]


class Library:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address
        self.rack_quantity = 0
        self.racks = dict()
        self.inventory = Inventory()

    def add_rack(self) -> Rack:
        self.rack_quantity += 1
        self.racks[self.rack_quantity] = Rack(self.rack_quantity, self)
        return self.get_rack_by_id(self.rack_quantity)

    def get_rack_by_id(self, rack_id: int) -> Rack:
        assert 0 < rack_id <= self.rack_quantity
        return self.racks[rack_id]


if __name__ == '__main__':
    pass
