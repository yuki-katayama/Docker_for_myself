#### 起動中のコンテナを表示
```
docker ps
```

#### 全てのコンテナを表示
```
docker ps -a 
```

#### コンテナの停止 
``` 
docker stop コンテナ1ID コンテナ2ID 
```

#### 全てのコンテナを削除
```
docker rm -f $(docker ps -q -a)
```
+ docker psに -qをつけるとコンテナIDのみを抜き出せる

#### コンテナの生成/起動
```
docker run [オプション] イメージ名[:タグ名] [引数]
```

#### Runの工程を個別で行う
1. コンテナの作成
```
docker create —name <任意> -it イメージ名 /bin/sh
```

2. コンテナの起動
```
docker start コンテナ名
```

#### コンテナの一時停止/解除
  
```
docker pause コンテナ名
docker unpause コンテナ名
```

#### コンテナのシェルに接続
```
docker exec -it <コンテナ名 or ID> /bin/bash
```

#### Ubuntuコンテナの立ち上げ
```
docker run --name <任意の名前> -it -d ubuntu /bin/bash
```

#### コンテナからイメージを作成
```
docker commit <コンテナ名 or ID> <イメージ名>:<タグ名>
```

#### コンテナのIPアドレスを確認
 ```
Ip adds show
```
+ Attachで指定のコンテナに入った後に行う

#### Docker cpコマンド
```
docker cp <ホスト上のコピーしたいファイルのパス> \
<コンテナ名 or ID>:<コピー先のパス>
```
+ ホストのファイルをコンテナ内にコピー

#### コンテナ内のファイルをホストにコピー
```
docker cp <コンテナ名 or ID>:<コンテナ上のコピーしたいファイルのパス> <コピー先のパス>
```