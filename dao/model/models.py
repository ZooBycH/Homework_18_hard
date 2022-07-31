from setup_db import db


class Genre(db.Model):
    """
    Модель для таблицы жанров
    """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Director(db.Model):
    """
    Модель для таблицы режиссеров
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Movie(db.Model):
    """
    Модель для таблицы с фильмами
    """
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey(f"{Genre.__tablename__}.id"))
    director_id = db.Column(db.Integer, db.ForeignKey(f"{Director.__tablename__}.id"))
    genre = db.relationship("Genre")
    director = db.relationship("Director")
