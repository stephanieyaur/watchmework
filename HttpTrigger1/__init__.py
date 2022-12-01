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
        key = list(e.keys())[0]
        while i < len(e[key]):
            if "wikipedia" in e[key][i]['link'] and (e[key][i]['title'].split(' - ')[0] in entities or e[key][i]['link'] in wiki_list):
                e[key].remove(e[key][i])   
                continue
            for e2 in resources[resources.index(e):]:
                key2 = list(e2.keys())[0]
                i2 = 0 if e2 != e else e2[key2].index(e[key][i])+1
                while i2 < len(e2[key2]):
                    if e[key][i]['link'] == e2[key2][i2]['link'] or e[key][i]['title'] == e2[key2][i2]['title']:
                        e2[key2].remove(e2[key2][i2])
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
    resource_list = []
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
        resource_list = [] 
        for t in topics[:5]:
                query = e + ' ' + t
                results = bing_api(query)
                resource_list.extend(parse_js(results))
        
        resources.append({e:resource_list})
            
    resources = remove_dup(resources, entities, wiki_links)

    return func.HttpResponse(
            json.dumps({"entities": info,"results": resources}),
            status_code=200
    )
