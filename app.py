from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    QuickReply,
    QuickReplyButton,
    PostbackAction,
)
from core.decision import predict_suggestion  # 你的判斷函式

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
LINE_CHANNEL_SECRET = "YOUR_CHANNEL_SECRET"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)


def parse_user_message(text):
    # 簡易關鍵字判斷範例
    context_from_msg = {
        "fatigue_level": 5 if "累" in text else 1,
        "med_adherence": False if "忘記吃藥" in text else True,
        "care_task_type": 0,
        "recent_incident": 0,
    }
    return context_from_msg


def get_user_record(user_id):
    # 這裡用假資料模擬資料庫查詢
    # 實際請改成 DB 查詢
    # 模擬使用 user_id 查詢
    user_record = {
        "user_id": user_id,
        "fatigue_level": 3,
        "med_adherence": True,
        "care_task_type": 1,
        "recent_incident": 0,
    }
    return user_record


def merge_context(db_context, msg_context):
    merged = db_context.copy()
    merged.update(msg_context)  # 訊息資料優先
    return merged


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    for event in events:
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
            user_id = event.source.user_id
            user_text = event.message.text

            db_context = get_user_record(user_id)
            msg_context = parse_user_message(user_text)
            context_dict = merge_context(db_context, msg_context)

        suggestion = predict_suggestion(context_dict)

        reply = TextSendMessage(
            text=f"建議：{suggestion}\n點下方看原因👇",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(label="看解釋", data="action=explain")
                    ),
                    QuickReplyButton(
                        action=PostbackAction(label="已完成", data="action=done")
                    ),
                ]
            ),
        )
        line_bot_api.reply_message(event.reply_token, reply)
    return "OK"
