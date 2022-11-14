import time
import requests
import json
import sys
import pandas as pd
import matplotlib.pyplot as plt
year = 2010

key = "TQrjlH0ESN5IoBOV6GOTDdInphTm71Pt"

def text(x):
    text = x['headline']['main'] + " " + x.abstract
    if x.abstract == x.lead_paragraph:
        if x.abstract == x.snippet:
            return text
        else:
            return text + " "+ x.snippet
    else:
        text = text + " " + x.lead_paragraph
        if x.lead_paragraph != x.snippet and x.abstract != x.snippet:
            return text + " " + x.snippet
        else:
            return text
    
def keywords(x):
    topics = []
    for i in x['keywords']:
        if i['name'] == 'subject' and "editorial" not in i['value'].lower():
            if len(topics) >= 2 or i['rank'] >= 4 and len(topics) >0:
                return topics
            topics.append(i['value'].lower())
    return topics
data = pd.DataFrame()
for month in range(1,13):
    month = 1
    url = "https://api.nytimes.com/svc/archive/v1/{}/{}.json?api-key={}".format(year, month, key)
    r = requests.get(url).text
    data = json.loads(r)
# time.sleep(7)

    df = pd.DataFrame(data['response']['docs'])
    df.drop(['print_section', 'print_page', 'multimedia', 'document_type','news_desk', 'source', 'word_count', "_id", "byline", 'type_of_material', "pub_date", "uri", 'section_name', "subsection_name"],1, inplace=True)
    df['text'] = df.apply(lambda x : text(x), axis=1)
    dr = df.apply(lambda x: len(x['text']) < 100, axis=1)

    df.drop(df[dr].index, inplace=True)

    df.drop(['lead_paragraph', 'abstract', 'snippet', 'headline'],1, inplace=True)
    dr = df.apply(lambda x: len(x['keywords']) == 0, axis=1)
    df.drop(df[dr].index, inplace=True)

    df['topics'] = df.apply(lambda x: keywords(x), axis=1)
    dr = df.apply(lambda x: len(x['topics']) == 0, axis=1)
    df.drop(df[dr].index, inplace=True)
    df.drop('keywords'.index, inplace=True)
    df = df.explode('topics', ignore_index=True)
    data = pd.concat([data, df], ignore_index=True)
    
    
    
# df =  df.groupby('topics').filter(lambda x : len(x)>50)


