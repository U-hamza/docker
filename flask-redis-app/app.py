from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return "Welcome to the Flask + Redis App!"

@app.route("/count")
def count():
    visits = r.incr("counter")
    return f"Visit count: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)