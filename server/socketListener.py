import websocket
import json
import pyrebase

config = {
    "apiKey": "AIzaSyA5Zfsn4fFQIC3IF68I-yCCvluOlcJ8oFo",
    "authDomain": "alarm-7be78.firebaseapp.com",
    "databaseURL": "https://alarm-7be78.firebaseio.com",
    "projectId": "alarm-7be78",
    "storageBucket": "alarm-7be78.appspot.com",
    "messagingSenderId": "796113443167"
  }
firebase = pyrebase.initialize_app(config)

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    message = {
        "request": "subscribe",
        "event_types": ["metal_alarm"],
        "reference": "myRef"
    }
    data_string = json.dumps(message)
    ws.send(data_string)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.2.2/api/v2/events",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()