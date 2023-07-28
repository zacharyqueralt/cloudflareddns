import requests
import json

def slack_notify(message):
    f = open("config.json", "r")
    url = json.loads(f.read())['slackwebhookurl']
    f.close()
    
    data = {
        'text': message
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=data, headers=headers)

    if not response.status_code == 200:
        print("!! SLACK MESSAGE FAILED TO SEND !!\nError: {response.text}")
