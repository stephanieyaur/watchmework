import webbrowser
import spacy

def extract_ent(text):
    nlp = spacy.load("en_core_web_sm")
    # doc = nlp(text)
    # ents = (list(doc.ents))
    # #labels = [ent.label for ent in ents]
    # #texts = [str(ent) for ent in ents]
    # #texts = list(dict.fromkeys(ents))
    # #print(ents)
    # seen = []
    # for ent in ents:
    #     if ent.label_=='PERSON' or ent.label_=='ORG' or ent.label_=='GPE':
    #         if ent.text.lemma_ not in seen:
    #             print(ent.text, ent.label_)
    #             seen.append(ent.text.lemma_)
    # print(seen)
    doc = nlp(text)
    # for word in sen:
    #     print(word, word.lemma_)
    #q = ""
    ret = []
    for ent in doc.ents:
        #if not (ent.label_=='DATE' or ent.label_=='TIME' or ent.label_=='CARDINAL' or ent.label_=='MONEY' or ent.label_=='QUANTITY' or ent.label_=='PERCENT'):

        #Types of entities: PERSON, GPE (geopolitical: countries, states, city), ORG (organization), WORK_OF_ART, EVENT

        if (ent.label_ == 'PERSON' or ent.label_ == 'GPE' or ent.label_ =='ORG' or ent.label_ =='EVENT' or ent.label_=='WORK_OF_ART'):
            print(ent.text, ent.label_)
            ret.append(ent.text)
            #q = q+ent.text+"+"
    print()
    print("done ent")
    #return q
    if len(ret) == 0: return [text]
    return ret

    
def extract_noun(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    q=""
    for tok in doc:
        #print(tok,tok.pos_)
        if tok.pos_=='PROPN' or tok.pos_=='NOUN':
            print(tok, tok.pos_)
            q = q+tok.text+"+"
    print("done proper noun")
    return q

if __name__ == "__main__":
    print()
    #fd = open('/Users/alextai/Documents/CS338/VanGogh.txt', 'r')
    #fd = open('/Users/alextai/Documents/CS338/Movies.txt', 'r')
    #fd = open('/Users/alextai/Documents/CS338/TheBean.txt', 'r')
    #txt = fd.read()
    #fd.close()
    #txt = "Textrank is a Python tool that extracts keywords and summarises text. The algorithm determines how closely words are related by looking at whether they follow one another. The most important terms in the text are then ranked using the PageRank algorithm. Textrank is usually compatible with the Spacy pipeline. Here are the primary processes Textrank does while extracting keywords from a document."
    
    #IDEA: SEARCH ENTITIES AND NOUNS SEPARATELY
    #IDEA: if work_of_art, use image search. If person, use bing entity search and news search. If place, use map search and news search? If product, use shopping? If org, use news?
    
    txt = "A spectre is haunting cinema – the spectre of animation. In Lev Manovich’s account of ‘digital cinema,’ animation, once banished to the critical and theoretical margins, became the center of modern moving image culture with the advent of digital editing and effects. Each frame of a movie became a mutable painting (rather than an index of reality) and live-action film became just one ingredient in a composite animated image.1 While Manovich’s subsumption of cinema under animation sits uncomfortably in certain contexts,2 it is an excellent starting point for the critical examination of early digital movies that foreground special effects, especially J-horror films like Kiyoshi Kurosawa’s Kairo. In this essay, I will take up a hauntological3 approach to Manovich’s conception of digital cinema to examine the way Kairo portrays, anticipates, and makes terrifying the ubiquity of animated digital media in everyday life, ultimately unsettling the contemporary status of the moving image."
    ents = extract_ent(txt)
    #print(ents[0])
    # for ent in ents:
    #     webbrowser.open_new(url="https://www.bing.com/images/search?q="+ent)

    #fulltxt = txt.replace(" ", "+")
    #webbrowser.open_new(url = "https://www.bing.com/search?q="+fulltxt)

    # noun_query = extract_noun(txt)
    # webbrowser.open_new(url="https://www.bing.com/search?q="+noun_query)