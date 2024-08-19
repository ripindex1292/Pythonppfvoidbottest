# license MIT
# author Arekusei
import json
import os
import sys
import time
from time import timezone
import websocket
from dhooks import Webhook

os.chdir(sys.path[0])

def on_message(ws, message):
    global web_hook, count, txt
    if isinstance(message, str):
        print(message)
        if message.find("cm,") != -1:
            msg = json.loads('{"msg":' + message.lstrip("cm,") + '}')
            msg = msg['msg']

# CHAT LOGGER DE ES
            if isinstance(msg[3], int) and msg[3] == 907:
                print('(:flag_' + str(msg[2]) + ': | ' + str(msg[0]) + ' | ' + 'ID:' + str(msg[4]) + '): ' + str(msg[1]))
                message_format = '**:flag_' + str(msg[2]) + ': | ' + str(msg[0]) + '**: ' + msg[1].replace('#d,', 'https://pixelplanet.fun/#d,')
                current_time = time.strftime("%H:%M:%S", time.localtime())
                message_format += f'\n`ID: {str(msg[4])} | {current_time}`'
                for i in web_hook:
                    if i[3] is not None:
                        try:
                            i[3].send(message_format)
                        except Exception as e:
                            print(f"Webhook de Logger de Chat 'es' inválido o vacío,  mensaje no enviado. Logger: {i[3]}")


            if msg[2] == 'xx' and 'Threat successfully' in msg[1]:
                print("■ Threat successfully defeated. Good work")
                for i in web_hook:
                    i[0].send("■ Threat successfully defeated. Good work! " + i[1])

            if msg[2] == 'xx' and 'Celebration time over' in msg[1]:
                for i in web_hook:
                    i[0].send('Celebration time over.')

# VOID COORDS
            
            if 'void' in msg[1].lower() and '#d,' in msg[1]:
                for i in web_hook:
                    i[0].send('(:flag_' + str(msg[2]) + ': | ' + str(msg[0]) + ' | ' + 'ID:' + str(msg[4]) + '): ' + msg[1].replace('#d,', 'https://pixelplanet.fun/#d,'))

            if msg[2] == 'xx' and msg[1] == 'Fight starting!':
                for i in web_hook:
                    i[0].send('■ Fight starting!' + i[2])

            if 'Clown Void reached' in msg[1]:
                for i in web_hook:
                    i[0].send(f"> {msg[1]}")

            if msg[2] == 'xx' and msg[1] == 'Void seems':
                for i in web_hook:
                    i[0].send('Void seems to leave again.')

            if msg[2] == 'xx' and 'Threat couldn\'t be' in msg[1]:
                print("■ Threat couldn't be contained. Leave the area")
                for i in web_hook:
                    i[0].send('Threat couldn\'t be contained.')


def on_error(ws, error):
    print("### Error ###")
    print(f"Error: {error}")
    if isinstance(error, Exception):
        print(f"Exception type: {type(error).__name__}")
    time.sleep(0.02)


def on_close(ws, *args):
            print("### closed ###")
            update_webhook()  # Update webhook on close


def on_open(ws):
    print('### Successfully connected. ###\n')

    headers = {
        "Host": "scd.pixelplanet.fun",
        "Connection": "Upgrade",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Cookie": "plang=es",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Upgrade": "websocket",
        "Origin": "https://pixelplanet.fun",
        "Sec-WebSocket-Version": "13",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9",
        "Sec-WebSocket-Key": "dLm8PgMW41XGZeNrRjOmUQ==",
        "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits"
    }

    ws.send("\r\n".join([f"{k}: {v}" for k, v in headers.items()]))

    ws.send(json.dumps(["sub", "chat"]))
    ws.send(json.dumps(["sub", "1"]))
    ws.send(json.dumps(["sub", "907"]))
    ws.send("\r\n".join([
        "GET /assets/client.es.38eedcd8.js HTTP/1.1",
        "Host: pixelplanet.fun",
        "Cookie: plang=es",
        "Accept: */*",
        ""
    ]))


if __name__ == "__main__":
    web_hook = []
    count = 0
    txt = ""

    def update_webhook():
        global web_hook
        with open("data.json", 'r', encoding='utf8') as file:
            data = json.load(file)
        web_hook = []
        for c in data:
            if 'logger' in c and c['logger']:
                try:
                    web_hook.append([Webhook(c["url"]), c["role"], c["alert"], Webhook(c["logger"])])
                except ValueError:
                    print(f"Error con webhook {c['logger']}: Inválido o vacío.")
            else:
                web_hook.append([Webhook(c["url"]), c["role"], c["alert"], None])

    update_webhook()



    while True:
        try:
            ws = websocket.WebSocketApp("wss://pixelplanet.fun:443/ws?cid=907",
                                        on_open=on_open,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close,
                                        cookie= "plang=es",
                                        header=["Cookie: plang=es"]
                                       )

            ws.run_forever(ping_interval=20, ping_timeout=10)

        except Exception as e:
            print(f"Network error occurred: {e}. Trying to reconnect...")
            time.sleep(0.01)
