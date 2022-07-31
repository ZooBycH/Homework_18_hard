from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):  # получает все фильмы
        return self.session.query(Movie)

    def get_movie_by_id(self, movie_id):  # получает фильм по id
        return self.session.query(Movie).get_or_404(movie_id)

    def get_movie_by_director_id(self, director_id):  # получает все фильмы режиссера по id
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):  # получает все фильмы жанра по id
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):  # получает все фильмы определенного года
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie_by_many_filters(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create_movie(self, **kwargs):  # добавляет новый фильм в таблицу
        try:
            self.session.add(
                Movie(
                    **kwargs
                )
            )
            self.session.commit()
        except Exception as e:
            print(f"Не удалось добавить данные\n{e}")
            self.session.rollback()

    def update(self, data):  # обновляет данные о фильме по id
        try:
            movie_id = data.get("id")
            self.session.query(Movie).filter(Movie.id == movie_id).update(
                data
            )
            self.session.commit()
        except Exception as e:
            print(f"Не удалось обновить фильм\n{e}")
            self.session.rollback()

    def delete(self, movie_id):  # удаляет фильм из таблицы
        try:
            self.session.query(Movie).filter(Movie.id == movie_id).delete()
            self.session.commit()

        except Exception as e:
            print(f"Не удалось удалить фильм\n{e}")
            self.session.rollback()
