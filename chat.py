import openai
openai.api_key = "API KEY" # https://platform.openai.com/account/api-keys

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Wie kann man in Python eine Datei einlesen?"}
  ]
)

print(completion.choices[0].message)

