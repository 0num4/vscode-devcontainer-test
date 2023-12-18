# README

## rails-with-rbs
https://qiita.com/kaishuu0123/items/2a91495e7daa8c7783ed
```
bundle init
# gemfileを編集
bundle install
bundle exec rails .
bundle exec rails s
```

https://karlley.hatenablog.jp/entry/2023/05/20/095016
rails newは勝手にgit repoを作ってしまうので、
rm -rf .gitで消す。
rails new -Gでも同じ効果が得られる。

## rails
https://tech.medpeer.co.jp/entry/2023-small-rbs-introduce
頑張らずに型を導入していこうな
rbsを導入して
```
gem 'rbs', require: false
bundle install
```

これでrbsコマンドが使えるようになります。

```
rbs collection init
```
rbs_collection.yamlというファイルが生成されます。

___

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...
