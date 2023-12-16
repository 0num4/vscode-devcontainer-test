import json
import mahjongsoul_pb2
from google.protobuf import json_format
from google.protobuf import text_format
# from typing import List, Dict
from typing import *

# import protocol_pb2
# 2個importすると被る

wrapper_mjsoul = mahjongsoul_pb2.Wrapper()
testItemData = mahjongsoul_pb2.Item()
# wrapper_protocol = protocol_pb2.Wrapper()

testItemData.item_id = 1
testItemData.stack = 2
testItemDataString =  testItemData.SerializeToString()

testItemDataJson = json_format.MessageToJson(testItemData)
# print(testItemDataJson)
testItemDataText = text_format.MessageToString(testItemData)
# print(testItemDataText)
jsonItemData: Dict[str,int] = {
  "itemId": 1,
  "stack": 2
}
testItemData2 = mahjongsoul_pb2.Item()
testItemDataJSONString = json_format.Parse(json.dumps(jsonItemData), testItemData2, ignore_unknown_fields=True)
print(testItemData2)

# def main():
#     # f = open('paifu/mahjongsoul_paifu_230921-2e8495ad-c9df-4b0f-9f10-dd354b9daeeb.txt', 'rb')
#     # wrapper_mjsoul.ParseFromString(f.read())
#     # print(f.read())
#     # f.close()
# main()