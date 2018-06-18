# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('zXdV4UMYRUitHOI/gEl2KzaryIbTCeNa0twwElwwYUp5y0ECqg4kUt796Vcw7a/EYwxgnsR7Cms6AsXpyFZtjFwXQXWX9If45fUVHT/VTLSz6Y/wWlKKJnWJCUYYnh8Ue8ali+8uVaZsdfhYjD6hWwdB04t89/1O/w1cDnyilFU=') 
handler = WebhookHandler('a5427de135df9579039872a72d700516') 

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])