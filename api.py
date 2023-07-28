import requests
import json

def check(zoneid, apikey):
    url = "https://api.cloudflare.com/client/v4/zones/"+zoneid+"/dns_records"

    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer "+apikey
    }
    response = requests.request("GET", url, headers=headers)
    
    final = []
    response = json.loads(response.text)['result']
    for res in response:
        final.append({ "name": res['name'], "type": res['type'], "id": res['id'], "content": res['content'] })
    return response[0]['zone_name'],final




def update(dnsid, rtype, name, value, proxied, ttl, zoneid, apikey):
    url = "https://api.cloudflare.com/client/v4/zones/"+zoneid+"/dns_records/"+dnsid
    payload = {
        "content": value,
        "name": name,
        "proxied": proxied,
        "type": rtype,
        "ttl": ttl
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer "+apikey
    }
    response = requests.request("PUT", url, json=payload, headers=headers)
    return json.loads(response.text)



def create(rtype, name, value, proxied, ttl, zoneid, apikey):
    url = "https://api.cloudflare.com/client/v4/zones/"+zoneid+"/dns_records"
    payload = {
        "content": value,
        "name": name,
        "proxied": proxied,
        "type": rtype,
        "ttl": ttl
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer "+apikey
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return json.loads(response.text)



