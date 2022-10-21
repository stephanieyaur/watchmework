import logging

import azure.functions as func
from Bing_API import *
from keyword_extract import *

def get_results(paragraph):
    keyword = extract_ent(paragraph)[0]
    results = bing_api(keyword)
    return results

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.get_body().decode()
    result = get_results(text)
    return func.HttpResponse(
            json.dumps(result),
            status_code=200
    )
