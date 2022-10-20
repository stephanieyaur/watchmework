import logging
# from Bing_API import *
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    text = req.get_body().decode()
    # # name = req.params.get('name')
    # # if not name:
    # #     try:
    # #         req_body = req.get_json()
    # #     except ValueError:
    # #         pass
    # #     else:
    # #         name = req_body.get('name')
    return func.HttpResponse(text)