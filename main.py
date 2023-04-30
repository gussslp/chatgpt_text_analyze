import openai

openai.api_key = "api_key"

text = input("enter text: ")

prompt=f"analyze the content of the text, display statistics on the number of words, sentences and named entities in this text : {text}"

model = "text-davinci-003"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
print(generated_text)
