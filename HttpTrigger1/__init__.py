import logging

import azure.functions as func
from Bing_API import *
from keyword_extract import *
from IBM_api import *
from parse_json import *
from scrapewiki import *

def remove_dup(resources, entities, wiki_list):
    for e in resources:
        i = 0
        while i < len(e):
            if "wikipedia" in e[i]['link'] and (e[i]['title'].split(' - ')[0] in entities or e[i]['link'] in wiki_list):
                e.remove(e[i])   
                continue
            for e2 in resources[resources.index(e):]:
                i2 = 0 if e2 != e else e2.index(e[i])+1
                while i2 < len(e2):
                    if e[i]['link'] == e2[i2]['link'] or e[i]['title'] == e2[i2]['title']:
                        e2.remove(e2[i2])
                        continue
                    i2 += 1
            i+=1
    return resources


def main(req: func.HttpRequest) -> func.HttpResponse:

    body = req.get_body().decode()
    body = json.loads(body)
    paragraph = body['paragraph']
    doc = body['doc']
  
    topics, entities = get_analysis(doc, paragraph)
    entities = entities[:5]
    resources = []
    info = []
    del_list = []
    wiki_links = []
    for e in entities:
        results =  scrape_wiki(e)
        if results == {}:
            del_list.append(e)
            continue
        info.append(results[0])
        wiki_links.append(results[1])

    for i in del_list:
        entities.remove(i)

    for e in entities:
        for t in topics[:5]:
                query = e + ' ' + t
                results = bing_api(query)
                resources.append(parse_js(results))
    resources = remove_dup(resources, entities, wiki_links)

    return func.HttpResponse(
            json.dumps({"entities": info,"results": resources}),
            status_code=200
    )
