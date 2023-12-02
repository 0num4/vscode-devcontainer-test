
getProto:
	echo "hello"

# https://github.com/Cryolite/kanachan/blob/main/.devcontainer/post-create.sh#L159C22-L159C22
build:
	protoc -I. --cpp_out=. mahjongsoul.proto

lint:
	protolint lint -config_dir_path=. protocol.proto 2>&1 | wc -l