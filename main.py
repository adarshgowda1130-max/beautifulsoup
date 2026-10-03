from bs4 import BeautifulSoup
from soupsieve import select_one
with open("C:/Users/Adarsha MP/Downloads/bs4-start/bs4-start/website.html") as file:
    data=file.read()
soup=BeautifulSoup(data,"html.parser")
print(soup.title.string)#this will print the title of the html page
#to get all the paragraphs,anchors tags,list eliments in the html page
all_paragraphs=soup.find_all("p")
# print(all_paragraphs)#this will print all the paragraphs in the html page
for paragraph in all_paragraphs:
    print(paragraph.getText())#this will print the text of all the paragraphs in the html page
all_anchors=soup.find_all("a")
# print(all_anchors)#this will print all the anchors in the html page
for tags in all_anchors:
    print(tags.get("href"))#this will print the href of all the anchors in the html page
heading=soup.find(name="h1",id="name")#this will find the h1 tag with id name
print(heading.getText())#this will print the text of the heading
companey_url=soup.select_one(selector="p a")
print(companey_url.get("href"))#this will print the href of the anchor tag inside the paragraph tag
headings=soup.select(selector=".heading")#this will find all the tags with class heading
for heading in headings:    
    print(heading.getText())#this will print the text of all the headings with class heading