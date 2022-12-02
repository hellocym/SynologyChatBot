import json
import requests
requests.packages.urllib3.disable_warnings()


def webhook_post_msg(url, msg):
    body = 'payload=' + json.dumps({'text': msg})
    response = requests.post(url, data=body, verify=False)


if __name__ == '__main__':
    webhook_url = "https://YOURIP:YOURPORT/webapi/entry.cgi?api=SYNO.Chat.External&method=incoming&version=2&token=%22YOURTOKEN%22"
    webhook_post_msg(webhook_url, "6")
