import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = cache.incr('hits')
    return f'''
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1>🚀 Flask + Redis Demo</h1>
        <p style="font-size: 20px;">This page has been visited <b>{count}</b> time(s).</p>
    </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)