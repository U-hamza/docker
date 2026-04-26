
from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/count")
def count():
    visits = r.incr("counter")
    return render_template("index.html", visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)



