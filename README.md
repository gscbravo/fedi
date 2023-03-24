# fedi

## About

A simple feed for the most recent posts on the
[Fediverse](https://en.wikipedia.org/wiki/Fediverse). It uses the Mastodon
API to get the most recent 40 posts. There's an option to preview media
attachments.

## Usage

```
pip3 install -r requirements.txt
cd src
flask run
```

When in production, use a WSGI server such as [Gunicorn](https://gunicorn.org/)
with [Nginx](https://nginx.org/).

