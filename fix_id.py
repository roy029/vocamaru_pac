import jsonlines

input_file = "replace_vocab_table/miss_mt5_replace_desc_table5000.jsonl"
output_file = "replace_vocab_table/mt5_replace_desc_table5000.jsonl"

# 新しい"id"値の初期値
new_id = 0

with jsonlines.open(input_file) as reader, jsonlines.open(output_file, mode='w') as writer:
    for obj in reader:
        obj['id'] = new_id  # "id"を新しい値に書き換える
        writer.write(obj)  # 書き換えたオブジェクトを出力ファイルに書き込む
        new_id += 1  # 新しい"id"値をインクリメントする

# with open("empty20k.txt", "w") as file:
#     for idx in range(21000):
#         data = f'▁<empty_{idx}>'
#         file.write(data + "\n")