from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8305667170:AAEnbi96RL8d3YtNVwPrY1bezjMQf-FuTDI"
CHAT_ID = "1861373830"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(url, data=data)

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.json

    signal = data['signal']
    ticker = data['ticker']
    price = data['price']
    timeframe = data['timeframe']

    msg = f"BYOMOKESH AB SIGNAL\n\nSymbol: {ticker}\nSignal: {signal}\nPrice: {price}\nTimeframe: {timeframe}"

    send_telegram(msg)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
