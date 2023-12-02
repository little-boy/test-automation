## Book service

### How to dev 
- install project requirements : `pip install --no-cache-dir -r requirements.txt`
- start fake book server : `docker-compose up`
- check books are well returned : `curl -X GET http://localhost:1080/books`

#### lint
- Run `python -m ruff .`

#### mypy
- Run `python -m mypy src`

#### unit tests
- Run `python -m pytest tests/unit`

#### integration tests
- Run `docker-compose up --build --exit-code-from=test`