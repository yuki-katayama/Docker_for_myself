## Docker-machine
#### dockerホストの作成
```
docker-machine create <dockerホスト名>
```

#### 作成された/接続ホストの確認
```
docker-machine ls
```
* Activeの所に 「*」が付いている所が接続ホスト

#### Dockerホストの開始/終了
+ 
```
docker-machine start <ホスト名>
```

+ 
```
docker-machine stop <ホスト名>
```

#### ホストにsshで接続
```
docker-machine ssh <ホスト名>
```

#### ホストの削除
```
docker-machine rm <ホスト名>
```

#### 作成したdockerホストに接続可能にする
1. 
```
docker-machine env <接続するホスト名>
```
2. 記載されたコマンドを実行する 
```
eval $(docker-machine env ~)
```

#### 接続の解除
1. 
```
docker-machine env -u
```
2. 
```
eval $(~)
```
3. docker ls でActiveの「*」が消えている事で確認可能

#### 接続ホストのip確認
```
docker-machine ip ホスト名
```
+ docker-machine ls でURLの場所でも確認できる.