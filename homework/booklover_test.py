import unittest
from .booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`
        book_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_1.add_book("War of the Worlds", 4)
        book = "War of the Worlds"
        self.assertTrue(book in book_1.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_1.add_book("Lessons in Chemistry", 4)
        book_1.add_book("Lessons in Chemistry", 4)
        actual = book_1.book_list['book_name'].value_counts()['Lessons in Chemistry']
        expected = 1
        self.assertTrue(actual==expected)
                        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_1.add_book("Lessons in Chemistry", 4)
        self.assertTrue(book_1.has_read("Lessons in Chemistry"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_1.add_book("Lessons in Chemistry", 4)
        self.assertFalse(book_1.has_read("Harry Potter and the Chamber of Secrets"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_1.add_book("Disappearing Spoon", 2)
        book_1.add_book("It Ends With Us", 4)
        actual = book_1.num_books_read()
        expected = 2
        self.assertEqual(actual, expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_1.add_book("Harry Potter and the Chamber of Secrets", 4)
        book_1.add_book("Percy Jackson", 5)
        book_1.add_book("Crying in H Mart", 5)
        book_1.add_book("Disappearing Spoon", 2)
        book_1.add_book("It Ends With Us", 2)
        fav_books_list = book_1.fav_books()
        self.assertTrue((fav_books_list['book_rating'] > 3).all())
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)