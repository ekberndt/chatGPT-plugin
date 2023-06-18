import os
import openai

# Assumes the files /auth/openai-key.txt and openai-org.txt exist
src_dir = os.path.dirname(os.path.abspath(__file__))
api_key_path = os.path.join(src_dir, '../auth/openai-key.txt')
# org_path = os.path.join(src_dir, '../auth/openai-org.txt')

with open(api_key_path, 'r') as file:
    api_key = file.read()

# with open(org_path, 'r') as file:
#     org = file.read()

# openai.organization = "ORG-HERE"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
# openai.Model.list()

def complete(prompt, max_token=50, outputs=3):
    reponse = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_token,
        n=outputs
    )
    output = list()
    for i in reponse['choices']:
        output.append(i['text'].strip())
    return output

output = complete("Write me a poem")
print(output)