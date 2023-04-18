#import openai
apikey = "" # https://platform.openai.com/account/api-keys
#openai.api_key = apikey 

#completion = openai.ChatCompletion.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    {"role": "user", "content": "Wie kann man in Python eine Datei einlesen?"}
#  ]
#)

###
# API Request with requests

import requests # https://requests.readthedocs.io/en/latest/

response = requests.post('https://api.openai.com/v1/chat/completions',
                        headers={'Authorization': f'Bearer {apikey}'},
                        json = {
                                    "model": "gpt-3.5-turbo",
                                    "messages": [{"role": "user", "content": "Hello!"}]
                                }
                        )

completion = response.json()

print(completion['choices'][0]['message'])
