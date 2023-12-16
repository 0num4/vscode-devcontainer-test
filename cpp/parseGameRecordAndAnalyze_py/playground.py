import glob
import json
file_list = glob.glob("paifu/*")

def tokusyusousa(type):
    if type != 1 and type != 2:
        print(f"特殊操作にゃ！{type}")

def parseFile(file_path):
    print(file_path)
    json_data = json.load(open(file_path, "r"))
    if json_data["head"]["config"]["category"] == 1:
        print("友人戦")
    elif json_data["head"]["config"]["category"] == 2:
        print("段位戦")
    
    if json_data["head"]["config"]["mode"] == 1:
        print("東風")
    elif json_data["head"]["config"]["mode"] == 2:
        print("半荘")
    # 4麻か3麻か
    results = json_data["head"]["result"]["players"]
    print(f"{len(results)}麻")

    actions = json_data['data']['data']['actions']
    sorted_actions = sorted(actions, key=lambda x: x['passed'])
    for i, action in enumerate(sorted_actions):
        elapsed_time = action['passed'] - sorted_actions[i - 1]['passed'] if i > 0 else action['passed']
        # print(f"前のイベントから{elapsed_time/1000}秒経ったよ")
        # print(f"{i}番目のアクション")
        if action["type"] == 1:
            # print(action["result"]["name"])
            if action["result"]["name"] == ".lq.RecordHule":
                # print(f"{elapsed_time/1000} ロンにゃ！ {action['result']['data']}")
                for fule in action['result']['data']['hules']:
                    print(f"{elapsed_time/1000} 他家のロン/ツモにゃ！ {fule['seat']}({'親' if fule['qinjia'] else '子'})が{fule['hu_tile']}で{'ツモ' if fule['zimo'] else 'ロン'}にゃ！{fule['count']}翻にゃ！")
            pass
        elif action["type"] == 2:
            if action['user_input']['type'] == 1:
                print(f"{elapsed_time/1000} スタンプを打ったにゃ！{action['user_input']['emo']}")
            elif action['user_input']['type'] == 2:
                tokusyusousa(action['user_input']['type'])
                # print(f"{elapsed_time/1000} {action['user_input']['operation']}")
                time_use = action['user_input']['operation'].get('timeuse')
                operation_tile = action['user_input']['operation'].get('tile')
                if time_use == 1000000:
                    print(f"特殊操作にゃ！多分時間切れにゃ！")
                    print(f"{elapsed_time/1000} 特殊操作にゃ！{action['user_input']['operation']}")
                    continue
                if action['user_input']['operation']["type"] == 1:
                    print(f"{elapsed_time/1000} ここは{operation_tile}とするにゃ！この牌は{'モギリ' if action['user_input']['operation']['moqie'] == True else 'モギらない'}にゃ！ 使った時間は{time_use}秒にゃ！")
                    if time_use > 5:
                        print("煽りにゃ！？")
                elif action['user_input']['operation']["type"] == 7:
                    print(f"{elapsed_time/1000} 立直にゃ！")
                elif action['user_input']['operation']["type"] == 11:
                    print(f"{elapsed_time/1000} ぺーにゃ！")
                elif action['user_input']['operation']["type"] == 4:
                    print(f"{elapsed_time/1000} カンにゃ！(暗槓) {operation_tile} 使った時間は{time_use}秒にゃ！")
                elif action['user_input']['operation']["type"] == 6:
                    print(f"{elapsed_time/1000} カンにゃ！(加槓) {operation_tile} 使った時間は{time_use}秒にゃ！")
                elif action['user_input']['operation']["type"] == 8:
                    print(f"{elapsed_time/1000} ロン/ツモにゃあ～！！！ 使った時間は{time_use if time_use is not None else '自動和了'}秒にゃ！")
                elif action['user_input']['operation']["type"] == 2:
                    print(f"{elapsed_time/1000} 操作キャンセルにゃ！ 使った時間は{time_use}秒にゃ！")
                else:
                    print(f"{elapsed_time/1000} 不明な操作にゃ！ {action['user_input']['operation']} 使った時間は{time_use}秒にゃ！")
            elif action['user_input']['type'] == 3:
                print(f"{elapsed_time/1000} CPGにゃ！ {action['user_input']['cpg']}")
            elif action['user_input']['type'] == 4:
                pass # 存在しない
            elif action['user_input']['type'] == 5:
                print(f"{elapsed_time/1000} 1局が終了し、次局の準備ができたときにゃ!")
            elif action['user_input']['type'] == 6:
                print(f"{elapsed_time/1000} 離席から戻り、操作再開したときにゃ！")
            elif action['user_input']['type'] == 7:
                print(f"{elapsed_time/1000} 対局を開始するときにゃ！")
            elif action['user_input']['type'] == 8 or 9:
                print(f"{elapsed_time/1000} 他家が回線落ち/回線復帰したときにゃ！")
        elif action["type"] == 3:
            if action["user_event"]["type"] == 1:
                if i < 10:
                    continue # 最初の接続イベントは無視
                print(f"{elapsed_time/1000} 回線復帰にゃ！どうしたにゃ？")
            elif action["user_event"]["type"] == 2:
                print(f"{elapsed_time/1000} 回線落ちにゃ～～～！死刑にゃ！")
        elif action["type"] == 4:
            if action["game_event"] == 1:
                print("ゲーム開始にゃ！")
            else:
                print(f"{elapsed_time/1000} ゲーム終了にゃ！お疲れさまでした～")
        else:
            print("不明なアクションにゃ！")


for file_path in file_list:
    parseFile(file_path)