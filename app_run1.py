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

line_bot_api = LineBotApi('EPOsx2HnNjg9Ja7GkE7Zd7EqpIcD6HsNF2SOs5OrbB40sPm6RaObrmaWt7oZcp9kuL7zwO/oNqDIrmlyy257KWm7qehgGCZPSzA5VUh6jUDZoTxD/jb0TmU7dG1yEl5aJgs85znwi+77afc8v7g/uAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6e36935df4d1dbbdc767a5121d45aee7')


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
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
