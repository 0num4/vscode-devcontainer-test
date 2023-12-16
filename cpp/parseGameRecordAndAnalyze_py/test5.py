import mahjongsoul_pb2
import json
import base64
from google.protobuf.descriptor import FieldDescriptor

def convert_json_to_protobuf(json_data, proto_class):
    if isinstance(proto_class, str):
        # プロトバフのクラス名が指定された場合は、そのクラスを取得
        proto_class = getattr(mahjongsoul_pb2, proto_class)
    proto_instance = proto_class()

    # JSON の各フィールドを確認
    for field_name, field_value in json_data.items():
        # プロトバフのフィールドディスクリプタを取得
        field = proto_instance.DESCRIPTOR.fields_by_name.get(field_name)
        if field:
            if field.type == FieldDescriptor.TYPE_BYTES:
                encoded_json_field_value = json.dumps(field_value).encode('utf-8')
                print(f"encoded_json_field_value: {encoded_json_field_value}")
                setattr(proto_instance, field_name, encoded_json_field_value)
            elif field.type == FieldDescriptor.TYPE_MESSAGE:
                # フィールドがメッセージ型の場合は再帰的に変換
                print(f"field.message_type.name: {field.message_type.name} field_name: {field_name}, field_value: f{field_value}")
                setattr(proto_instance, field_name, convert_json_to_protobuf(field_value, field.message_type.name))
            else:
                # それ以外の場合は値を直接設定
                print(f"field_name: {field_name}, field_value: {field_value}")
                setattr(proto_instance, field_name, field_value)

    return proto_instance

# JSON データ
json_data = {
    "name": "world",
    "data": {
        "bar": "baz",
        "qux": "quux"
    }
}

file = open("/workspaces/vscode-devcontainer-test/cpp/parseGameRecordAndAnalyze_py/paifu/mahjongsoul_paifu_231214-df604b7c-fc99-425c-8a3c-5ad0bed89a65.json", "r")
json_data = json.load(file)
# JSON データを Protobuf に変換
protobuf_data = convert_json_to_protobuf(json_data, mahjongsoul_pb2.ResGameRecord)

# 結果の確認
print(protobuf_data)
