from bs4 import BeautifulSoup
import requests
from lxml import etree


def get_all_reviews(product_name):
    res = requests.get("https://www.flipkart.com/search?q="+product_name)
    soup = BeautifulSoup(res.text, 'html.parser')
    bigboxes = soup.findAll("div", {"class": "_1AtVbE col-12-12"})
    res = requests.get("https://www.flipkart.com" +bigboxes[3].div.div.div.a['href'])
    soup = BeautifulSoup(res.text, 'html.parser')
    comments = soup.findAll("div", {"class": "col _2wzgFH"})
    reviews = []
    for comment in comments:
        temp = []
        temp.append(product_name)
        temp.append(comment.find("p", {"class": '_2sc7ZR _2V5EHH'}).text)
        temp.append(comment.find("div", {"class": "_3LWZlK _1BLPMq"}).text)
        temp.append(comment.find("p").text)
        temp.append(comment.find("div", {"class": "t-ZTKy"}).text)
        reviews.append(temp)
    return reviews
