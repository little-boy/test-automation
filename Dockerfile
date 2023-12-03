FROM python:3.12

WORKDIR /usr/src/app

RUN curl -o /usr/src/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /usr/src/wait-for-it.sh

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


