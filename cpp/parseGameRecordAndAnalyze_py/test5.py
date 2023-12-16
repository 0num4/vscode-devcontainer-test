import mahjongsoul_pb2
import json
import base64
from google.protobuf.descriptor import FieldDescriptor

def convert_json_to_protobuf(json_data, proto_class):
    proto_instance = proto_class()

    # JSON の各フィールドを確認
    for field_name, field_value in json_data.items():
        # プロトバフのフィールドディスクリプタを取得
        field = proto_instance.DESCRIPTOR.fields_by_name.get(field_name)
        if field:
            if field.type == FieldDescriptor.TYPE_BYTES:
                encoded_json_field_value = json.dumps(field_value).encode('utf-8')
                print(encoded_json_field_value)
                setattr(proto_instance, field_name, encoded_json_field_value)
            else:
                # それ以外の場合は値を直接設定
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

# JSON データを Protobuf に変換
protobuf_data = convert_json_to_protobuf(json_data, mahjongsoul_pb2.Wrapper)

# 結果の確認
print(protobuf_data)
