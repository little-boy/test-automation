# https://docs.python.org/3/library/typing.html#the-any-type

from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService
from tests.utils.array import is_equal_unordered

def test_list_user_multiple_users(monkeypatch):
    user_service = UserService(user_fetcher_service=UserFetcherService())
    users = user_service.list_users()

    assert is_equal_unordered(users, [
        {
            'id': 1,
            'email': 'john.doe@gmail.com'
        }, {
            'id': 2,
            'email': 'jane.doe@gmail.com'
        }, {
            'id': 3,
            'email': 'johnny.doe@gmail.com'
        }
    ])
