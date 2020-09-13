## Docker Network
### ネットワークの種類
1. Bridgeネットワーク : 比較的小規模ネットワークにおすすめ。defaultではこの状態
2. None : ネットワークインターフェイスを元内
3. Hostネットワーク : ホストドライバーを使用。ホストネットワークでwebserverを構築した場合、ホストipで接続可能。なので、-pフラグを設定する必要がない 


#### 使用ネットワークの確認
```
docker network ls
```

#### ネットワークの詳細(<コンテナ名>でコンテナの詳細も見れる)
```
docker network inspect <ネットワーク名>
```

#### ネットワークとコンテナを接続
```
docker network connect <ネットワーク名> <コンテナ名>
```

#### ネットワークを作成(デフォルトはbridge)
```
docker network create <ネットワーク名>
```

#### 指定のネットワーク指定して起動
```
docker run -itd --name <任意のコンテナ名> —network <ネットワーク名> <イメージ名> /bin/sh
```

#### コンテナを指定のネットワークから切断
```
docker network disconnect <切断するネットワーク名> <切断するコンテナ名>
```