from flask_restx import Resource, Namespace
from flask import request

from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Получение списка всех фильмов
        :return:
        """
        return movie_schema.dump(movie_service.get_all_movies()), 200

    def post(self):
        """
        Добавление нового фильма
        :return:
        """
        movie_service.add_movie(request.json)
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        """
        Получение  фильмов по id
        :return:
        """
        return movie_schema.dump([movie_service.get_movie_by_id(movie_id)]), 200

    def put(self, movie_id):
        """
        Изменение данных о фильме с указанным id
        :return:
        """
        request.json["id"] = movie_id
        movie_service.update_movie(request.json)
        return "", 200

    def delete(self, movie_id):
        """
        удаление фильма с указанным id
        :param movie_id:
        :return:
        """
        movie_service.delete_movie(movie_id)

        return "", 204
