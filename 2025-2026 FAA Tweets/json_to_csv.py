import json
import pandas as pd

with open("2025-2026 FAA Tweets/tweets_updated.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.json_normalize(data)
df.to_csv("2025-2026 FAA Tweets/tweets_updated.csv", index=False)