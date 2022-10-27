import json

def _parsewebPages(dat):
    ret = []
    if "webPages" in dat:
        for p in dat["webPages"]["value"]:
            res = {
                "title": p["name"],
                "link": p["url"],
                "preview": p["snippet"]
            }
            ret.append(res)
    return ret

def _linktosearch(link):
    return link.split("=")[1].replace("+", " ").replace("%22", "\"")

def _stringtolink(string):
    return "https://www.bing.com/search?q="+string.replace(" ", "+").replace("\"", "%22")

def _getsummary(dat):
    if "entities" in dat:
        return dat["entities"]["value"][0]["description"]
    else:
        return ""

def parse_js(dat):
    #f = open(file)
    #dat = json.load(f)
    #f.close()
    ret = {
        "searchstring": dat["queryContext"]["originalQuery"],
        "searchlink": _stringtolink(dat["queryContext"]["originalQuery"]),
        "summary": _getsummary(dat),
        "results": _parsewebPages(dat),
    }
    return ret
    #return (dat["entities"]["value"][0]["description"], dat["webPages"]["value"][0]["displayUrl"])

if __name__ == '__main__':
    f = open('results/formatted_results.json')
    dat = json.load(f)
    f.close()
    parsed_res = parse_js(dat)
    print(parsed_res)

    ### testing the _linktosearch function
    #print(_linktosearch("https://www.bing.com/search?q=%22vincent+van+gogh%22+AND+%22paul+gauguin%22"))