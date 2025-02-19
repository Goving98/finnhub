from fastapi import FastAPI, Request
import json
import requests
import os
app = FastAPI()


@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()  # Get the trading data
    print("Received Webhook Data:", json.dumps(payload, indent=2))
    return {"message": "Webhook received"}



tok = os(API_KEY)
WEBHOOK_URL = "wss://ws.finnhub.io"  # Replace with ngrok/public server URL

headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}

payload = {"webhook_url": WEBHOOK_URL}

response = requests.post("wss://ws.finnhub.io", headers=headers, json=payload)

print(response.json())
