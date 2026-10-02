import os
import json

lessons = []
lessons_dir = "lessons"

if os.path.exists(lessons_dir):
    for filename in os.listdir(lessons_dir):
        if filename.endswith(".json") or filename.endswith(".md"):
            filepath = os.path.join(lessons_dir, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    # 自動相容沒有包括號的 json 物件或陣列
                    data = json.loads(content)
                    if isinstance(data, list):
                        lessons.extend(data)
                    elif isinstance(data, dict):
                        lessons.append(data)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

# 依照 id 排序（由大到小）
lessons.sort(key=lambda x: int(x.get("id", 0)), reverse=True)

# 寫入 data.js
with open("data.js", "w", encoding="utf-8") as f:
    f.write(f"window.ALL_LESSONS_DATA = {json.dumps(lessons, ensure_ascii=False)};\n")

print(f"Successfully generated data.js with {len(lessons)} lessons.")
