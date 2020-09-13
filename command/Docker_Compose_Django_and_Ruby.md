# Docker Compose(Django)
1. Dockerfileか、image(docker hubなどに)を用意する.
2. docker-compose.ymlを定義する
3. docker-compose up -d を実行する

## Djangoの環境を構築する
+ 参考 : https://docs.docker.com/compose/django/
+ 完成版 : https://github.com/yuki-katayama/Docker_for_myself/tree/master/django

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

## Ruby on Rails の環境を構築する
+ 参考 : https://docs.docker.com/compose/rails/
+ 完成版 :

Dockerfile
```
FROM ruby:2.5
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
RUN mkdir /myapp
WORKDIR /myapp
COPY Gemfile /myapp/Gemfile
COPY Gemfile.lock /myapp/Gemfile.lock
RUN bundle install
COPY . /myapp
```
---
docker-compose.yml
```
version: '3'
services:
  db:
    image: postgres
    volumes:
      - ./tmp/db:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: password
  web:
    build: .
    command: bash -c "rm -f tmp/pids/server.pid && bundle exec rails s -p 3000 -b '0.0.0.0'"
    volumes:
      - .:/myapp
    ports:
      - "3000:3000"
    depends_on:
      - db
```
---
Gemfile
```
source 'https://rubygems.org'
gem 'rails', '~>5'
```
---
Gemfile.lock
```
touch Gemfile.lock
```

### プロジェクトを作成する
```
docker-compose run web rails new . --force --no-deps --database=postgresql
```

#### config/database.ymlの設定
追加
```
default: &default
  adapter: postgresql
  encoding: unicode
  host: db
  username: postgres
  password: password
```

#### 起動
```
docker-compose up
```
---
### エラー対処
*エラーメッセージ*
 ```
Could not find public_suffix-4.0.6 in any of the sources
Run `bundle install` to install missing gems.
```
##### キャッシュで bundle install が実行されない場合があるっぽい！
```
docker-compose build --no-cache 
```
を実行する
### データベース作成
```
docker-compose run web rake db:create
```
### Scaffoldにて簡易的なアプリケーション作成(ユーザー名を管理する)
```
docker-compose run web bin/rails g scaffold User name:string
```
```
docker-compose run web bin/rails db:migrate
```
