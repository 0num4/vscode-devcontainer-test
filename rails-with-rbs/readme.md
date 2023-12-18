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
https://techlife.cookpad.com/entry/2020/12/09/120454
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
https://techlife.cookpad.com/entry/2020/12/09/120454
rbsファイルはじゃあ何という話ですが、特に何もない。
> RBS はそれ単体で何かをするものではなく *2 、Ruby 3 の型情報を扱うツールが共通で使いたくなるものを集めた gem になっています。この gem は Ruby 3 に同梱されます。しかし基本的には型解析ツール向けの gem であり、普通の Ruby プログラマは RBS 言語を読み書きすることはあっても、RBS gem を直接使うことはあまりないと思います。

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
コンソールにコードが出力される。
クラスだけじゃ分かりにくいかなと思ってsample.rbの関数にも型情報を消してtypeprofをかけてみたところ、定義だけかと思ったらそもそもクラスが作られた。
```
# TypeProf 0.21.8

# Classes
class Object
  private
  def add: (Integer a, Integer b) -> Integer
end
```

typeprofには引数を2つ渡して-vを付けることでエラーが出る可能性のあるところを示せる。
```
(base) root ➜ /workspaces/vscode-devcontainer-test/rails-with-rbs/rbssample (feat/rails-with-rbs2) $ typeprof sample.rb sample.rbs -v
# TypeProf 0.21.8

# Errors
sample.rb:5: [error] failed to resolve overload: Object#puts
sample.rb:2: [error] failed to resolve overload: Integer#+

# Classes
```
-oでrbsファイルとして出力出来る。
typeprof sample.rb -o sample.rbs

出力されたファイルはsteepで使える。生のrubyには型構造が無いので何も使えなさそう()
この記事を書いているときにcopilotがsorbetをサジェストしてくるんですがsteepはsorbetと同じ静的型検査機らしい。
```
gem 'steep', require: false

```
https://qiita.com/kettomorrow/items/8ccada8a4c9eac85b7ad
steepはsteep initしないと使えない。
steep initするとSteepfileが生成される。
慣習に倣ってsigファイルにrbsを格納してそこから読み取れるようにsteepfileを編集する。(コメントアウトを外す)
```
ここまで来て初めてsteep checkを走らせることが出来る。
```
(base) root ➜ /workspaces/vscode-devcontainer-test/rails-with-rbs/rbssample (feat/rails-with-rbs2) $ steep check
# Type checking files:

...................................................................................

No type error detected. 🍵
```
mochaのtestみたいなのが出力が出てきた。
sample.rbにエラーになるようにガチャガチャやってみたが関数などには効果がない？引数を変えたり新たなメソッドを足しても特にsteep checkはエラーにならなかった

次にsorbetを導入してみる。
```
gem 'sorbet', require: false
```
https://note.com/pharmax/n/naa573d13410d
sorbetはrubyの中に型アノテーションとして書けるらしい。

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
