import requests

from ..config.main_cfg import main_config


class UserFetcherService:
    api_url: str

    def __init__(self):
        print(main_config)
        self.api_url = main_config['USER_API_URL']

    def get_users(self):
        print(f'HEEEY {self.api_url}/users')
        r = requests.get(f'{self.api_url}/users')
        return r.json()
