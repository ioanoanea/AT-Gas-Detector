import datetime
import time

import requests
import serial


def send_request(title, body):
    url = 'https://fcm.googleapis.com/fcm/send'
    api_key = 'AAAADa-SV5E:APA91bGDinDtzuxA6r04QwZKDAtb5HlEx59s08C6ENlrcBGzObiJJt' \
              '-hxqO8BBLhh1PIGBSQMCdazdO4zD_PtdttKw3FcD2jZGUmjQKVoL-OIgSLqeAaGESsPJzYI-Nrixd3Oh77lqR4'
    headers = {
        'Authorization': 'key=' + api_key,
        'Content-Type': 'application/json'
    }
    to = 'eCxqUvD_Sa6adEyOK-L4-8' \
         ':APA91bHJDawglfJh7EFl6p5PiS0COoifNSvbIZSDWgRjDhkdconofqCzbnWLuaYwlHVGbcmv0qfnETdGqCcFe4NlH9Y5VP1oR3JWajwdSDjfR2elSrZ9iNTih4m6oQoE3LqknmCNBdET'
    notification = {
        'to': to,
        'notification': {
            'title': title,
            'body': body
        }
    }
    response = requests.post(url, json=notification, headers=headers)
    print(response)


def check_time(last_time):
    if last_time is None:
        return True
    this_time = datetime.datetime.now()
    return abs((this_time - last_time).seconds) > 60


arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

last_time = None

while True:
    try:
        data = arduino.readline().decode().strip()
        print(data)
        if int(data) > 200:
            if check_time(last_time):
                send_request('Alert!', 'Gas detected!')
                last_time = datetime.datetime.now()
    except:
        print("invalid serial")
