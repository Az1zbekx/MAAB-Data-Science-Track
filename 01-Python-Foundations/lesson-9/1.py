class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books")
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, title):
        book = None
        for b in self.books:
            if b.title == title:
                book = b
                break
        if not book:
            raise BookNotFoundException(f"'{title}' does not exist in the library")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{title}' is already borrowed")
        member.borrow_book(book)
        book.is_borrowed = True

    def return_book(self, member, title):
        book = None
        for b in self.books:
            if b.title == title:
                book = b
                break
        if book and book in member.borrowed_books:
            member.return_book(book)
            book.is_borrowed = False


lib = Library()


lib.add_book(Book("Python Basics", "John Doe"))
lib.add_book(Book("AI for Beginners", "Jane Doe"))
lib.add_book(Book("Data Science", "Someone"))
lib.add_book(Book("Cybersecurity", "Hacker"))


m1 = Member("Ali")
lib.add_member(m1)


try:
    lib.borrow_book(m1, "Python Basics")
    lib.borrow_book(m1, "AI for Beginners")
    lib.borrow_book(m1, "Data Science")
    lib.borrow_book(m1, "Cybersecurity") 
except BookNotFoundException as e:
    print("BookNotFound:", e)
except BookAlreadyBorrowedException as e:
    print("BookAlreadyBorrowed:", e)
except MemberLimitExceededException as e:
    print("MemberLimitExceeded:", e)


try:
    lib.borrow_book(m1, "Nonexistent Book") 
except Exception as e:
    print(e)


lib.return_book(m1, "Python Basics")


try:
    lib.borrow_book(m1, "Cybersecurity") 
    print(f"{m1.name} successfully borrowed 'Cybersecurity'")
except Exception as e:
    print(e)


print(f"{m1.name} has borrowed: {[b.title for b in m1.borrowed_books]}")
