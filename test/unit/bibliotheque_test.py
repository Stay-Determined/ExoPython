import unittest

from exercice2 import Book, Library, Client

class TestBook(unittest.TestCase):
    
    def test_check_out(self):
        book = Book("To Kill a Mockingbird", "CL1")
        if book.is_checked_out == False:
            book.check_out()
            self.assertTrue(book.is_checked_out)
        else:
            print("Book is already checkout")

    def test_check_in(self):
        book = Book("To Kill a Mockingbird", "CL2")
        if book.is_checked_out == False:
            book.check_out()
            self.assertTrue(book.is_checked_out)

            if book.is_checked_out == True:
                book.check_in()
                self.assertFalse(book.is_checked_out)
            else:
                print("Book isn't checkout")
        else:
            print("Book is already checkout")

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "CL1")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "CL2")
        self.library.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 2)
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)        

    def test_check_out_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.library.check_out_book("Pride and Prejudice")
        self.assertTrue(self.book2.is_checked_out)
        self.library.check_out_book("Unknow book")
        self.assertEqual(len(self.library.books), 2)
    
    def test_check_in_book(self):
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_out_book("Pride and Prejudice")
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.library.check_in_book("Pride and Prejudice")
        self.assertFalse(self.book2.is_checked_out)
        self.library.check_in_book("Unknow book")
        self.assertEqual(len(self.library.books), 2)
        
        
        
class TestClient(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "CL1")
        self.library.add_book(self.book1)
        self.book2 = Book("Pride and Prejudice", "CL2")
        self.library.add_book(self.book2)
        self.client = Client("Pierre")

    def test_check_out_book(self):
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertIn(self.book1, self.client.checked_out_books)
        self.assertTrue(self.book1.is_checked_out)
        self.client.check_out_book(self.library, "Pride and Prejudice")
        self.assertIn(self.book2, self.client.checked_out_books)
        self.assertTrue(self.book2.is_checked_out)
        self.client.check_out_book(self.library, "Unknow book")
        self.assertEqual(len(self.client.checked_out_books), 2)

    def test_check_in_book(self):
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.client.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertNotIn(self.book1, self.client.checked_out_books)
        self.assertFalse(self.book1.is_checked_out)
        self.client.check_in_book(self.library, "Unknow book")
        self.assertEqual(len(self.client.checked_out_books), 0) 
        
# Afficher le checking des test
if __name__ == '__main__':
    unittest.main()