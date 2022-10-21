import flask
from keyword_extract import *
from Bing_API import *
from keyword_extract import *
from parse_json import *
app = flask.Flask(__name__)

@app.route('/<string:paragraph>', methods=['GET'])
def get_results(paragraph):
    keyword = extract_ent(paragraph)[0]
    results = bing_api(keyword)
    p_results = parse_js(results)
    return p_results


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")