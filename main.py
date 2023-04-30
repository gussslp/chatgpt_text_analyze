import openai

openai.api_key = ""
model = "text-davinci-003"

import os
txt_list = []
for file in os.listdir():
    if file.endswith(".txt"):
        txt_list.append(file)

with open(txt_list[0]) as f:
    text = f.readlines()

    prompt=f"analyze the content of the text, display statistics on the number of words, sentences and named entities in this text : {text}"

    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

    generated_text = response.choices[0].text
    print(generated_text)
