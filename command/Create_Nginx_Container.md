### Nginxのコンテナ立ち上げ
```
docker run --name<コンテナ名> (—rm) -d\
	-p <ホスト側のポート番号>:<コンテナ側のポート番号>\
	<イメージ名>
```
#### 解説
+ --nameは起動するコンテナに任意の名前をつける
+ —rm コンテナ終了時にコンテナを削除
+ -d　デタッチモード(コンテナ立ち上げをバックグラウンドで行う)を行う。これにより、実行中もコマンド操作が可能になる。
+ <>:<> ホスト側のポート番号にアクセスすれば、コンテナ側のポート番号にアクセスできる。

#### 例 
```
docker run --name some-nginx -d -p 8080:80 some-content-nginx
```

### Nginx バインドマウントを使用

```
docker run —name <コンテナ名> -d\
	-v <ホスト側ディレクトリ>:<コンテナ側のマウントポイント>:<オプション>\
	-p <ホスト側のポート番号>:<コンテナ側のポート番号>\
	<イメージ名>
```
#### 解説
+ -v <コンテナにマウントするホストのディレクトリ> :
+ <マウント先コンテナのディレクトリ> :
+ <roの場合(読み取り専用 read-only)>

>#### MACの場合の -v (例)
>> -v /Users/<ユーザー名>/docker-tutrial/html:/usr/share/nginx/html:ro
#### コード例

```
docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d -p 8080:80 nginx
```
