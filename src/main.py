import json
from dotenv import load_dotenv
from website import Website
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
console = Console()

MODEL = 'gpt-4o-mini'
client = OpenAI()

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

system_prompt = """
You are an assistant that analyzes the contents of several relevent pages from a company's website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown format.
Include details of company culture, customers and carreers/jobs if you have the information.
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

def get_all_details(url: str):
    result = f"""
    Landing Page:
    {Website(url).get_content()}
    """

    links = get_links(url)
    for link in links['links']:
        result += f"""

        {link['type']}
        {Website(link['url']).get_content()}
        """
    return result

def get_brochure_user_prompt(company_name: str, url: str) -> str:
    user_prompt = f"""
      You are looking at a company called: {company_name}
      Here is the contents of its landing page and other relevant pages; use this information to create a short brochure of the company in markdown format.
      {get_all_details(url)}
    """
    return user_prompt[:20000]

def create_brochure(company_name: str, url: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ]
    )
    result = response.choices[0].message.content
    md = Markdown(result)
    console.print(md)
    

if __name__ == "__main__":
    create_brochure('Anthropic', 'https://anthropic.com')