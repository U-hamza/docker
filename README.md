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

<img width="263" height="179" alt="Screenshot 2026-04-27 at 19 18 00" src="https://github.com/user-attachments/assets/a7b07030-8c32-4158-b727-d19cbbefc603" />

<br/>

# 2. Flask application code
- Within your app folder create the file: app.py
- The following was coded with python and redis was used as its database
- Choose what port to run your code. In this case port 5001 was used.


<img width="765" height="635" alt="Screenshot 2026-04-27 at 19 55 36" src="https://github.com/user-attachments/assets/172f8d71-459a-4f9c-9a7c-9d8e45d8b06d" />

<br/>



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


<img width="635" height="590" alt="Screenshot 2026-04-27 at 19 56 21" src="https://github.com/user-attachments/assets/4d0c0405-50c6-4e69-9c6e-4f70ce4c2d69" />

<br/>



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
- This is optional and in my case it was used because of previous web development background.
- Create a templates folder, and then create a file index.html
- Create a static folder, and then crease style.css
- Use a similar structure to the one below. If the structure is in correct, flask will not be able to run it.


<img width="245" height="260" alt="Screenshot 2026-04-27 at 19 59 18" src="https://github.com/user-attachments/assets/dc60a080-e252-43e8-b961-a6395b7ca548" />

<br/>

- templates and statics folders names should be not be altered otherwise flask will not be able to detect the HTML and CSS files.
- HTML file must have static name present in the href as shown below.

<img width="883" height="54" alt="Screenshot 2026-04-27 at 20 02 51" src="https://github.com/user-attachments/assets/8e6328dc-1d01-4ed2-9ac9-a4f7674f3c0a" />

<br/>

- If you are familiar with HTML and CSS then customise as you wish. 











