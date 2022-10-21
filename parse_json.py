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

def parse_js(file):
    f = open(file)
    dat = json.load(f)
    f.close()
    ret = {
        "search": dat["webPages"]["webSearchUrl"],
        "summary": dat["entities"]["value"][0]["description"],
        "results": _parsewebPages(dat["webPages"]["value"])
    }
    return json.dumps(ret, indent=4)
    #return (dat["entities"]["value"][0]["description"], dat["webPages"]["value"][0]["displayUrl"])

if __name__ == '__main__':
    parsed_res = parse_js('results/formatted_results.json')
    print(parsed_res)