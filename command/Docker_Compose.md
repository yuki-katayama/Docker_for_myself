# Docker Compose(Django)
1. Dockerfileか、image(docker hubなどに)を用意する.
2. docker-compose.ymlを定義する
3. docker-compose up -d を実行する

### Djangoの環境を構築する
https://docs.docker.com/compose/django/

Dockerfile
```
FROM python:3
ENV PYTHONUNBUFFERED 1 //変数に 1 を代入
RUN mkdir /code  //コードディレクトリを作成
WORKDIR /code.  //作業ディレクトリをcodeに移動
COPY requirements.txt /code/  //buildcontext上にあるrequirements.txtを/codeディレクトリ内に置く。requirements.txtにインストールしたいパッケージなどを記述する
RUN pip install -r requirements.txt 
COPY . /code/
```
---
requirements.txt
```
Django>=3.0,<4.0
psycopg2-binary>=2.8
```
---
docker-compose.yml
```
  version: '3'
    
  services:
    db:
      image: postgres
      environment:
        - POSTGRES_DB=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
    web:
      build: .
      command: python manage.py runserver 0.0.0.0:8000
      volumes:
        - .:/code
      ports:
        - "8000:8000"
      depends_on:
        - db
```
---
#### プロジェクト作成
```
docker-compose run web django-admin startproject <プロジェクト名>
```

#### プロジェクト名/settings.pyを編集
settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

### Djangoの起動
```
docker-compose up -d 
```

#### Djangoのstartappをする
```
docker-compose run web python3 manage.py startapp <app名>
```