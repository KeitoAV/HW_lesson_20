from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='Тейлор Шеридан')
    d2 = Director(id=2, name='Квентин Тарантино')
    d3 = Director(id=3, name='Владимир Ваййншток')

    directors = {1: d1, 2: d2, 3: d3}

    director_dao.get_one = MagicMock(return_value=Director(id=2))
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=Director(id=4))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(3)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        d4 = {'name': 'Декстерp Флетчер'}
        director = self.director_service.create(d4)
        assert director is not None
        assert director.id is not None

    def test_update(self):
        d4 = {'id': 4, 'name': 'Декстер Флетчер'}
        self.director_service.update(d4)

    def test_partially_update(self):
        d3 = {'id': 3, 'name': 'Владимир Вайншток'}
        self.director_service.update(d3)

    def test_delete(self):
        self.director_service.delete(1)
