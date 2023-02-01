from datetime import datetime
from db import db

class MoviesModel(db.Model):

    __tablename__ = 'movie_tbl'
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    numberInStock = db.Column(db.Integer,nullable=False)
    dailyRentalRate = db.Column(db.Float(),nullable=False)
    publishDate = db.Column(db.DateTime, default=datetime.now())
    liked = db.Column(db.Boolean, default=False, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre_tbl._id'))

    def json(self):
        return {
            '_id': self._id,
            'title': self.title,
            'genre': self.genre.json(),
            'numberInStock': self.numberInStock,
            'dailyRentalRate': self.dailyRentalRate,
            'liked': self.liked,
            'publishDate': {
                'year':self.publishDate.strftime("%Y"),
                'month':self.publishDate.strftime("%b"),
                'day':self.publishDate.strftime("%d"),
            },
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)
    
    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
