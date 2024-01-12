from flask import Flask, make_response, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Health check
@app.route('/')
def health_check():
    return make_response("Healthy.", 200)

# Fetches HTML from any given url. Expects the url to be a query parameter.
@app.route('/fetch-html', methods=["GET"])
def fetch_html():
    print(request.args)
    url = request.args.get('url')
    print(url)
    page = requests.get(url)
    html_text = page.text
    encoded_html = html_text.encode(page.encoding)
    decoded_html = encoded_html.decode(page.encoding)

    return make_response({"html": decoded_html}, 200)

if __name__ == "__main__":
    app.run('127.0.0.1', port=5000)
