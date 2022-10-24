import json

def _parsewebPages(pages):
    ret = []
    for p in pages:
        res = {
            "title": p["name"],
            "link": p["url"],
            "preview": p["snippet"]
        }
        ret.append(res)
    return ret

def _linktosearch(link):
    return link.split("=")[1].replace("+", " ").replace("%22", "\"")

def parse_js(dat):
    #f = open(file)
    #dat = json.load(f)
    #f.close()
    ret = {
        "searchlink": dat["webPages"]["webSearchUrl"],
        "searchstring": _linktosearch(dat["webPages"]["webSearchUrl"]),
        "summary": dat["entities"]["value"][0]["description"],
        "results": _parsewebPages(dat["webPages"]["value"])
    }
    return json.dumps(ret, indent=4)
    #return (dat["entities"]["value"][0]["description"], dat["webPages"]["value"][0]["displayUrl"])

if __name__ == '__main__':
    f = open('results/formatted_results.json')
    dat = json.load(f)
    f.close()
    parsed_res = parse_js(dat)
    print(parsed_res)

    ### testing the _linktosearch function
    #print(_linktosearch("https://www.bing.com/search?q=%22vincent+van+gogh%22+AND+%22paul+gauguin%22"))