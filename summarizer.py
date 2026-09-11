
from scraper import fetch_website_content
from openai import OpenAI

import requests


OLLAMA_BASE_URL = 'http://localhost:11434/v1/'

system_prompt = """
You are a website summarization assistant.

Your job is to summarize only the information explicitly present in the provided website content.

First, identify the primary topic, purpose, or identity of the webpage.
Then focus the summary mainly on information directly related to that primary topic.

De-emphasize or omit unrelated secondary content such as:
- navigation text
- footer content
- social links
- advertisements
- sidebar content
- recommended content
- cross-site sections
- unrelated news categories

Do not create sections about contact information, social links, or actions unless they are central to the webpage's primary purpose.

Do not infer, invent, or assume information that is not included in the provided text.

Do not include notes, disclaimers, or commentary about your summarization process.

If the page mentions a linked article, course, resource, product, or page without providing its contents, only mention that it exists. Do not guess what the linked content contains.

If the page contains news, announcements, resources, projects, courses, products, or services, summarize the items that are most relevant to the page's primary topic.

Respond in concise, clear Markdown.

Create only sections that are relevant to the actual content.
Avoid repetitive disclaimers and unnecessary details.
"""
    
user_prompt_prefix = """
Here is the extracted content of a webpage.

Please provide:

1. A concise summary explaining what the webpage is mainly about.
2. The most important information related to the page's primary topic.
3. Any important news, announcements, resources, projects, courses, products, or services that are explicitly mentioned and relevant to that primary topic.

Prioritize the main subject of the webpage.
Do not give equal importance to unrelated secondary sections that may appear elsewhere on the page.

Use only the supplied website content.

Website content:
"""


def get_available_models():
    try:
        response = requests.get(
            url="http://localhost:11434/api/tags",
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        return [
            model['name']
            for model in data['models']
        ]

    except requests.RequestException:
        return []


def messages_for_website(content):
    return [
        {'role':'system','content': system_prompt},
        {'role':'user', 'content': user_prompt_prefix +"\n\n" + content}
    ]


def summarize_website_content(url,model):

    content = fetch_website_content(url)

    client = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

    response = client.chat.completions.create(
        model=model,
        messages = messages_for_website(content=content)
    )

    return response.choices[0].message.content

