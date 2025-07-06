import pytest

from books_collector import BooksCollector

@pytest.fixture(scope='function')
def books_collector():
        return BooksCollector()

