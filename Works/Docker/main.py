from flask import Flask
from redis import Redis


app = Flask(__name__)
redis_client = Redis(host='redis_service', port = 6379)


@app.route('/')
def index():
    hits = redis_client.incr('hits')
    return f'<h1> Hello, Docker! <br> {hits} defe muraciet edilib </h1>'

if __name__ == '__main__':
    app.run(debug=True)