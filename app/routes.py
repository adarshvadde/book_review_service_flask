from flask import Blueprint, request, jsonify
from .models import Book, Review
from .extensions import db, cache

book_routes = Blueprint('books', __name__)

@book_routes.route('/books', methods=['GET'])
def get_books():
    """
    Get list of all books
    ---
    responses:
      200:
        description: A list of books
    """
    try:
        cached = cache.get('books')
        if cached:
            return jsonify(cached)
    except Exception as e:
        print(f"Redis cache.get failed: {e}")
        cached = None  # fallback

    # On cache miss or Redis error
    books = Book.query.all()
    book_list = [{'id': b.id, 'title': b.title} for b in books]

    try:
        cache.set('books', book_list, timeout=60)
    except Exception as e:
        print(f"Redis cache.set failed: {e}")

    return jsonify(book_list)


@book_routes.route('/books', methods=['POST'])
def add_book():
    """
    Add a new book
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
    responses:
      200:
        description: Book added
    """
    data = request.get_json()
    book = Book(title=data['title'])
    db.session.add(book)
    db.session.commit()
    return jsonify({'id': book.id, 'title': book.title})

@book_routes.route('/books/<int:book_id>/reviews', methods=['GET'])
def get_reviews(book_id):
    reviews = Review.query.filter_by(book_id=book_id).all()
    return jsonify([{'id': r.id, 'content': r.content} for r in reviews])

@book_routes.route('/books/<int:book_id>/reviews', methods=['POST'])
def add_review(book_id):
    """
    Add a review to a book
    ---
    parameters:
      - name: book_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            content:
              type: string
    responses:
      200:
        description: Review added
    """
    data = request.get_json()
    review = Review(content=data['content'], book_id=book_id)
    db.session.add(review)
    db.session.commit()
    return jsonify({'id': review.id, 'content': review.content})
