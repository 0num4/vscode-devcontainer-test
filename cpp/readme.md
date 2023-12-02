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
