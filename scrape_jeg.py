

import os
import sys
import pandas as pd
import random
import matplotlib.pyplot as plt
import sqlite3
from bs4 import BeautifulSoup, ResultSet
import urllib.request
import re
import tqdm
from tqdm import tqdm

os.chdir("/home/chris/HOPE") # HARDCODED FILE PATH
random.seed(666)

def scrape_article_urls(url, latest_volume):

    article_urls = pd.DataFrame([])
    for volume in tqdm(range(1, latest_volume + 1)):
        new_url = url + str(volume)
        for issue in range(1,10): # Harcdoded
            newest_url = new_url + "/" + str(issue) # Technical debt: fix the janky naming conventions
            html_page = urllib.request.urlopen(newest_url)
            soup = BeautifulSoup(html_page, "html.parser")
            soup = soup.select("ol") # "ol" is the HTML table full of articles that we are searching for
            if len(str(soup[0])) == 10: # Harcdoded und
                print("This page does not exist!")
                break
            print(newest_url)
            df = pd.DataFrame(soup)
            df = df[df.columns[1::2]].T
            for i in range(0, len(df)):
                line = str(df.iloc[i, 0])
                line = line.split('href=\"')[1]
                line = line.split('\">')[0]
                line = pd.DataFrame(pd.Series(line))
                line.columns = ["article_url"]
                line["article_url"] = "https://link.springer.com/" + line["article_url"]
                line["volume"] = volume
                line["issue"] = issue
                article_urls = article_urls.append(line)

    return(article_urls)


def crawl_articles(input):

    articles = pd.DataFrame([])
    for i in tqdm(range(0, len(input))):
        url = urls.iloc[i,0]
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")
        metadata = pd.DataFrame([])
        for a in soup.find_all('meta'):
            a = str(a)
            content = a.rsplit(' ', 1)[0]
            attribute = a.rsplit(' ', 1)[1]
            attribute = str(attribute.rsplit('\"/>', 1)[0])
            try:
                attribute = attribute.rsplit('\"', 1)[1]
            except IndexError:
                continue
            content = pd.DataFrame(pd.Series(content))
            content.columns = [attribute]
            content = content.T
            metadata = metadata.append(content)
        metadata["attribute"] = metadata.index
        metadata = metadata[metadata.attribute.isin(["dc.publisher", "dc.type", "dc.description", "citation_title", "citation_publication_date", "dc.subject", "citation_author","citation_author_institution"])] #drop useless (?) data
        metadata.columns = ["content", "attribute"]
        metadata[['trash','text']]  = metadata['content'].str.split('=',expand=True)
        metadata = metadata[["attribute", "text"]]
        metadata = metadata.reset_index(drop=True)
        metadata['text'] = metadata['text'].str[1:-1]
        metadata = metadata.groupby(['attribute'])['text'].apply('/'.join).reset_index()
        metadata = metadata.T
        headers = metadata.iloc[0]
        metadata = pd.DataFrame(metadata.values[1:], columns=headers)
        metadata["url"] = str(url)
        citations = soup.find(id="altmetric-container")
        citations = citations.text
        citations = citations.replace('\n', ' ').replace('\r', '')
        metadata["accesses"] = citations.rsplit('Accesses', 1)[0]
        citations = citations.rsplit('Accesses', 1)[1]
        metadata["citations"] = citations.rsplit('Citations', 1)[0]
        articles = articles.append(metadata)

    return(articles)

if __name__ == "__main__":

    urls = scrape_article_urls("https://link.springer.com/journal/10887/", latest_volume=25)
    df = crawl_articles(urls)
    df.to_csv("journal_of_economic_growth.csv")