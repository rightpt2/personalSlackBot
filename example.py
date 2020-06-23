from Credentials.cred import *
import os
# import re
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token=Bot_OAuth_Token)

try:
    response = client.chat_postMessage(
        channel='#random',
        text="I'm learning to tell jokes so plese, take it easy on me for a bit!")
    assert response["message"]["text"] == "I'm learning to tell jokes so plese, take it easy on me for a bit!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")