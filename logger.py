from datetime import datetime

LOG_FILE = "aplikasi.log"

def tulis_log(pesan: str):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{waktu}] {pesan}\n")