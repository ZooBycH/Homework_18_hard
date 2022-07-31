from dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):  # получает всех режиссеров
        return self.session.query(Director).all()

    def get_director_by_id(self, director_id):  # получает режиссера по id
        return self.session.query(Director).get_or_404(director_id)

