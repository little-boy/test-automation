import pytest

from services.book_fetcher_service import BookFetcherService
from services.book_service import BookService

def test_list_book_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            { 'id': 'aaa-001', 'name': 'Origine', 'author': { 'firstname': 'Dan', 'lastname': 'Brown' }},
            { 'id': 'aaa-002', 'name': 'Anges & Démons', 'author': { 'firstname': 'Dan', 'lastname': 'Brown' }},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ['aaa-001', 'aaa-002']

def test_list_authors(monkeypatch):
    pass