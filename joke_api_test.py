# import os
import requests
import json
from Credentials.cred import joke_key
import time



def ask_for_joke():
    """a little function to help us pull jokes from our free api"""
    
    url = "https://dad-jokes.p.rapidapi.com/random/jokes"

    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': joke_key
        }

    response = requests.request("GET", url, headers=headers)

    return response


def tell_joke(response=ask_for_joke()):

    if response.status_code == 200:

        joke = json.loads(response.content)
        
        print(joke['setup'])
        time.sleep(2)
        print(joke['punchline'])

    else:
        print("looks like I'm out of jokes for today")