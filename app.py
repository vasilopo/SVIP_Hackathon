from flask import Flask, request

from helpers.app_helpers import classifier

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return 'Welcome to our Mask Classification System! ' \
           'To use the system please post a photo on /has_mask under name image.'


@app.route('/has_mask', methods=['POST'])
def has_mask():
    return classifier(request.files['image'])


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
