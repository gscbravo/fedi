from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # show media attachments
    media = '1' if request.args.get('media', '') == '1' else ''

    # fediverse server
    url = 'https://mastodon.social'

    # get posts
    response = requests.get(f'{url}/api/v1/timelines/public?limit=40')
    posts = response.json()

    return render_template('index.html', posts=posts, media=media)

if __name__ == '__main__':
    app.run()

