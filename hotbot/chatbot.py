import requests

TOKEN = "EAAEFyjOzpW0BALLnIubQe3tMmM2EEhLgZAum0mqCddLwlWoWTgle0zPuwAolv9OJsebnAsg6JRFFKzaTcirSFlM5YZAHC0fwQXJZCWZArKdGoQ9okaIDrLLHe5FjAGPFcbZClNNOYDPyxw6CK2wmCgN2VbB0PYufGJNaaLkbbB5bWSLs2ZCBPR"
API = "https://graph.facebook.com/v7.0/me/messages"


def verify_webhook(req):
    """Return the challenge token from the request if token is valid.
    """
    if req.args.get('hub.verify_token') == "hotbot":
        return req.args.get('hub.challenge')
    else:
        return "wrong token"

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
    return response.json()