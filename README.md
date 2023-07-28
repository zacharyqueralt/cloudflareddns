# cloudflareddns

== INSTALL ==
- install python: https://www.python.org
- navigate to main directory of downloaded code
- run: "pip install -r requirements.txt"
- run: "python main.py"




== SLACK NOTIFICATIONS SETUP ==
- make slack account or signin
- goto https://api.slack.com/apps
- create new app
- from scratch
- name it something and select servers
- click incoming webhooks
- turn on
- click add new webhook to workspace
- select a channel - you may need to make one and a server
- copy the new webhook url
- paste into config.json under "slackwebhookurl"
- remember to change notifications to true in config.json
