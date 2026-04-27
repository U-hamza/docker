## Docker Assignment


# Objective 
To create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application must use Redis to store and retrieve data.


# Requirements 
Flask Web Application:

- A Flask app that has two routes:
    /: Displays a welcome message.
    /count: Increments and displays a visit count stored in Redis.
- Redis Database:
  Use Redis as a key-value store to keep track of the visit count.
- Dockerize Both Services:
  Create Dockerfiles for both the Flask app and Redis.
  Use Docker Compose to manage the multi-container application.


# 1. Project structure 
I followed the structure shown below to avoid errors from occuring later. 

flask-redis-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml


# 2. Flask application code
- Within your app folder create the file: app.py
- The following was coded with python and redis was used as its database
- Choose what port to run your code. In this case port 5001 was used.


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



# 2. Create requirements.txt file
- Withing the app folder create a requirements.txt file and insert flask and redis.
- This file is a must for managing Python dependencies
- 

<img width="763" height="330" alt="Screenshot 2026-04-27 at 19 33 47" src="https://github.com/user-attachments/assets/1625c3bc-7d14-427e-ae95-fc16ac37d014" />

<br/>


# 3. Create flask dockerfile
- The dockerfile was created with the following code:

<img width="639" height="353" alt="Screenshot 2026-04-27 at 19 36 59" src="https://github.com/user-attachments/assets/66685e9b-dbe4-46d2-bc68-7d4feb15724e" />

<br/>


# 4. Redis container
- Although the objective states make two dockerfiles, redis image can be used automatically from Dockerhub.
- redis: 7 (this was used and inserted into the docker compose file which will be shown below)


# 5. Create Docker Compose 
- Create the file outside the app folder but within the project folder.
- create docker-compose.yml
- The following code was used to create the file:


services:
  web:
    build: ./app
    container_name: flask_app2
    ports:
      - "5001:5001"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis

  redis:
    image: redis:7
    container_name: redis_db
    ports:
      - "6379:6379"


# 6. Run the application
- From the project root which in this case is flask-redis-app, run docker compose up  --build
- For more clarity go to the terminal: cd into project root and then run docker compose up --build

# 7. Test the application
- Run the application on your local port and you should see the welcome message
- Click the visit button to ensure that it goes up with every click or page refresh


<img width="1224" height="736" alt="Screenshot 2026-04-27 at 19 50 22" src="https://github.com/user-attachments/assets/13b8a1a3-bde0-4987-93a8-2fbe2202fa51" />

<br/>


<img width="1368" height="533" alt="Screenshot 2026-04-27 at 19 50 41" src="https://github.com/user-attachments/assets/651eac53-358c-4c1f-9c13-53dcc257d260" />

<br/>


# 8. Use HTML and CSS to be creative (optional)
- This is optional and in my case it was used because previous web development background.
- 










