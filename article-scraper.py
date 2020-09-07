#!/usr/bin/python
import mechanize
import urllib
import os
import bs4
import json
from collections import OrderedDict
import dicttoxml
import xml.dom.minidom
import glob
import re

# clear files before opening
open(os.getcwd() + '/src/data/articles.json', 'w').close()
jsonFile = open(os.getcwd() + '/src/data/articles.json', 'a')

# create images directory/remove images contents at start
# if os.path.exists(os.getcwd() + '/src/assets/articles/'):
# 	filelist = glob.glob(os.getcwd() + "/src/assets/articles/*")
# 	for f in filelist:
# 		os.remove(f)
# else:
#     os.makedirs(os.getcwd() + '/src/assets/articles/')

userAgent = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('user-agent', userAgent)]

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', userAgent)]
urllib.request.install_opener(opener)

baseUrl = 'https://muckrack.com/neil-maggs/articles'

selectors = {
    'articles': '.news-story .news-story-title a',
    'title': 'meta[property="og:title"]',
    'description': 'meta[property="og:description"]',
    'date': '.news-story-meta .timeago',
    'image': 'meta[property="og:image"]'
}

def scrape():
    page = browser.open(baseUrl)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'lxml')

    articles = soup.select(selectors['articles'])
    dates = soup.select(selectors['date'])

    for i in range(len(articles)):
        articleLink = articles[i]['href']

        page = browser.open(articleLink)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'lxml')

        title = soup.select(selectors['title'])[0]['content']
        description = soup.select(selectors['description'])[0]['content']
        image = soup.select(selectors['image'])[0]['content']
        date = dates[i].text.strip()

        ordered = OrderedDict([("title", title), ("description", description), ("link", articleLink), ("image", image), ("date", date)])

        appendToJsonFile(ordered)

def appendToJsonFile(dictionary):
	jsonFile.write(json.dumps(dictionary, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')) + ',\n')

def getImageLink(link):
    page = browser.open(link)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'lxml')
    imageTag = soup.select(selectors['image'])
    if imageTag[0].has_attr('content'):
        return imageTag[0]['content']
    else:
        return ''

def downloadImage(link):
    page = browser.open(link)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'lxml')
    imageTag = soup.select(selectors['image'])
    if imageTag[0].has_attr('content'):
        imageSrc = imageTag[0]['content']
        filename = imageSrc.split('/')[-1]
        cwd = os.getcwd()
        downloadedImgLoc = '../assets/articles/' + filename
        print('downloading', imageSrc)
        urllib.request.urlretrieve(imageSrc, cwd + '/src/assets/articles/' + filename)
        return downloadedImgLoc

def main():
    jsonFile.write('[\n')
    scrape()
    jsonFile.write(']')

if __name__ == '__main__':
	main()
