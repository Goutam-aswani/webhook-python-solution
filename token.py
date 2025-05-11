import requests

data = {
    "name": "Goutam Aswani",               
    "regNo": "0827AL221053",               
    "email": "goutamaswani221152@acropolis.in"  
}

api_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

response = requests.post(api_url, json=data)

if response.status_code == 200:
    result = response.json()
    print("Webhook URL:", result.get("webhook"))
    print("Access Token:", result.get("accessToken"))
else:
    print("Failed to generate webhook. Status code:", response.status_code)
    print("Response message:", response.text)
