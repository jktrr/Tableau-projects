import json
import os
import pandas as pd
from pathlib import Path

riot = "BRT CauliDerp#ecchi"

os.makedirs("my_stats", exist_ok=True)

for filename in os.listdir("matches_json"):
    output = f"my_stats/{filename.removesuffix('.json')}_p.csv"

    if not filename.endswith(".json") or os.path.exists(output):
        continue

    stats = []

    with open(os.path.join("matches_json", filename), encoding="utf-8") as f:
        data = json.load(f)

    for stat in data["data"]["segments"]:
        if stat.get("attributes").get("platformUserIdentifier") == riot and (stat.get("type") == "player-loadout" or stat.get("type") == "player-summary"):
            stats.append(stat)

    df = pd.json_normalize(stats)
    df.to_csv(f"my_stats/{filename.removesuffix('.json')}_p.csv",
              index=False)
