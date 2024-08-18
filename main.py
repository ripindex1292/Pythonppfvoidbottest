# license MIT
# author Arekusei
import json
import websocket
import time
import sys
import os
from dhooks import Webhook

os.chdir(sys.path[0])

def on_message(ws, message):
    global web_hook, count, txt
    if type(message) == str:
        print(message)
        txt += f'{message}\n'
        count += 1
        if not message.find("cm,") == -1:
            msg = json.loads('{"msg":' + message.lstrip("cm,") + '}')
            msg = msg['msg']

            if msg[2] == 'xx' and msg[1] == 'Threat successfully defeated. Good work!':
                print("Threat successfully defeated. Good work")
                for i in web_hook:
                    i[0].send("Threat successfully defeated. Good work! " + i[1])
                # Sleep for 26 minutes (60 seconds * 26 minutes)
                time.sleep(60 * 26)

            if msg[2] == 'xx' and msg[1] == 'Celebration time over, get back to work.':
                for i in web_hook:
                    i[0].send('Celebration time over.')

            if msg[2] == 'xx' and 'Threat couldn\'t be contained' in msg[1]:
                print("Threat couldn't be contained.")
                for i in web_hook:
                    i[0].send('Threat couldn\'t be contained.')
                # Sleep for 26 minutes (60 seconds * 26 minutes)
                time.sleep(60 * 26)


def on_error(ws, error):
    print("### Error ###")
    print(f"Error: {error}")
    if isinstance(error, Exception):
        print(f"Exception type: {type(error).__name__}")
    time.sleep(0.02)


def on_close(ws, *args):
    print("### closed ###")
    time.sleep(3)


def on_open(ws):
    print('### Successfully connected. ###\n')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Connection": "Upgrade",
        "Upgrade": "websocket",
        "Sec-WebSocket-Version": "13",
        "Sec-WebSocket-Key": "xqBt3ImNzJbYqRINxEFlkg==",
    }


if __name__ == "__main__":
    with open("data.json", 'r', encoding='utf8') as file:
        data = json.load(file)

    web_hook = []
    count = 0
    txt = ""
    for c in data:
        web_hook.append([Webhook(c["url"]), c["role"]])

    while True:
        try:
            ws = websocket.WebSocketApp("wss://pixelplanet.fun:443/ws",
                                        on_open=on_open,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)

            ws.run_forever(ping_interval=20, ping_timeout=10)

        except Exception as e:
            print("Network error occurred. Trying to reconnect...")
            time.sleep(0.02)
