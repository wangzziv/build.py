import os
import json

lessons = []
base_dir = os.path.dirname(os.path.abspath(__file__))

print("=== Starting build.py ===")
print(f"Base Directory: {base_dir}")

# 1. 搜救邏輯：掃描全專案目錄下的所有 .json 檔案（不論資料夾大小寫）
for root, dirs, files in os.walk(base_dir):
    # 忽略 .git 和 .github 目錄
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.json') and file != 'package.json':
            filepath = os.path.join(root, file)
            print(f"Found JSON file: {filepath}")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        if isinstance(data, list):
                            lessons.extend(data)
                        elif isinstance(data, dict):
                            lessons.append(data)
                        print(f"Successfully loaded data from {file}")
            except Exception as e:
                print(f"Error reading {file}: {e}")

# 2. 依照 ID 排序（防呆轉 int）
lessons.sort(key=lambda x: int(x.get("id", 0)), reverse=True)

# 3. 強制寫入 data.js
output_path = os.path.join(base_dir, "data.js")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"window.ALL_LESSONS_DATA = {json.dumps(lessons, ensure_ascii=False)};\n")

print(f"=== Successfully written {len(lessons)} lessons to data.js ===")
