import requests

from src.config.main_cfg import main_config


class BookFetcherService:
    api_url: str

    def __init__(self):
        self.api_url = main_config['BOOK_API_URL']

    def get_books(self):
        r = requests.get(f'{self.api_url}/books')
        return r.json()
