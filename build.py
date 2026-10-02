import os
import json

lessons = []
# 取得當前腳本所在資料夾的絕對路徑
base_dir = os.path.dirname(os.path.abspath(__file__))
lessons_dir = os.path.join(base_dir, "lessons")

print(f"Scanning directory: {lessons_dir}")

if os.path.exists(lessons_dir):
    for filename in os.listdir(lessons_dir):
        if filename.endswith(".json") or filename.endswith(".md"):
            filepath = os.path.join(lessons_dir, filename)
            print(f"Reading file: {filepath}")
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        if isinstance(data, list):
                            lessons.extend(data)
                        elif isinstance(data, dict):
                            lessons.append(data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

# 按 id 由大到小排序
lessons.sort(key=lambda x: int(x.get("id", 0)), reverse=True)

# 寫入 data.js
output_path = os.path.join(base_dir, "data.js")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"window.ALL_LESSONS_DATA = {json.dumps(lessons, ensure_ascii=False)};\n")

print(f"Successfully generated data.js with {len(lessons)} lessons.")
