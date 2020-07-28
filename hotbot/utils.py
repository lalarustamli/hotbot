from wit import Wit

access_token = "3B73VICLG6DCXL6NY6LLDYOJXLVHLWEG"

client = Wit(access_token)
def wit_response(user_message):
    """ Return Wit.ai <entity> and <value> of message based on <user_message>
    """
    resp = client.message(user_message)
    intent = None
    entity = None
    value = None

    try:
        intent = list(resp['intents'])[0]['name']
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return (intent,entity, value)

print(wit_response("speaking по русски ?"))
