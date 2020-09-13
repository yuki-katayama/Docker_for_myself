# Dockerのデータ管理
### volume
同じホスト内にあるコンテナでしか共有できない。
基本、移動や編集を行わない。 コンテナ上でファイルを管理するための機能。
コンテナを削除してもvolumeは残り続ける

+ volumeコマンド
```
docker volume <データベース名>
docker volume ls
docker volume inspect <データベース名>
docker volume rm <削除したいデータベース>
```

#### コンテナにvolumeをマウントする方法

--mount:
```
docker run -itd  --name <コンテナ名> --mount \
source=<マウント元のvolume名>,target=/<マウント先> nginx:latest
```

#### 読み取り専用でボリュームをマウントする場合
```
docker run -itd  --name <コンテナ名> --mount \
source=<マウント元のvolume>,target=<マウント先>,readonly nginx:latest
```
+ readonlyを付けるだけで良い



### bind mount
ホストのユーザーが管理しているファイルはディレクトリをコンテナ上にマウントする。
ホスト側で直接編集おっけー！
マウント元の領域は事前に用意しておく。

```
docker run -d -it --name devtest --mount \
type=bind,source="$(pwd)”/<マウント元のvolume>,target=/<マウント先> nginx:latest
```
