import os
import json

lessons = []
base_dir = os.path.dirname(os.path.abspath(__file__))

# 搜尋 lessons 資料夾（相容大小寫與全目錄掃描）
for root, dirs, files in os.walk(base_dir):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.json') and file != 'package.json':
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        if isinstance(data, list):
                            lessons.extend(data)
                        elif isinstance(data, dict):
                            lessons.append(data)
            except Exception as e:
                print(f"Error reading {file}: {e}")

# 按 ID 由大到小排序
lessons.sort(key=lambda x: int(x.get("id", 0)), reverse=True)

# 關鍵修復：使用 json.dumps 確保 JSON 格式完全轉義無語法錯誤，並掛載至 window
json_str = json.dumps(lessons, ensure_ascii=False)
output_path = os.path.join(base_dir, "data.js")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"window.ALL_LESSONS_DATA = {json_str};\n")

print(f"Successfully generated data.js with {len(lessons)} lessons.")
