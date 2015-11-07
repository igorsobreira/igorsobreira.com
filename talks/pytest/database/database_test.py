import pytest

from database import Database

@pytest.fixture
def db(request):
    db = Database('mongodb://localhost:27017/registrations')
    request.addfinalizer(db.clear)
    return db

def test_database_create_and_find_all(db):
    db.create({'name': 'igor', 'category': 'OC1'})
    db.create({'name': 'josh', 'category': 'V1'})

    assert db.find_all() == [
        {'name': 'igor', 'category': 'OC1'},
        {'name': 'josh', 'category': 'V1'},
    ]


import time

@pytest.mark.slow
def test_with_fixed_time(monkeypatch):
    def mocked_time():
        return 123
    monkeypatch.setattr(time, 'time', mocked_time)

    assert time.time() == 123
