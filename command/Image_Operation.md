#### イメージにタグ付け
```
docker tag <イメージ名> <新しいイメージ名>:<付けたいtag名>
```

#### イメージの詳細情報
```
docker inspect <イメージ名>
```

#### イメージファイル一覧
```
docker images
```

#### イメージファイルの削除 or 全削除
+ 削除
```
docker rmi -f <イメージ名> or <イメージID>
```
+ 全削除
```
docker rmi -f $(docker images -q)
```

#### イメージを取得(pull)
```
docker pull docker <イメージ名>
```

#### イメージのbuild
```
docker build -t <イメージ名> <docker-contextがあるディレクトリの場所>
```

#### イメージファイルのbuild(キャッシュ使用なし)
```
docker build --no-cache -t <イメージ名> <docker-contextがあるディレクトリの場所>
```
+ アップデートなどのコマンドがあった場合、dockerファイルの差分実行ではなく、毎度アップデートコマンドを使用したい時などに使用する