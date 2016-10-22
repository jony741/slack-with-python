"""
Import requests and simplejson module
"""
import requests
import simplejson as json


def slack_hooks(message='Hello Developer', channel_type=1, username="192.168.100.227"):
    # try to get slack configuration
    slackConfig = __slack_config(channel_type)
    

    payload = json.dumps(
        {"channel": slackConfig['d']['channel'],
         "username": username,
         "text":message,
         "icon_emoji":  slackConfig['d']['icon_emoji']})

    #post call using request module
    r = requests.post(slackConfig['ep'], data=payload)
    if r.status_code == 200:
        return 'Success'
    else:
        return r.content


def __slack_config(param):
    # this is your own slack api end point
    #sould be change the end point
    end_point = "https://hooks.slack.com/services/yourendpoint"

    #channel name
    value = {
        '1': {'channel': '#error', 'icon_emoji': ':ghost:', 'icon_url': ''},
        '2': {'channel': '#error2', 'icon_emoji': ':bank:', 'icon_url': ''}}

    return {'d': value[str(param)], 'ep': end_point}
    
    
"""
Handle three parameter
1. your message
2. channel type
3. username/hostname
"""

slack_hooks()



