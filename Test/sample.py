import json
import requests
headers = {"Authorization": "Bearer ya29.GlsIBm_RHgwGwQV-pMuvlKFLNDXbSLZylaEV04tzNTfBPKIktw8ZSn29c8oN_7drBsnpaejC5fandjNQd3jTiUbXm-c4tuaKp8IWJCPK-paiIf6-Ng4kpdFEhv91"}
para = {
    "name": "roche.png",
    "parents": ["14ricvjvrL9rvZop_IanWQfS6Go3jvbKr"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("roche.png", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)