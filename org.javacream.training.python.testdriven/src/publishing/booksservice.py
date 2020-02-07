class Book(object):
    def __init__(self, isbn, title, pages, price):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.price = price
    def info(self):
        return "Book: isbn=%s, title=%s, pages=%.0f, price=%.2f" %(self.isbn, self.title, self.pages, self.price)
    def __repr__(self):
        return self.info()
    
class BooksService(object):
    def __init__(self):
        self.books = {}
    def init(self, isbngenerator = None, storeservice = None):
        self.isbngenerator = isbngenerator
        self.storeservice = storeservice
    def new(self, title, pages=0, price=0):
        isbn = self.isbngenerator.next_isbn()
        print ("generated isbn %s" %(isbn))
        book = Book("Book-" +  self.isbngenerator.next_isbn(), title, pages, price)
        self.books[book.isbn] = book
        return book.isbn
    def find_book_by_isbn(self, isbn):
        book = self.books[isbn]
        stock = self.storeservice.get_stock("Book", book.title)
        print ("Retrieved stock is %.0f" % (stock))
        book.available = (self.storeservice.get_stock("Book", book.title) >= 0)
        return book
    def delete_book_by_isbn(self, isbn):
        self.books.pop(isbn)            
    def find_all(self):
        return self.books.values()
    def update(self, isbn, **values):
        price = values["price"]
        pages = values["pages"]
        if isbn in self.books:
            book = self.books[isbn]
        else:
            book = Book(isbn, "", 0, 0)
            self.books[isbn] = book
        if price:
            book.price = price
        if pages:
            book.pages = pages
