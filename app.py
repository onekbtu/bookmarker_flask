from bleach import clean
from flask import Flask, request

app = Flask(__name__)


@app.route(rule='/', methods=('POST',))
def hello_world():
    content = request.get_json()['content']
    print(
        clean(content, tags=[], attributes={}, styles=[], strip=True)
    )
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
