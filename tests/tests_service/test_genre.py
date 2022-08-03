from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService
from setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='комедия')
    g2 = Genre(id=2, name='Семейный')
    g3 = Genre(id=3, name='Фэнтези')

    genres = {1: g1, 2: g2, 3: g3}

    genre_dao.get_one = MagicMock(return_value=Genre(id=2))
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=Genre(id=4))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) > 0

    def test_create(self):
        g4 = {'name': 'драма'}
        genre = self.genre_service.create(g4)
        assert genre is not None
        assert genre.id is not None

    def test_update(self):
        g4 = {'id': 4, 'name': 'Драма'}
        self.genre_service.update(g4)

    def test_partially_update(self):
        g1 = {'id': 1, 'name': 'Комедия'}
        self.genre_service.update(g1)

    def test_delete(self):
        self.genre_service.delete(1)
