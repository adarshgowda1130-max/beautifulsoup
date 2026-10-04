from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
data=response.text
soup = BeautifulSoup(data, 'html.parser')
articles=soup.find_all(name="span",class_="titleline")
articles_score=soup.find_all(name="span",class_="score")
scores=[int(score.getText().split()[0]) for score in articles_score]
article_texts=[article.get_text() for article in articles]
article_links=[article.find("a").get("href") for article in articles]
print(article_texts[0:5])
print(article_links[0:5])
print(scores[0:5])
max_score_index=scores.index(max(scores))
print(f"Article with the highest score: {article_texts[max_score_index]}")
print(f"Score: {scores[max_score_index]}")