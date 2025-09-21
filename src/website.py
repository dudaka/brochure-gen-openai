import requests
from bs4 import BeautifulSoup

class Website:
  def __init__(self, url: str):
    self.url = url
    response = requests.get(url)
    self.body = response.content
    soup = BeautifulSoup(self.body, 'html.parser')
    self.title = soup.title.string if soup.title else 'No Title Found'
    if soup.body:
      for irrelevant in soup.body(['script', 'style', 'img', 'input']):
        irrelevant.decompose()

      self.text = soup.body.get_text(separator='\n', strip=True)
    else:
      self.text = ''
    links = [link.get('href') for link in soup.find_all('a')]
    self.links = [link for link in links if link]

  def get_content(self) -> str:
    return f'Website Title: {self.title}\nWebpage Contents:\n{self.text}\n\n'
  

if __name__ == "__main__":
  ed = Website('https://edwarddonner.com')
  print(ed.get_content())
  print(ed.links)