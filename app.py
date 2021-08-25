from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os


# Initializing app
app = Flask(__name__)

#setting up SQLAlchemy database uri
basedir = os.path.abspath(os.path.dirname(__file__))

#setting up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dbalchemy.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing database
dbal = SQLAlchemy(app)
# Initializing marshmallow
marshy = Marshmallow(app)

#Creating User Class/Model
class User(dbal.Model):
    user_id = dbal.Column(dbal.Integer,primary_key = True)
    username = dbal.Column(dbal.String(100), unique=True)

    def __init__(self, username):
        self.username = username


#Creating Sales Class/Model
class Sales(dbal.Model):
    sales_id = dbal.Column(dbal.Integer, primary_key = True)
    user_id = dbal.Column(dbal.String(100))
    book_id = dbal.Column(dbal.String(100))

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

#Creating Book Class/Model
class Book(dbal.Model):
    book_id = dbal.Column(dbal.Integer, primary_key = True)
    book_name = dbal.Column(dbal.String(100))
    genre = dbal.Column(dbal.String(100))
    author = dbal.Column(dbal.String(100))

    def __init__(self, book_name, genre, author):
        self.book_name = book_name
        self.genre = genre
        self.author = author




#Creating User Schema
class UserSchema(marshy.Schema):
    class Meta:
        fields = ('user_id', 'username')


#Creating Book Schema
class BookSchema(marshy.Schema):
    class Meta:
        fields = ('book_id', 'book_name', 'genre' , 'author')

#Creating Sales Schema
class SalesSchema(marshy.Schema):
    class Meta:
        fields = ('sales_id', 'user_id', 'book_id')

# Init Schema
user_schema = UserSchema()
book_schema = BookSchema()
books_schema = BookSchema(many=True)
sales_schema = SalesSchema()


#Checking the APIResponse
@app.route('/')
def send_response():
    return jsonify({"Message" : "It's Up And Running"})


#Route for creating new user
@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    new_user = User(username)

    dbal.session.add(new_user)
    dbal.session.commit()

    return user_schema.jsonify(new_user)

#Getting the user data
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)


#Updating the user data
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    username = request.json['username']
    user.username = username
    dbal.session.commit()
    return user_schema.jsonify(user)

#Deleting the user data
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    sales = Sales.query.all()
    for sale in sales:
        if sale.user_id == user_id:
            dbal.session.delete(sale)
    user = User.query.get(user_id)
    dbal.session.delete(user)
    dbal.session.commit()
    return user_schema.jsonify(user)


#Creating new book 
@app.route('/book', methods=['POST'])
def add_book():
    book_name = request.json['book_name']
    genre = request.json['genre']
    author = request.json['author']

    new_book = Book(book_name, genre, author)
    dbal.session.add(new_book)
    dbal.session.commit()
    return book_schema.jsonify(new_book)

#Getting one book details
@app.route('/book/<book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    return book_schema.jsonify(book)

#Getting all books details
@app.route('/book', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    result = books_schema.dump(books)
    return books_schema.jsonify(result)

#Updating one book details
@app.route('/book/<book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    book.book_name = request.json['book_name']
    book.genre = request.json['genre']
    book.author = request.json['author']
    dbal.session.commit()
    return book_schema.jsonify(book)

#Deleting one book details
@app.route('/book/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    sales = Sales.query.all()
    for sale in sales:
        if sale.book_id == book_id:
            dbal.session.delete(sale)
    book = Book.query.get(book_id)
    dbal.session.delete(book)
    dbal.session.commit()
    return book_schema.jsonify(book)

#Creating a sales record
@app.route('/sale', methods=['POST'])
def create_sale():
    user_id = request.json['user_id']
    book_id = request.json['book_id']
    new_sale = Sales(user_id, book_id)
    dbal.session.add(new_sale)
    dbal.session.commit()
    return sales_schema.jsonify(new_sale)


#Getting a sales record
@app.route('/sale/<sales_id>', methods=['GET'])
def get_sale(sales_id):
    sale  = Sales.query.get(sales_id)
    return sales_schema.jsonify(sale)

#Deleting a sales record
@app.route('/sale/<sales_id>', methods=['DELETE'])
def update_sale(sales_id):
    sale = Sales.query.get(sales_id)
    dbal.session.delete(sale)
    dbal.session.commit()
    return sales_schema.jsonify(sale)

#Running the Server
if __name__ == '__main__':
  app.run(debug=True)