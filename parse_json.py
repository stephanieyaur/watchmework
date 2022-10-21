import json

def parse_js(file):
    f = open(file)
    dat = json.load(f)
    f.close()
    ret = {
        "search": dat["webPages"]["webSearchUrl"],
        "summary": dat["entities"]["value"][0]["description"],
        "results": dat["webPages"]["value"]
    }
    return json.dumps(ret, indent=4)
    #return (dat["entities"]["value"][0]["description"], dat["webPages"]["value"][0]["displayUrl"])

if __name__ == '__main__':
    parsed_res = parse_js('formatted_results.json')
    print(parsed_res)