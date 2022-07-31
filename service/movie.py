from flask import request

from dao.model.models import Movie
from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all_movies(self) -> list[Movie]:
        """
        Возвращает список всех фильмов, а так же список фильмов по указанным параметрам запроса
        :return:
        """
        movies_query = self.movie_dao.get_all_movies()

        args = request.args

        director_id = args.get('director_id')  # условие с режиссером
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)

        genre_id = args.get('genre_id')  # условие с жанром
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)

        year = args.get('year')  # условие с годом выпуска в прокат
        if year is not None:
            movies_query = movies_query.filter(Movie.year == year)

        movies = movies_query.all()

        return movies

    def get_movie_by_id(self, movie_id):  # получает фильмы по id
        return self.movie_dao.get_movie_by_id(movie_id)

    def add_movie(self, data):  # добавляет фильм в таблицу
        self.movie_dao.create_movie(**data)

    def update_movie(self, data):  # обновляет данные о фильме по id
        self.movie_dao.update(data)

    def delete_movie(self, movie_id):  # Удаляет запись о фильме
        self.movie_dao.delete(movie_id)
