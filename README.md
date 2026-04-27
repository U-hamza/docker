# Docker Assignment


## Objective 
To create a multi-container application that consists of a simple Python Flask web application and a Redis database. The Flask application must use Redis to store and retrieve data.


## Requirements 
Flask Web Application:

- A Flask app that has two routes:
  -  /: Displays a welcome message.
  -  /count: Increments and displays a visit count stored in Redis.
- Redis Database:
  Use Redis as a key-value store to keep track of the visit count.
- Dockerise Both Services:
  Create Dockerfiles for both the Flask app and Redis.
  Use Docker Compose to manage the multi-container application.


## 1. Project structure 
I followed the structure shown below to avoid errors from occuring later. 

<img width="263" height="179" alt="Screenshot 2026-04-27 at 19 18 00" src="https://github.com/user-attachments/assets/a7b07030-8c32-4158-b727-d19cbbefc603" />

<br/>

## 2. Flask application code
- Within your app folder create the file: app.py
- The following was coded with python and redis was used as its database.
- Choose what port to run your code. In this case port 5001 was used.


<img width="555" height="565" alt="Screenshot 2026-04-27 at 20 12 27" src="https://github.com/user-attachments/assets/517bf695-e588-4de3-b640-5d3b20d57405" />


<br/>



## 2. Create requirements.txt file
- Withing the app folder create a requirements.txt file and insert flask and redis.
- This file is a must for managing Python dependencies.
  

<img width="763" height="330" alt="Screenshot 2026-04-27 at 19 33 47" src="https://github.com/user-attachments/assets/1625c3bc-7d14-427e-ae95-fc16ac37d014" />

<br/>


## 3. Create Flask Dockerfile
- The dockerfile was created with the following code:

<img width="639" height="353" alt="Screenshot 2026-04-27 at 19 36 59" src="https://github.com/user-attachments/assets/66685e9b-dbe4-46d2-bc68-7d4feb15724e" />

<br/>


## 4. Redis Container
- Although the objective states make two dockerfiles, redis image can be used automatically from Dockerhub.
- redis: 7 (this was used and inserted into the docker compose file which will be shown below)


## 5. Create Docker Compose 
- Create the file outside the app folder but within the root project folder.
- Create docker-compose.yml
- The following code was used to create the file:


<img width="635" height="590" alt="Screenshot 2026-04-27 at 19 56 21" src="https://github.com/user-attachments/assets/4d0c0405-50c6-4e69-9c6e-4f70ce4c2d69" />

<br/>



## 6. Run the application
- From the project root which in this case is flask-redis-app, run docker compose up  --build.
- For further clarity go to the terminal: cd into project root and then run docker compose up --build.

## 7. Test the application
- Run the application on your local port and you should see the welcome message.
- Click the visit button to ensure that it goes up with every click or page refresh.


<img width="1224" height="736" alt="Screenshot 2026-04-27 at 19 50 22" src="https://github.com/user-attachments/assets/13b8a1a3-bde0-4987-93a8-2fbe2202fa51" />

<br/>


<img width="1368" height="533" alt="Screenshot 2026-04-27 at 19 50 41" src="https://github.com/user-attachments/assets/651eac53-358c-4c1f-9c13-53dcc257d260" />

<br/>


## 8. Use HTML and CSS to be creative (optional)
- This is optional but effective to create a more user-friendly interface
- Create a templates folder, and then create a file index.html.
- Create a static folder, and then crease a file style.css
- Use a similar structure to the one below. If the structure is incorrect, flask will not be able to run it.


<img width="245" height="260" alt="Screenshot 2026-04-27 at 19 59 18" src="https://github.com/user-attachments/assets/dc60a080-e252-43e8-b961-a6395b7ca548" />

<br/>

- Templates and statics folders names should be not be altered otherwise flask will not be able to detect the HTML and CSS files.
- HTML file must have static name present in the href as shown below.

<img width="883" height="54" alt="Screenshot 2026-04-27 at 20 02 51" src="https://github.com/user-attachments/assets/8e6328dc-1d01-4ed2-9ac9-a4f7674f3c0a" />

<br/>

- If you are familiar with HTML and CSS then customise as you wish.
- Alter the app.py file, which will allow flask to detect the HTML file.

 <img width="710" height="628" alt="Screenshot 2026-04-27 at 20 09 44" src="https://github.com/user-attachments/assets/f967cc16-09f3-4ff5-9b38-21a3958c37ba" />

<br/>

- Finally, run on your local port and the HTML and CSS changes should automatically be applied.




## Challenges 
I faced several challenges, particularly with configuring Docker and ensuring the correct project structure. I initially struggled with file paths and build contexts, especially when the Docker Compose file was not in the expected location, which caused errors when running the application. Linking the HTML and CSS correctly in Flask also required careful attention to folder naming and file references. In addition, I encountered issues when pushing my work to GitHub, such as incorrect remote URLs and authentication problems. Overcoming these challenges helped me develop a better understanding of debugging, and containerisation.


## What I learnt
Through this project, I learned how to build and containerise a multi-service web application using Docker and Docker Compose. I developed a basic Flask application and integrated it with a Redis database to store and retrieve data, which helped me understand how different services communicate within a shared network. I also gained experience structuring a project correctly, linking HTML and CSS for a more user-friendly interface, and troubleshooting common issues related to file paths, containers, and configuration. Additionally, I improved my understanding of version control by managing changes and pushing my work to GitHub.













