import os
import json

lessons = []
base_dir = os.path.dirname(os.path.abspath(__file__))

# 搜尋 lessons 資料夾（相容大小寫）
target_dir = None
for item in os.listdir(base_dir):
    if item.lower() == "lessons" and os.path.isdir(os.path.join(base_dir, item)):
        target_dir = os.path.join(base_dir, item)
        break

print(f"Target lessons directory: {target_dir}")

if target_dir:
    for filename in os.listdir(target_dir):
        if filename.endswith(".json") or filename.endswith(".md"):
            filepath = os.path.join(target_dir, filename)
            print(f"Processing file: {filepath}")
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

# 按 ID 由大到小排序
lessons.sort(key=lambda x: int(x.get("id", 0)), reverse=True)

# 寫入 data.js
output_path = os.path.join(base_dir, "data.js")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"window.ALL_LESSONS_DATA = {json.dumps(lessons, ensure_ascii=False)};\n")

print(f"Successfully generated data.js with {len(lessons)} lessons.")
