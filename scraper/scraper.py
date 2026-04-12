import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# =========================
# TARGET DATA
# =========================
TARGET_DATA = 250  # bisa ubah 200–300

# =========================
# CONNECT KE CHROME (SUDAH LOGIN)
# =========================
options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

# =========================
# KEYWORD MBG
# =========================
queries = [
    "MBG",
    "makan bergizi gratis",
    "program makan gratis indonesia",
    "kebijakan makan gratis"
]

# =========================
# MODE TAB
# =========================
tabs = ["top", "live"]  # top = populer, live = terbaru

all_data = []
seen_tweets = set()

# =========================
# FUNCTION SCROLL & SCRAPE
# =========================
def scrape_current_page(query, tab):
    global all_data

    scroll_count = 0

    while len(all_data) < TARGET_DATA and scroll_count < 10:
        tweets = driver.find_elements(By.XPATH, '//article//div[@lang]')

        for tweet in tweets:
            try:
                text = tweet.text.strip()

                # Filter basic
                if (
                    text != "" and
                    text not in seen_tweets and
                    any(word in text.lower() for word in ["makan", "gratis", "indonesia", "anak"])
                ):
                    seen_tweets.add(text)

                    all_data.append({
                        "query": query,
                        "tab": tab,
                        "tweet": text
                    })

                    print(f"✅ {len(all_data)} data terkumpul")

                    # STOP kalau target tercapai
                    if len(all_data) >= TARGET_DATA:
                        return

            except:
                pass

        # scroll
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        scroll_count += 1

        print(f"Scrolling {scroll_count}...")

# =========================
# LOOP SEMUA QUERY & TAB
# =========================
for query in queries:
    for tab in tabs:

        if len(all_data) >= TARGET_DATA:
            break

        print(f"\n🔍 Query: {query} | Tab: {tab}")

        url = f"https://x.com/search?q={query.replace(' ', '%20')}&src=typed_query&f={tab}"
        driver.get(url)

        time.sleep(5)

        scrape_current_page(query, tab)

    if len(all_data) >= TARGET_DATA:
        break

# =========================
# SIMPAN DATA
# =========================
df = pd.DataFrame(all_data)

output_path = "data/raw/mbg_tweets_final.csv"
df.to_csv(output_path, index=False, encoding='utf-8')

print("\n==========================")
print(f"🎯 TARGET: {TARGET_DATA}")
print(f"✅ TOTAL DIDAPAT: {len(df)}")
print(f"📁 FILE: {output_path}")
print("==========================")

# =========================
# SELESAI
# =========================
driver.quit()