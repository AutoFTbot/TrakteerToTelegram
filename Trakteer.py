# -----------------------------------------------------
# AutoFtBot - Kode ini dibuat oleh AutoFtBot.
# Dilarang keras untuk mengubah, menyalin, atau
# menggunakan kode ini tanpa izin dari AutoFtBot.
# Harap menghubungi untuk informasi lebih lanjut.
# -----------------------------------------------------

from flask import Flask, request
import requests

app = Flask(__name__)
bot_token = "BOT_TOKEN"
chat_id = "LOG_CHAT"

@app.route('/donation', methods=['POST'])
def donation():
    data = request.json
    supporter_name = data['supporter_name']
    supporter_message = data['supporter_message']
    quantity = data['quantity']
    unit = data['unit']
    price = data['price']
    send_thank_you_message(supporter_name, supporter_message, quantity, unit, price)
    return '', 200
def send_message(msg, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
def send_thank_you_message(supporter_name, supporter_message, quantity, unit, price):
    msg = f"""
Halo {supporter_name}! 🌟
Terima kasih banyak atas dukunganmu yang luar biasa!🙏
Kamu baru saja memberikan:
 {quantity} {unit} senilai {price}

pesan anda kepada kami : {supporter_message}

Setiap bantuanmu sangat berarti bagi kami! Terima kasih atas kontribusimu yang luar biasa! 🌺🌍
"""
    send_message(msg, chat_id)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
