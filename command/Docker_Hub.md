#### Docker hubにログイン
```
docker login
```
#### Docker Hubでのタグ付け
```
docker tag <イメージ名> <docker_hubに置くイメージ名(<DockerID>/<イメージ名>:<タグ名>)>
```

#### Docker Hubにイメージをpush
```
docker push <DockerID>/<イメージ名>:<タグ名>
```

#### イメージをbuild
```
docker run --name ~
```
 + 自動的にdocker_hubを探しに行く

 ## 自動ビルド(githubから)
Docker hubにgitリポジトリと連携したリポジトリを作成しておく

#### 作成したDockerfileをgitリポジトリに追加
1. git add .
2. git commit -m “message”
3. git push origin master

すると、自動的にbuildが行われ、tagsの場所にpullコマンドが書いてあるので、それを実行すると、imageがローカルにpullされる。