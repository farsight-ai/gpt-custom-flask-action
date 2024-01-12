from flask import Flask, make_response, request
from flask_cors import CORS
import requests
import re

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Health check
@app.route('/')
def health_check():
    return make_response("Healthy.", 200)

# This is not included in the blog for simplicity's sake, but cleans up
# the content a bit before sending it back to the GPT.
def remove_html_tags_and_whitespace(html):
    content = re.sub(r"\<.*?\>|[\t\n]", "", html)
    return content

# Fetches HTML from any given url. Expects the url to be a query parameter.
@app.route('/fetch-html', methods=["GET"])
def fetch_html():
    url = request.args.get('url')
    page = requests.get(url)
    html_text = page.text
    encoded_html = html_text.encode(page.encoding)
    decoded_html = encoded_html.decode(page.encoding)
    html_content = remove_html_tags_and_whitespace(decoded_html)

    return make_response({"html": html_content}, 200)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)