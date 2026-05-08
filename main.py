import requests
import time
import os

BOT_TOKEN = os.getenv("8791230210:AAH3h1EgwJFCFA7k1lEW_tkFxDeZ9r2_MaM")
CHANNEL_ID = os.getenv("@daddyscricketline")

def send_msg(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHANNEL_ID, "text": text})
        print("MSG SENT")
    except:
        pass

print("CRICKET BOT START")

send_msg("🏏 CRICKET BOT LIVE 🏏")

while True:
    try:
        r = requests.get("https://hs-consumer-api.espncricinfo.com/v1/pages/matches/current?lang=en", timeout=5)
        data = r.json()
        matches = data.get("content", {}).get("matches", [])
        
        for m in matches[:3]:
            t1 = m.get("team1", {})
            t2 = m.get("team2", {})
            title = m.get("name", "LIVE")
            
            msg = f"🏏 {title}\n{t1.get('team', {}).get('shortName', 'T1')}: {t1.get('score',0)}/{t1.get('wickets',0)}\n{t2.get('team', {}).get('shortName', 'T2')}: {t2.get('score',0)}/{t2.get('wickets',0)}"
            send_msg(msg)
        
        print(f"OK: {len(matches)} matches")
        time.sleep(20)
        
    except:
        print("RETRY")
        time.sleep(20)
