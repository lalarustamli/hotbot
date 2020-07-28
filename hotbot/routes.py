from hotbot import chatbot
from hotbot import app
from flask import request


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/hotbot',methods=['GET', 'POST'])
def listen():
    if request.method == "GET":
        return chatbot.verify_webhook(request)
    if request.method == "POST":
        message = request.get_json()
        # Check if the user message exists and it has sender and recipient id
        if 'messaging' in request.json['entry'][0]:
            events = request.json['entry'][0]['messaging']
            for event in events:
                # Check if the message comes from the user
                if chatbot.is_user_message(event):
                    # Abstraction of respond function
                    chatbot.respond(event)
        return message







