import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <div id="header" class="box container">
      <h1>E-Commerce Store</h1>
    </div>
    
    <div id="products" class="container">
      <div class="product" data-price="25" data-stock="10">
        <h2 class="title">Wireless Mouse</h2>
        <a href="/buy/101" class="btn buy-btn">Buy Now</a>
        <a href="/details/101" class="btn">Details</a>
      </div>

      <div class="product" data-price="120" data-stock="0">
        <h2 class="title">Mechanical Keyboard</h2>
        <span class="out-of-stock">Sold Out</span>
      </div>

      <div class="product" data-price="85" data-stock="5">
        <h2 class="title">Gaming Headset</h2>
        <a href="/buy/103" class="btn buy-btn">Buy Now</a>
      </div>
    </div>

    <footer class="box">
      <p>Contact support@example.com</p>
    </footer>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
affordable_products=soup.find_all(lambda tag: tag.name=="div" and tag.has_attr("data-price") and int(tag['data-price']) <= 100 )
print(affordable_products)
# note that if we did not use the lambda function, we would have to write a more complex find_all statement to filter by price.
# The lambda function allows us to easily filter the products based on their price attribute.
# if we not provide the tag name it chects to entire document and returns all the tags that match the condition, which is not what we want in this case. By specifying the tag name, we limit the search to only the div tags that have a data-price attribute.