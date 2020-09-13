# マルチホストネットワーク
### キーバリューストア
クラスタの状態管理
### Swarmクラスタ内
##### コンテナ間通信可能: オーバーレイネットワーク
+ master ノード : クラス全体の管理機能を持っている 
+ agent　ノード : 管理機能を持っていない

#### キーバリューストアの作成
---
```
docker run -d --name consul -p 8500:8500 \
-h consul consul agent -server -bootstrap -client 0.0.0.0
```
+  Consulイメージからconsulコンテナを-dで起動
+ -p 8500:8500 : 8500番ポートを使用
+ -h consul : ホスト名をconsulで指定
+ consul agent ~ : consulコンテナで実行するコマンド
+ -server : サーバーモードのエージェントを起動
+ -bootstrap : リーダーが一台だけで構成される場合、起動した鯖がリーダーになる
+ -client ~ : consulへ問いつける鯖ipを指定

#### swarm内のmasterノードの作成
---
``` 
docker-machine create --swarm --swarm-master \
--swarm-discovery="consul://$(docker-machine ip mh-keystore):8500" \
--engine-opt="cluster-store=consul://$(docker-machine ip mh-keystore):8500" \
--engine-opt="cluster-advertise=eth1:2376" \
mhs-demo0
```
+ --swarm : 作成するホストをswamクラスターに追加
+ --swarm-master : swarmクラスター内の管理ノードとして設定
+ --swarm-discovery ~ : swarmにおいて使用されるキーバリューストアの場所
+ --engine-opt=“cluster-store ~” : オーバーレイネットワーク用に使用されるキーバリューストア
+ --engine-opt=“cluster-advertise~” : 他のホストのdockerデーモンとの繋がりにどのネットワークインターフェイスのどのポートを使用するかを指定
+ mhs-demo0 : ホスト名

#### Agentノードの作成
---
これは、masterノードの作成のコマンドから--swarm-masterを取り除いて、別のホスト名にするだけで良い

#### オーバーレイネットワークの構築
---
1. 操作対象をswarmのマスターノード
```
eval $(docker-machine env --swarm mhs-demo0)
```
 + --swarmをつける事で、dockerコマンドの情報がswarmの情報のみに制限される

2. オーバーレイネットワークの構築
```
docker network create --driver overlay --subnet=10.0.9.0/24 mh-net
```
 + ovelayドライバーを使用したmh-netのネットワークが作成される

3. ネットワークの起動 
```
docker run -itd --name web --network mh-net --env \ 
“constraint:node==mhs-demo0” nginx
```
 + --env “constraint:node==mhs-demo0 : クラスタ内のmhs-demo0ノードでコンテナ起動
 + もしこれがない場合、クラスタ内のどこかのコンテナで起動される
	—network mh-net : 作成したoverlayネットワークで接続 

4. 確認方法
mhs-demo1ネットワーク内で
```
docker run -it --rm --network mh-net --env \
 ”constraint:node==mhs-demo1” busy box wget -O- http://web
```
 + ”constraint:node==mhs-demo1” : エージェントノードでコンテナ起動を指示
 + busy box wget -O- http://web : マスターノードのコンテンツを取得
 + wget : マスターノードで起動した nginx のコンテンツを取得
 + -0- : 取得したコンテンツを標準出力する