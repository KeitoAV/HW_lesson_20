from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='Йеллоустоун', description='Description',
               trailer='trailer', year=2018, rating=8.6, genre_id=17, director_id=1)
    m2 = Movie(id=2, title='Омерзительная восьмерка', description='Description',
               trailer='trailer', year=2015, rating=7.8, genre_id=4, director_id=2)
    m3 = Movie(id=3, title='Вооружен и очень опасен', description='Description',
               trailer='trailer', year=1978, rating=6, genre_id=17, director_id=3)

    movies = {1: m1, 2: m2, 3: m3}

    movie_dao.get_one = MagicMock(return_value=Movie(id=2))
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=4))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_create(self):
        m4 = {
            'title': 'Джанго освобожденный',
            'description': 'Description',
            'trailer': 'trailer',
            'year': 2012,
            'rating': 8.4,
            'genre_id': 17,
            'director_id': 2
        }
        movie = self.movie_service.create(m4)
        assert movie is not None
        assert movie.id is not None

    def test_update(self):
        m1 = {
            'id': 1,
            'title': 'Йеллоустоун',
            'description': 'Description',
            'trailer': 'trailer',
            'year': 2019,
            'rating': 10.0,
            'genre_id': 2,
            'director_id': 3
        }
        self.movie_service.update(m1)

    def test_partially_update(self):
        m1 = {
            'id': 2,
            'year': 2010
        }
        self.movie_service.update(m1)

    def test_delete(self):
        self.movie_service.delete(1)
