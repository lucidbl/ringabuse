import requests
import time

token = {"authorization":"token"}
group_id = input("Group ID: ")
payload = {
    "recipients":["paste id"] #if you want to ring more do: ["id","id","id"]

}

while True:
    ring = requests.post(f"https://discord.com/api/v9/channels/{group_id}/call/ring", headers = token, json=payload)
    time.sleep(0.05)
    stop_ring = requests.post(f"https://discord.com/api/v9/channels/{group_id}/call/stop-ringing", headers = token, json=payload)
    time.sleep(0.05)
