from api import check, update, create
from notify_api import slack_notify
import json
import requests
import time


def synchronous_update(config, newip):
    for zone in config['zones']:
        amountupdated = 0

        for record in zone['records']:
            zonename, records = check(zone['zoneid'], zone['apikey'])

            exists = False
            for r in records:
                if r['name'] == record['name'] and r['type'] == record['type']:
                    exists = True

            if exists:
                doupdate = True
                for r in records:
                    if r['name'] == record['name'] and r['type'] == record['type'] and r['content'] == newip:
                        doupdate = False

                if doupdate:
                    dnsid = ""
                    for r in records:
                        if r['name'] == record['name'] and r['type'] == record['type']:
                            dnsid = r['id']

                    print("Updating '"+record['name']+"' to '"+newip+"'")
                    res = update(dnsid, record['type'], record['name'], newip, record['proxied'], 1, zone['zoneid'], zone['apikey'])
                    if res['success']:
                        amountupdated += 1
                    elif config['notifications']:
                        slack_notify("Updating failed:\nType: {}\nName: {}\nValue: {}\nProxied: {}".format(record['type'], record['name'], record['value'], record['proxied']))

            else:
                print("Creating '"+record['name']+"' to '"+newip+"'")
                res = create(record['type'], record['name'], newip, record['proxied'], 1, zone['zoneid'], zone['apikey'])
                if res['success']:
                        amountupdated += 1
                elif config['notifications']:
                    slack_notify("Creation failed:\nType: {}\nName: {}\nValue: {}\nProxied: {}".format(record['type'], record['name'], record['value'], record['proxied']))

        if amountupdated > 0:
            slack_notify("Successfully updated {} records in zone \"{}\"".format(amountupdated, zonename))



def trigger(config, amount, pause):
    newip = requests.get('http://checkip.amazonaws.com').text.replace("\n","")
    #newip = requests.get('http://ip.42.pl/raw').text           #alternative
    try:
        synchronous_update(config, newip)
    except Exception as e:
        print("Error somewhere: "+str(e)+"\nAttempting to recover through recursion ("+str(amount)+")")
        trigger(config, amount+1, pause)
        time.sleep(5)
    print("Update complete - pausing for "+pause+" mins\n")


while True:
    f = open("config.json", "r")
    config = f.read()
    f.close()
    try:
        config = json.loads(config)
    except Exception as e:
        print("Your syntax of config.json sucks - fix it lol\nTrace below:\n"+str(e))
    print("Config load succcessful - triggering an update\n")
    trigger(config, 0, config['interval (mins)'])
    time.sleep(60*float(config['interval (mins)']))
