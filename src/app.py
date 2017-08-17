import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Set this stuff from environment vars?
app_base = '/trump-tweet/'
content_root = os.path.join(os.getcwd(), 'trump-tweet-app', 'build')

@app.route(app_base + 'content/<path:filename>')
def content(filename):
    return send_from_directory(os.path.join(content_root), filename)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)