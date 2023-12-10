# vscode-devcontainer-test

This is a test repository for VSCode Dev Container.
https://blog.kinto-technologies.com/posts/2022-12-10-VSCodeDevContainer/

今年の5月に大分変わってそう
https://zenn.dev/newgyu/scraps/4c24bf3df804bd

## featuresについて

Rebuild Containerしないとfeaturesは入らない。Reopenだけでは入らない。
```
	"features": {
		"ghcr.io/devcontainers/features/ruby": {}
	}
```

	    "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {}
を追加するとdockerコマンドがインストールされる。
https://github.com/devcontainers/features/tree/main/src/docker-outside-of-docker
https://qiita.com/t_katsumura/items/d5be6afadd6ec6545a9d
別にdindでもいい気がするけどね

devcontainer上でdocker psすると一番外側のdocker psになっており、自分自身(devcontainer)が見えたのでdoodになっている。
```
vscode ➜ /workspaces/vscode-devcontainer-test $ docker ps
CONTAINER ID   IMAGE                                                                                           COMMAND                  CREATED         STATUS         PORTS     NAMES
3d8786ddc6ba   vsc-vscode-devcontainer-test-bd0ab0b712e5c3240d4add4fdc1b4eaa0e94d8228bb3d99bd0c49ec87c2a22c5   "/bin/sh -c 'echo Co…"   7 minutes ago   Up 7 minutes             wizardly_mcclintock
```


# memo

reopen container を選ぶと.devcontainer に Dockerfile と devcontainer.json ができる。
時間はかかるが勝手にdevcontainerが立ち上がる。
ctrl+jとかすると勝手にコンテナ内部に入ってcondaもactivateされる。


# coderabbitについて

coderabbitAIとoss版のcode rabbitがある

## branch protection ruleについて
管理者は普通にprotectionをしてもpush出来てしまうらしい
https://zenn.dev/snowcait/articles/42bb6b56c806da

# ai-pr-reviewer
https://github.com/coderabbitai/ai-pr-reviewer/pull/494
github-actions[bot]でcoderabbitを呼び出してる

https://github.com/keshav-infracloud/coderabbit-test/pull/8
この辺の設定とか参考になりそう

## vscodeのcpp設定
https://qiita.com/yut-nagase/items/ced10f952b74f115c733

## protobufの設定など

https://vscode.dev/github/0num4/kanachan/blob/majsoul-proto/mjai.app/Dockerfile#L33

aptからインストールするprotobuf-compilerとlibprotobuf-devが単純に壊れていて下記のようなエラーが出る
```
In file included from /workspaces/vscode-devcontainer-test/cpp/main.cpp:2:
/workspaces/vscode-devcontainer-test/cpp/mahjongsoul.pb.h:26:10: fatal error: google/protobuf/generated_message_bases.h: No such file or directory
   26 | #include <google/protobuf/generated_message_bases.h>
```

実際`dpkg -L libprotobuf-dev`などでインストールされるheaderファイルを見ても無い。終わっている。
ということでソースからインストールするしかないのでインストールする。

https://github.com/protocolbuffers/protobuf/tree/main/src

### bazelのインストールする

普通にcppでもインストール出きるっぽい
https://github.com/protocolbuffers/protobuf/tree/main/src

```
sudo apt install apt-transport-https curl gnupg -y
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
sudo mv bazel-archive-keyring.gpg /usr/share/keyrings
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
```

bazelはこけるがcmakeは動く
```

 cmake --build .

 [100%] Building C object third_party/utf8_range/CMakeFiles/utf8_range.dir/range2-sse.c.o
[100%] Linking C static library libutf8_range.a
[100%] Built target utf8_range
```