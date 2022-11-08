import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
import Features, CategoriesOptions, EntitiesOptions


api_key = 'mTAM4m9Xd1tUGg-iFXxlIVq1GKX0JbMkM4MUZVHL0trs'
service_url = 'https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/0e13ef0f-3489-4f56-b11e-4d2b14b54c91'

def get_topics(document):
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(service_url)

    response = natural_language_understanding.analyze(
        text=document,
        features=Features(categories=CategoriesOptions(limit=10))
    ).get_result()

    return response

def get_entities(paragraph):
    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(service_url)

    response = natural_language_understanding.analyze(
        text=paragraph,
        features=Features(entities=EntitiesOptions(limit = None))
    ).get_result()

    return response


if __name__ == '__main__':
    paragraph = 'Chicago, on Lake Michigan in Illinois, is among the largest cities in the United States. Known for its bold architecture, it has a skyline punctuated by skyscrapers such as the iconic John Hancock Center, 1,451-ft. Willis Tower (formerly the Sears Tower) and the neo-Gothic Tribune Tower. The city is also renowned for its museums, including the Art Institute of Chicago with its noted Impressionist and Post-Impressionist works. Lori Elaine Lightfoot is an American attorney and politician serving since 2019 as the 56th mayor of Chicago. She is a member of the Democratic Party. Before becoming mayor, Lightfoot worked in private legal practice as a partner at Mayer Brown and held various government positions in Chicago. The Bulls are the basketball located in Chicago. Players on the team include Demar DeRozen, and the team made it to the first round of the playoffs last year.'
    topics = get_topics(paragraph)
    entities = get_entities(paragraph)
    print("ENTITIES:")
    print(entities['entities'])
    print("CATEGORIES:")
    print(topics["categories"])

