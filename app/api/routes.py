from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Book, book_schema, books_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/books', methods=['POST'])
@token_required
def create_book(current_user_token):
    isbn = request.json['isbn']
    title = request.json['title']
    author = request.json['author']
    length = request.json['length']
    cover = request.json['cover']
    copyright = request.json['copyright']
    description = request.json['description']
    user_id = User.query.get(current_user_token.id)
    
    
    book = Book(isbn, title, author, length, cover, copyright, description, user_id=user_id)    
    
    db.session.add(book)
    db.session.commit()
    
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods = ['GET'])
@token_required 
def get_books(current_user_token):
    user_id = current_user_token.id
    books = Book.query.filter_by(user_id=user_id).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods=['GET'])
@token_required
def get_book(current_user_token, id):
    book = Book.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)



@api.route('/books/<id>', methods=['POST', 'PUT'])
@token_required
def update_book(current_user_token, id):
    book = Book.query.get(id)
    book.isbn = request.json['isbn']
    book.title = request.json['title']
    book.author = request.json['author']
    book.length = request.json['length']
    book.cover = request.json['cover']
    book.copyright = request.json['copyright']
    book.description = request.json['description']
    book.user_id = current_user_token.id
    
    
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books/<id>', methods=['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)