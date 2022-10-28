import gensim
import nltk
import re
from gensim import corpora
from gensim.models.ldamodel import LdaModel
nltk.download('stopwords')
from nltk.corpus import stopwords
from pprint import pprint

example_doc = "Chicago, on Lake Michigan in Illinois, is among the largest cities in the U.S. Famed for its bold architecture, it has a skyline punctuated by skyscrapers such as the iconic John Hancock Center, 1,451-ft. Willis Tower (formerly the Sears Tower) and the neo-Gothic Tribune Tower. The city is also renowned for its museums, including the Art Institute of Chicago with its noted Impressionist and Post-Impressionist works. Lori Elaine Lightfoot is an American attorney and politician serving since 2019 as the 56th mayor of Chicago. She is a member of the Democratic Party. Before becoming mayor, Lightfoot worked in private legal practice as a partner at Mayer Brown and held various government positions in Chicago. The Bulls are the basketball located in Chicago. Players on the team include Demar DeRozen, and the team made it to the first round of the playoffs last year."

def get_topics(doc):
    sentences = doc.split('. ')
    stop_words = stopwords.words('english')
    words = [[word for word in sentence.split(' ') if word not in stop_words] for sentence in sentences]
    dictionary = corpora.Dictionary(words)
    mycorpus = [dictionary.doc2bow(sentence, allow_update=True) for sentence in words]


    model = LdaModel(corpus=mycorpus, 
                    id2word=dictionary, 
                    num_topics=1,
                    random_state=100,
                    update_every=1,
                    chunksize=100,
                    passes=10,
                    alpha='auto',
                    per_word_topics=True)


    topics = model.show_topics()
    main_topic = re.split("\*|\+", topics[0][1])[1]
    return main_topic


example_topic = get_topics(example_doc)
print(example_topic)