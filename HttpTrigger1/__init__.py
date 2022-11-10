import logging

import azure.functions as func
from Bing_API import *
from keyword_extract import *
from IBM_api import *
from parse_json import *
from scrapewiki import *


def main(req: func.HttpRequest) -> func.HttpResponse:

    body = req.get_body().decode()

    body = json.loads(body)
    paragraph = body['paragraph']
    doc = body['doc']
  
    topics, entities = get_analysis(doc, paragraph)
    topics = topic_parse(topics)
    entities = entity_parse(entities)
    entities = entities[:3]
    resources = []
    info = []
    for e in entities:
        info.append(scrape_wiki(e))
    for e in entities:
        for t in topics:
                query = e + ' ' + t
                results = bing_api(query)
                resources.append(parse_js(results))

    return func.HttpResponse(
            json.dumps({"entities": info,"results": resources}),
            status_code=200
    )
