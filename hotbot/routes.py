from hotbot import app
from flask import request

TOKEN = "EAAEFyjOzpW0BALLnIubQe3tMmM2EEhLgZAum0mqCddLwlWoWTgle0zPuwAolv9OJsebnAsg6JRFFKzaTcirSFlM5YZAHC0fwQXJZCWZArKdGoQ9okaIDrLLHe5FjAGPFcbZClNNOYDPyxw6CK2wmCgN2VbB0PYufGJNaaLkbbB5bWSLs2ZCBPR"
API = "https://graph.facebook.com/v7.0/me/messages"
@app.route('/')
def index():
    return 'Hello World!'


def verify_webhook(req):
    """Return the challenge token from the request if token is valid.
    """
    if req.args.get('hub.verify_token') == "hotbot":
        return req.args.get('hub.challenge')
    else:
        return "wrong token"


@app.route('/hotbot',methods=['GET', 'POST'])
def listen():
    if request.method == "GET":
        return verify_webhook(request)
    if request.method == "POST":
        message = request.get_json()
        if 'messaging' in request.json['entry'][0]:
            events = request.json['entry'][0]['messaging']
            for event in events:
                if is_user_message(event):
                    respond(event)




def is_user_message(event):
    """Return whether the message is from the user.
    """
    return (event.get('message') and not event['message'].get("is_echo"))


def respond(event):
    """Formulate a response to the user and pass it on to a send_message function.
    """
    sender_id = event['sender']['id']
    message = "Hello you back!"
    send_message(sender_id, message)

def send_message(recipient_id, message):
    """Send a response to Facebook by making a post request.
    """
    payload = {
        'message': {
            'text': message
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': TOKEN
    }

    response = requests.post(
        API,
        params=auth,
        json=payload
    )
    print('payload2'+str(payload))
    return response.json()