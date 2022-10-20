import flask
from keyword_extract import *
from Bing_API import *
from keyword_extract import *
app = flask.Flask(__name__)

@app.route('/<string:paragraph>', methods=['GET'])
def get_results(paragraph):
    keyword = extract_ent(paragraph)[0]
    results = bing_api(keyword)
    return results


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")