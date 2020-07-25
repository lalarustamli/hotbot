from hotbot import app

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

def is_user_message(event):
    """Return whether the message is from the user.
    """
    return (event.get('message') and not event['message'].get("is_echo"))

@app.route('/hotbot',methods=['GET', 'POST'])
def listen():
    if request.method == "GET":
        return verify_webhook(request)
    if request.method == "POST":
        message = request.get_json()
        print(message)





