# 牌譜読み込んで煽りスタンプとか出すやつ

サブ目的: 牌譜と仲良くなる

ref:
https://github.com/0num4/paifu-playground/tree/main/protoc-study


* playground.py
この辺読みながら写経ついでにルールベース解析したやつ。主に煽り検知など。
https://wikiwiki.jp/majsoul-api/%E7%89%8C%E8%AD%9C%E3%82%92%E8%AA%AD%E3%82%80%E3%81%AB%E3%82%83#d5c53ae6

## 牌譜
* mahjongsoul_paifu_231214-df604b7c-fc99-425c-8a3c-5ad0bed89a65.json
    * cpu、半荘、四麻、絵文字
* mahjongsoul_paifu_230921-0a39a19b-4820-4b40-9fda-dd5481d023e4.txt
    * timpoにゃ普通の四麻段位
* mahjongsoul_paifu_230921-0a39a19b-4820-4b40-9fda-dd5481d023e4.txt
    * timpoにゃ普通の四麻段位

## protobuf関係
https://zenn.dev/hayato/articles/4f62385f672be5a79ab1#%E6%A8%99%E6%BA%96%E7%9A%84%E3%81%AA%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E6%96%B9%E6%B3%95
https://atsushi2022.hatenablog.com/entry/2022/11/20/015958

##
```proto
message ResGameRecord {
  Error error = 1;
  RecordGame head = 3;
  bytes data = 4;
  string data_url = 5;
}
<!-- 上のdataが -->
message GameDetailRecords {
  repeated bytes records = 1;
  uint32 version = 2;
  repeated GameAction actions = 3;
  bytes bar = 4;
}
```
