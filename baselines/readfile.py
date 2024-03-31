import json

# 打开 JSON 文件
with open('/Users/grace/Desktop/baselines/ref_dur_3_test_merge_1pspk_with_punc_refmeta_normwav_fix_refuid_new_diffprompt.json') as f:
    # 使用 json.load() 方法加载 JSON 数据
    data = json.load(f)

# 现在你可以访问 JSON 数据了
# print(data["test_cases"])

# print(type(data["test_cases"]))
# print(len(data["test_cases"]))

print(data["test_cases"][0])
print(type(data["test_cases"][0]))

for i in range(len(data["test_cases"])):
    print(data["test_cases"][i]['wav_path'])



