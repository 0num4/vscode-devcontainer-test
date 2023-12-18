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
https://note.com/fukurou_dev/n/n5bc20a87bf01
https://tech.medpeer.co.jp/entry/2023-small-rbs-introduce
頑張らずに型を導入していこうな

railsにおいて型(rbs)の導入には5つの方法がある。
* gem_rbs_collectionや各gemに登録されている型を取得する
* pocke/rbs_railsなどによる型の自動生成
* typeprofによる型の自動生成
* rbs prototypeによる型のプロトタイプの自動生成
* 自分で型を書く

openapiから型を生成する方法もありそう。

型を導入したら当たり前だが型を活用する必要がある。
* steeep
* sorbet
* rbspy
* katakataIrb
* コーディング時の型強化

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
rbs_collection.yamlはどこから型情報を持ってくるかなどが定義されているみたい。
ビルドイン関数やビルドインライブラリには型がないらしい(python流煽り)

この時点で型を補完したrbファイルを作ってrubyコマンドで実行すると、壊れた。
```
def add(a: Integer, b: Integer) -> Integer
    return a + b
end
  
puts add(1, 2)
# syntax errorが出る
```
次にtypeprofを導入してみた
```
gem 'typeprof', require: false
bundle install
```
これでtypeprofコマンドが使えるようになる。
https://note.com/fukurou_dev/n/n5bc20a87bf01
ここで紹介されているようなコード持ってきて、これにtypeprofをかけてみる。
```
(base) root ➜ /workspaces/vscode-devcontainer-test/rails-with-rbs/rbssample (feat/rails-with-rbs2) $ typeprof  typeprofTest.rb 
# TypeProf 0.21.8

# Classes
class Information
  @animal: untyped
  @height: untyped

  def initialize: (animal: untyped, height: untyped) -> void
end
```
コンソールにコードが出力される
```
```

```
rbs prototype init
```



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
