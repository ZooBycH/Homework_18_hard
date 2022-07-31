from dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):  # получает все жанры
        return self.session.query(Genre).all()

    def get_genre_by_id(self, genre_id):  # получает жанры по id
        return self.session.query(Genre).get_or_404(genre_id)
