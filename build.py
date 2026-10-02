import os
import json

lessons = []

# 掃描 lessons 資料夾裡的所有檔案
lessons_dir = "lessons"
if os.path.exists(lessons_dir):
    for filename in os.listdir(lessons_dir):
        if filename.endswith(".json") or filename.endswith(".md"):
            filepath = os.path.join(lessons_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        lessons.extend(data)
                    elif isinstance(data, dict):
                        lessons.append(data)
                except Exception as e:
                    print(f"Error reading {filename}: {e}")

# 按 ID 由大到小排序
lessons.sort(key=lambda x: x.get("id", 0), reverse=True)

# 寫入 data.js
with open("data.js", "w", encoding="utf-8") as f:
    f.write(f"window.ALL_LESSONS_DATA = {json.dumps(lessons, ensure_ascii=False, indent=2)};")

print(f"Successfully generated data.js with {len(lessons)} lessons.")
