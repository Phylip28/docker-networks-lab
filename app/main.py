from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, decode_responses=True)

@app.route("/")
def index():
    visits = r.incr("counter")
    return f"Hello! This page has been visited {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
