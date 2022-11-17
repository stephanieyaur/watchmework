import logging

import azure.functions as func
from Bing_API import *
from keyword_extract import *
from IBM_api import *
from parse_json import *
from scrapewiki import *

def remove_dup(resources, entities, wiki_list):
    for i in resources:
        for res in i['results']:
            if "wikipedia" in res['link'] and (res['title'].split(' - ')[0] in entities or res['link'] in wiki_list):
                i['results'].remove(res)
                continue
            for j in resources[resources.index(i)+1:]:
                for res2 in j['results']:
                  

                    if res['link'] == res2['link'] or res['title'] == res2['title']:
                        j['results'].remove(res2)
    return resources

def main(req: func.HttpRequest) -> func.HttpResponse:

    body = req.get_body().decode()
    body = json.loads(body)
    paragraph = body['paragraph']
    doc = body['doc']
  
    topics, entities = get_analysis(doc, paragraph)
    topics = topic_parse(topics)
    entities = entity_parse(entities)
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
