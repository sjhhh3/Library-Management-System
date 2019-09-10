import sys
sys.path.append('..')

from _Library.BookClass import Book, BookSet, BookItem
from _Library.LibraryClass import Library, Rack, Shelf
from enums import BookSubject, BookStatus, BookFormat, Address


class Printer:
    def __init__(self):
        pass

    def book_printer(self, book):
        assert isinstance(book, Book)
        print(f"Book name: {book.title}, written by {book.author}.\n"
              f"Please use {book.isbn} to query book locations.")

    def bookset_printer(self, bookset):
        assert isinstance(bookset, BookSet)
        print(f"Book name: {bookset.book.title}, placed at {bookset.location}, "
              f"current available quantity is {bookset.check_availability()}.")

    def library_printer(self, library):
        assert isinstance(library, Library)
        print(f"{library.name}, located at {library.address},"
              f" with {len(library.racks)} {'racks' if len(library.racks)>1 else 'rack'}")

    def rack_printer(self, rack):
        assert isinstance(rack, Rack)
        print(f"{rack.library.name}, rack id {rack.rack_id},"
              f" with {len(rack.shelves)} {'shelves' if len(rack.shelves)>1 else 'shelf'}")

    def shelf_printer(self, shelf):
        assert isinstance(shelf, Shelf)
        print(f"{shelf.rack.library.name}, rack id {shelf.rack.rack_id},"
              f" shelf id {shelf.shelf_id}, placing following books:")
        for bs in shelf.booksets.values():
            self.bookset_printer(bs)

    def shelf_detailed_printer(self, shelf):
        assert isinstance(shelf, Shelf)
        print(f"{shelf.rack.library.name}, rack id {shelf.rack.rack_id},"
              f" shelf id {shelf.shelf_id}, placing following books:")
        for bs in shelf.booksets.values():
            for bi in bs.bookitems.values():
                self.bookitem_printer(bi)

    def bookitem_printer(self, bookitem):
        assert isinstance(bookitem, BookItem)
        if bookitem.status == BookStatus.Available:
            print(f"Book id of {bookitem.isbn_id}, is {bookitem.status.name}.")
        elif bookitem.status == BookStatus.Loaned:
            print(f"Book id of {bookitem.isbn_id} is {bookitem.status.name},"
                  f" due date is {bookitem.due_date}.")
        else:
            print(f"Book id of {bookitem.isbn_id} is {bookitem.status.name}.")


if __name__ == '__main__':
    a1 = Address('503 Beautiful Rd', 'Thiscity', 'WA', '98188', 'USA')
    l1 = Library('Tom Library', a1)
    r1 = l1.add_rack()
    r2 = l1.add_rack()
    s1 = r1.add_shelf()
    s11 = r1.add_shelf()
    s2 = r2.add_shelf()

    print(s1,s2)

    bk1 = l1.inventory.create_new_book('0-7475-3269-9',"Harry Potter and The Philosopher's Stone",
                                 "J. K. Rowling", "Bloomsbury Publishing", "English",
                                 BookSubject.Fiction, BookFormat.Hardcopy, 336)

    bk2 = l1.inventory.create_new_book('0-7475-5100-6',"Harry Potter and The Order of the Phoenix",
                                 "J. K. Rowling", "Bloomsbury Publishing", "English",
                                 BookSubject.Fiction, BookFormat.Hardcopy, 389)

    bs1 = l1.inventory.create_new_bookset(bk1, s2)
    bs2 = l1.inventory.create_new_bookset(bk2, s2)
    bs1.create_book_item(5)
    bs2.create_book_item(3)
    Printer().library_printer(l1)
    Printer().rack_printer(r1)
    Printer().shelf_detailed_printer(s2)
    bs1.get_book_item_by_id(2).checkout()
    bs2.get_book_item_by_id(3).checkout()
    # Printer().bookitem_printer(bs2.get_book_item_by_id(3))
    print("\nAfter check out books")
    Printer().shelf_detailed_printer(s2)