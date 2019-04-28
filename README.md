# docker-nginx-uwsgi-bottle

よく忘れる構成を雛形にした

client -> [nginx] -> (tcp socket) -> [uwsgi -> bottle framework]

[ ]の箇所が構築対象のコンテナ

## 使い方
* ローカルに持ってくる

`$ git clone https://github.com/takesaki/docker-nginx-uwsgi-bottle.git`

* dockerコンテナとして起動

`$ docker-compose up`

* ブラウザから以下にアクセス

http://[ip]:8800/      (nginxが応答)

http://[ip]:8800/test  (uwsgiが応答)


