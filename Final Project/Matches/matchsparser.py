import pandas as pd
import json
import os
from playwright.sync_api import sync_playwright

DEBUG_URL = "http://127.0.0.1:9222"


ids = pd.read_csv("remaining.csv")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(DEBUG_URL)
    context = browser.contexts[0]

    page = context.new_page()

    for match_id in ids["id"]:

        url = f"https://api.tracker.gg/api/v2/valorant/standard/matches/{match_id}"

        print(f"{match_id}")

        page.goto(url, wait_until="networkidle")

        text = page.text_content("body")

        with open(f"{match_id}.json", "w", encoding="utf-8") as f:
            f.write(text)
