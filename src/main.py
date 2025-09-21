import json
from dotenv import load_dotenv
from website import Website
from openai import OpenAI

load_dotenv()

MODEL = 'gpt-4o-mini'

link_system_prompt = """
You are provided with a list of links extracted from a webpage.
You are able to decide which of the links would be the most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.

You should response in JSON as in this example:
{
  "links": [
    {
      "type": "about page",
      "url": "https://example.com/about"
    },
    {
      "type": "careers page",
      "url": "https://example.com/careers"
    }
  ]
}
"""

def get_link_user_prompt(website: Website) -> str:
    user_prompt = f"""
      Here is the list of links extracted from the webpage {website.url} - 
      Please decide which of the links would be the most relevant to include in a brochure about the company, 
      respond with the full https URL in JSON format,
      Do not include Terms of Service, Privacy Policy, or email links.
      Links (some might be relative links):
      {"\n".join(website.links)}
    """
    return user_prompt

def get_links(url: str):
    website = Website(url)
    client = OpenAI()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_link_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)

if __name__ == "__main__":
    print(get_links('https://anthropic.com'))