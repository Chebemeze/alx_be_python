class Book:
  
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False

  def is_available(self):
    return not self._is_checked_out

  def check_out(self):
    if not self._is_checked_out:
      self._is_checked_out = True
  
  def return_book(self):
    if self._is_checked_out:
      self._is_checked_out = False

  def __str__(self):   #Function formats how the title and author are printed anything the print method is called
    return (f"{self.title} by {self.author}")


class Library:

  def __init__(self):
    self._books = []
    self._checked_out_books = []

# Add book method. Adds book oject to a list.
  def add_book(self, book):
    self._books.append(book)

# Check out method. adds it to checked out list then removes the specified object from the available list.
  def check_out_book(self, title):

    for book in self._books:
      if book.title == title and book.is_available():
        self._checked_out_books.append(book)
        self._books.remove(book)
        book.check_out()

  # Return removed books method.
  def return_book(self, title):

    for book in self._checked_out_books:
      if book.title == title and not book.is_available():
        self._books.append(book)
        book.return_book()
  
  # List available books method.
  def list_available_books(self):
    for book in self._books:
      print(book)