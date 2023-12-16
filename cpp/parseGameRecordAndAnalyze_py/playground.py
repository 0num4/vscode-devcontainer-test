import glob

file_list = glob.glob("paifu/*")

# ファイル一覧を表示
for file_path in file_list:
    print(file_path)