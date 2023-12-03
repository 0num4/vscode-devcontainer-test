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