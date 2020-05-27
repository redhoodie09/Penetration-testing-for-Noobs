import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
print(questions[0].attrs)
print(questions[0].get("id", 0))
print(questions[0].select(".question-hyperlink"))
print(questions[0].select_one(".question-hyperlink"))
print(questions[0].select_one(".question-hyperlink").getText())
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
