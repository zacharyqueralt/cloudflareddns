# cloudflareddns

== INSTALL ==
- install python: https://www.python.org
- navigate to main directory of downloaded code
- run: "pip install -r requirements.txt"
- run: "python main.py"


== LINKING A CLOUDFLARE ZONE ==
- login to https://dash.cloudflare.com
- click on the zone you wish to use
- scroll down to "API" and copy the zone id
- paste it into config.json
- click the profile icon (top right)
- click "my profile"
- click "api tokens"
- click "create token"
- click "use template" for "edit zone dns"
- under "zone resources" select the same zone
- click "continue to summary"
- click "create token"
- copy the token and paste it into config.json


== SLACK NOTIFICATIONS SETUP ==
- make slack account or signin
- goto https://api.slack.com/apps
- click "create new app"
- click "from scratch"
- name it something and select "servers"
- click "incoming webhooks"
- turn on
- click "add new webhook to workspace"
- select a channel - you may need to make one and a server
- copy the new webhook url
- paste into config.json under "slackwebhookurl"
- remember to change notifications to true in config.json
