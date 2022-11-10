from google.cloud import language
from google.oauth2 import service_account


def get_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print(entity)

from google.cloud import language_v1

def get_topics(text_content):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    content_categories_version = (
        language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2)

    response = client.classify_text(request = {
        "document": document,
        "classification_model_options": {
            "v2_model": {
                "content_categories_version": content_categories_version
            }
        }
    })

    for category in response.categories:
        print(u"Category name: {}".format(category.name))
        print(u"Confidence: {}".format(category.confidence))


text = "Chicago, on Lake Michigan in Illinois, is among the largest cities in the U.S. Famed for its bold architecture, it has a skyline punctuated by skyscrapers such as the iconic John Hancock Center, 1,451-ft. Willis Tower (formerly the Sears Tower) and the neo-Gothic Tribune Tower. The city is also renowned for its museums, including the Art Institute of Chicago with its noted Impressionist and Post-Impressionist works. Lori Elaine Lightfoot is an American attorney and politician serving since 2019 as the 56th mayor of Chicago. She is a member of the Democratic Party. Before becoming mayor, Lightfoot worked in private legal practice as a partner at Mayer Brown and held various government positions in Chicago. The Bulls are the basketball located in Chicago. Players on the team include Demar DeRozen, and the team made it to the first round of the playoffs last year."
get_topics(text)
print("=====================================================================================================================================")
get_entities(text)