import re
import unittest
import requests


#API_URL = URL
#URL = url
#r = res

class TestUser(unittest.TestCase):
    URL = "http://127.0.0.1:5000/user"
    user_id = 1
    url = "{}/{}".format(URL, user_id)

    def test_post_user(self):
        res = requests.post(TestUser.URL, json={'username': 'test_user'})
        result = res.json()

        #checking the statuscode
        self.assertEqual(res.status_code, 200)
        #checking content-type
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        #checking if number of returned json objects match
        self.assertEqual(len(result), 1)
        #checking if the correct username inserted and returned
        self.assertEqual(result['username'], 'test_user')

    def test_get_user(self):
        res = requests.get(TestUser.url)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertGreaterEqual(len(result), 1)
    
    def test_update_user(self):
        res = requests.put(TestUser.URL, json={'username': 'test_updated_user'})
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 1)
        self.assertEqual(result['username'], 'test_updated_user')

    def test_delete_user(self):
        res = requests.delete(TestUser.URL)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 1)


class TestBook(unittest.TestCase):
    URL = "http://127.0.0.1:5000/book"
    book_id = 1
    url = "{}/{}".format(URL, book_id)

    def test_post_book(self):
        res = requests.post(TestBook.URL, 
        json={'book_name': 'testBookName', 'genre': 'testGenre', 'author': 'testAuthor'})
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertEqual(len(result), 1)
        self.assertEqual(result['book_name'], 'testBookName')
    
    def test_get_book(self):
        res = requests.get(TestBook.url)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)
    
    def test_get_all_books(self):
        res = requests.get(TestBook.URL)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)

    def test_update_book(self):
        res = requests.put(TestBook.url,
        json={'book_name': 'updatedBookName', 'genre': 'updatedGenre', 'author': 'updatedAuthor'})
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertEqual(len(result), 1)
        self.assertEqual(result['book_name'], 'updatedBookName')

    def test_delete_book(self):
        res = requests.delete(TestBook.url)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertEqual(len(result), 1)


class SaleTest(unittest.TestCase):
    URL = "http://127.0.0.1:5000/sale"
    sale_id = 1
    url = "{}/{}".format(URL, sale_id)

    def test_post_sale(self):
        res = requests.post(SaleTest.URL, 
        json={'book_id': 'testBookId', 'user_id': 'testUserId'})
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertEqual(len(result), 1)
        self.assertEqual(result['book_id'], 'testBookId')
    
    def test_get_sale(self):
        res = requests.get(SaleTest.url)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)

    def test_delete_sale(self):
        res = requests.delete(SaleTest.URL)
        result = res.json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['content-type'], 'application/json')
        self.assertEqual(len(result), 1)

if __name__ == "__main":
    unittest.main()