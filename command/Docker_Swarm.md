# Docker Swarm
#### Swarmで使用されるポート番号
+ クラスタ管理通信用 : TCP 2377
+ ノード間通信用 : TDP/ UDP 7946
+ オーバーレイネットワークトラフィック用:UDP 4789

### ノード作成
1. envでアクセスする。
2. docker infoでIPを確かめる (他のノードと通信可能なIP)
3. 
```
docker swarm init --advertise-add <2.で見たIP>
```
 + swarm initでswarmモードがactiveになり、自動的にmanagerノード and workerモードとして扱われる。
4. To add a worker to this swarm, run the following command:
```
docker swarm join-token (manager or worker)
docker swarm join --token <token> <IP>
```
 + これでクラスタの選択したノードを追加する事が可能
5. 
```
docker node ls
```
 + 追加後は、managerノードに行き、このコマンドで実行できる。

#### ノードをworkerからmanagerに昇格させたい場合
```
docker node promote <昇格させたいノード>
```

#### Swarmの構成を可視化する。
```
docker run -d --name=viz --publish=8080:8080/tcp \
--mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
dockersamples/visualizer
```
+ これで、managerコンテナのIP:8080で可視化できる。

#### ネットワークIDの確認
```
docker-machine ip <network-name>
```

#### サービス作成
+ 通常一つのノードに一つのタスク
```
docker service create -d --name <サービス名> \ 
--replicas <タスク数> --publish <設定したいポート名> (例:8000:80) nginx
```
+ これにより、タスク数のノードにnginxコンテナがランダムに作成される

#### 指定したノードにコンテナを配置したい場合
```
docker service create --name nginx --constraint \
'node.role==<ノードID or ノードホスト名>’ \ 
--replicas <サービス数> --detach=true nginx
```
#### serviceコマンド
```
docker-machine ls
```
+ 各ネットワークのアドレスがわかる

---
```
docker service ls
```
+ 作成しているサービスを表示
 docker service ps　<サービス名>
	各サービスでのタスクを表示
---
#### 追加で開放するポートを設定する場合
```
docker service update \ 
--publish-add 8000:80 --detach=true <ポートを設定するサービス名>
```

#### サービスに行なった作業を一つ戻す(ロールバック)
```
docker service rollback --detach=true <サービス名>
```
+ 二回行うと元に戻る

#### ポート設定を消す場合
```
docker service update --publish-rm <接続しているポート> --detach=true <サービス名>
```

#### サービスの詳細
```
docker service inspect --pretty <サービス名>
```
+ --pretty : 読みやすい状態にしてくれる

#### ルーティングメッシュ
```
docker service create --name \ host-nginx \
--publish mode=host,published=8000,target=80 --replicas 2 nginx
```
+ mode=host : 各ノードに個別に指示を行える
+ docker-machine attach タスク(コンテナ)idで確認できる

#### グローバルモード
```
docker service create --name web --mode global nginx
```
+ replicasの指定はいらない
+ 格ノードに一つ一つずつタスクが実行されている
	
## Docker swarmの可用性
マネージャーノードが停止した場合、他のマネージャーノードで補完する場合,マネージャーノードの数:
```
停止が許容される数 = (N - 1) / 2個
例). N = 5 なら、2台停止しても継続可能
```
---
#### タスク数を増やす/減らす
```
docker service scale <サービス名>=<タスクの数>
```
+ タスク数には既存のタスクも含まれる

#### タスクの再配置
```
docker service update —force <サービス名>
```
+ Stop→startなどで普及したノードには、タスクが割り当てられていないので、タスクの再配置ができる.