import openai
import os
from datetime import datetime

prompt = "Generate a markdown formatted document about a random topic. At the bottom, include a disclaimer explaining that the document was generated by you. The first line of the document should be the title. Make sure that the entire document is in proper markdown format, using a mix of various tags to make the document visually appealing."
role = "You are a writer, made to generate documents in markdown format. It is very important that all of the documents you generate are in valid markdown format."
model = "gpt-3.5-turbo"

openai.api_key = os.environ.get("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo" 
# This specifies which GPT model to use, as there are several models available, each with different capabilities and performance characteristics.

def write_article(title,message):
    f = open(f"content/posts/{title}.md", "w")
    f.write("---\n")
    f.write(f"title: '{title}'\n")
    f.write(f"date: {datetime.now()}\n")
    f.write(f"draft: false\n")
    f.write(f"description: {title}\n")
    f.write(f"role: {role}\n")
    f.write(f"model: {model}\n")
    f.write(f"prompt: {prompt}\n")
    f.write("---\n\n")
    f.write(message['content'])
    f.close()

def main():
    response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "system", 
      "content" : role},
        {"role": "user", "content": prompt},
    ])
    message = response.choices[0]['message']
    print("{}".format(message['content']))
    title = message['content'].partition('\n')[0].replace("#","").strip()
    write_article(title,message)

if __name__ == "__main__":
    main()