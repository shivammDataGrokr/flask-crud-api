import unittest
import requests

class UserTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/user"
    user_id = 1
    URL = "{}/{}".format(API_URL, user_id)
    def test_get_user(self):
        r = requests.get(UserTest.URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)

    def test_post_user(self):
        r = requests.post(UserTest.API_URL, json={'username': 'test_username'})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 2)
        self.assertEqual(result['username'], 'test_username')

    def test_update_user(self):
        r = requests.put(UserTest.URL, json={'username': 'test_username_2'})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 2)
        self.assertEqual(result['username'], 'test_username_2')

    def test_delete_user(self):
        r = requests.delete(UserTest.URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 2)


class BookTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/book"
    book_id = 1
    URL = "{}/{}".format(API_URL, book_id)

    def test_get_all_books(self):
        r = requests.get(BookTest.API_URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)


    def test_get_book(self):
        r = requests.get(BookTest.URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)

    def test_post_book(self):
        r = requests.post(BookTest.API_URL, json={'book_name': 'test_book_name', 'genre': 'test_genre', 'author': 'test_author'})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 4)
        self.assertEqual(result['book_name'], 'test_book_name')

    def test_update_book(self):
        r = requests.put(BookTest.URL, json={'book_name': 'test_book_name_2', 'genre': 'test_genre_2', 'author': 'test_author_2'})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 4)
        self.assertEqual(result['book_name'], 'test_book_name_2')

    def test_delete_book(self):
        r = requests.delete(BookTest.URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 4)



class SaleTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/sale"
    sale_id = 1
    URL = "{}/{}".format(API_URL, sale_id)

    def test_get_sale(self):
        r = requests.get(SaleTest.URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)

    def test_post_sale(self):
        r = requests.post(SaleTest.API_URL, json={'book_id': 'test_book_id', 'user_id': 'test_user_id'})
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 3)
        self.assertEqual(result['book_id'], 'test_book_id')

    def test_delete_sale(self):
        r = requests.delete(SaleTest.URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(len(result), 3)



class QueryTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/query"

    def test_get_query(self):
        r = requests.get(QueryTest.API_URL)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertGreaterEqual(len(result), 0)
