from enum import Enum

class BookFormat(Enum):
    Hardcopy = 0
    Paperback = 1
    Audiobook = 2
    Ebook = 3
    Newspaper = 4
    Magazine = 5
    Journal = 6


class BookStatus(Enum):
    Reserved = 0
    Available = 1
    Loaned = 2
    Lost = 3


class ReservationStatus(Enum):
    Waiting = 0
    Complete = 1
    Pending = 2
    Canceled = 3
    Unknown = 4


class AccountStatus(Enum):
    Closed = 0
    Active = 1
    Canceled = 2
    Blacklisted = 3
    Unknown = 4


class BookSubject(Enum):
    Literature = 0
    Poetry = 1
    Fiction = 2
    Biography = 3
    Sports = 4
    Art = 5
    Science = 6
    Politics = 7


class Address:
    def __init__(self, street_address: str, city: str, state: str, zipcode: str, country: str):
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

    def __repr__(self):
        return ', '.join(self.__dict__.values())


class Person:
    def __init__(self, name: str, address: Address, email: str, phone: str):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    def __repr__(self):
        return ', '.join(self.__dict__.values())

if __name__ == '__main__':
    print(AccountStatus(1))
    print(AccountStatus['Canceled'].value)

    for name, member in AccountStatus.__members__.items():
        print(name, '--->', member)