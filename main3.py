import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []
all_quotes = soup.select(".quote")
print(all_quotes)  # Print the list of quote elements for debugging
for quote in all_quotes:
    text = quote.select_one(".text").get_text()
    author = quote.select_one(".author").get_text()
    tags = [tag.get_text() for tag in quote.select(".tag")]
    
    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })
#print(soup.prettify())  # Print the prettified HTML for debugging
# # Loop over all quote elements on the page
# for quote in soup.select(".quote"):
#     text = quote.select_one(".text").get_text()
#     author = quote.select_one(".author").get_text()
#     tags = [tag.get_text() for tag in quote.select(".tag")]
    
#     quotes_data.append({
#         "Quote": text,
#         "Author": author,
#         "Tags": ", ".join(tags)
#     })

df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)
print("Saved", len(df), "quotes to quotes.csv!") # Convert list of dicts to Pandas DataFrame and export
