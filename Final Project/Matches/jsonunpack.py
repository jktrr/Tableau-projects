import pandas as pd
import json
import os
from pathlib import Path

df = pd.read_csv("all_matches.csv")
ids = pd.read_csv("GameID.csv")

id_list = []
i = 0

for match_id in ids["id"]:
    id_list.append(match_id)

for _, row in df.iterrows():
    match_id = id_list[i]
    json_text = row["json"]
    i += 1

    if Path(f"{match_id}.json").is_file():
        continue

    try:
        data = json.loads(json_text)

        with open(f"{match_id}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"{match_id}.json")

    except Exception as e:
        print(f"Failed for {match_id}: {e}")
