# protocpp

## protoc の format, lint などについて

https://qiita.com/yoheimuta/items/da7678fcd046b93a2637

- protoc-gen-lint
- prototool...https://github.com/yoheimuta/protolint インストールが楽（macbrew tap yoheimuta/protolint）
- buf

あたりが有名っぽい

mahjongsoul.proto の CustomizedContestManagerApi は admin api

```
vscode-devcontainer-test/cpp on  feat/protoc-cpp-init [!] via C on ☁️  r.oonuma@matsuri-tech.com
❯ go install github.com/ckaznocha/protoc-gen-lint@latest
go: downloading github.com/ckaznocha/protoc-gen-lint v0.3.0

```

## protolint

```
brew tap yoheimuta/protolint
brew install protolint

vscode-devcontainer-test/cpp on  feat/protoc-cpp-init [!?] via C v15.0.0-clang on ☁️  r.oonuma@matsuri-tech.com
❯ protolint lint mahjongsoul.proto 2>&1 | wc -l
     500

vscode-devcontainer-test/cpp on  feat/protoc-cpp-init [!?] via C v15.0.0-clang on ☁️  r.oonuma@matsuri-tech.com
❯ protolint lint protocol.proto 2>&1 | wc -l
     594
```

## proto-gen-lint

必ず option go_package = "github.com/yourusername/yourrepo/your_package";を指定しろって言われる。。。

```
❯ protoc --lint_out=. ./protocol.proto
protoc-gen-lint: unable to determine Go import path for "protocol.proto"

Please specify either:
        • a "go_package" option in the .proto source file, or
        • a "M" argument on the command line.

See https://developers.google.com/protocol-buffers/docs/reference/go-generated#package for more information.

--lint_out: protoc-gen-lint: Plugin failed with status code 1.
```

とりあえず go_package を指定してみたら動いた

```
option go_package = "./";

protocol.proto:5453:7: 'startObserve' - Use CamelCase (with an initial capital) for RPC method names.
protocol.proto:5454:7: 'stopObserve' - Use CamelCase (with an initial capital) for RPC method names.
--lint_out: encountered lint errors: 310 total

vscode-devcontainer-test/cpp on  feat/protoc-cpp-init [!] via C v15.0.0-clang on ☁️  r.oonuma@matsuri-tech.com
❯ protoc --lint_out=. ./protocol.proto
```

## buf

インストール楽そう
https://qiita.com/taisei_otsuka/items/78d49f03536086944d07
