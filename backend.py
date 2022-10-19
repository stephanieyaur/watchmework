import flask
from keyword_extract import *
from Bing_API.py import *

app = flask.Flask(__name__)

@app.route('/<string:paragraph>', methods=['GET'])
def get_results(paragraph):
    # DO KEYWORD EXTRACTION AND CALL SEARCH API
    return paragraph


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")