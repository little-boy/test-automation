from dotenv import dotenv_values
import os

main_config = None

env = os.environ['ENV']

if env == 'test':
    main_config = {
        'BOOK_API_URL': os.environ['BOOK_API_URL'],
        'USER_API_URL': os.environ['USER_API_URL'],
    }
else:
    main_config = dotenv_values()

