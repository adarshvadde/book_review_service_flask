from .extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    reviews = db.relationship('Review', backref='book', lazy=True, cascade="all, delete-orphan")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    __table_args__ = (
        db.Index('idx_book_id', 'book_id'),
    )
