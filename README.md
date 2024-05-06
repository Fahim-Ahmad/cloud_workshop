# Cloud Workshop

In this workshop, you will explore and try Cloud Technology. You are expected to have knowledge of Python, algorithms, and computational thinking. You may know SDLC and Data Science. You have probably written a lot of code. This workshop will focus on what happens after your code leaves your local computer, in theory and practice.

- [Learning Objectives](README.md#learning-objectives)
- [Prep work](README.md#prep-work)
- [Workshop Outline](README.md#workshop-outline)
- [Slides](slides)
- [Deployment to App Engine (that you will use)](Deployment_AppEngine.md)
- [Deployment to Virtual Machine (for advanced study)](Deployment_VM.md)
- [Suggested Study](<Suggested Study.md>)

## Learning Objectives

🥚 Basic objectives are desired and reachable goals for you. 

✔️ Advanced are more complicated topic, and they are important if you want to excel. You should work on them after you are familiar with the 🥚 Basics. 

### Networking

Basics:
- 🥚 You can explain what happens when you enter a site name in your browser.
- 🥚 You know about the 7 layers of networking.
- 🥚 You understand how a program on your computer communicate with other computers via Internet.
- 🥚 You can explain what is a web application.

Advanced:
- ✔️ You can explain application layer requests and responses, and know what is GET and POST.
- ✔️ You know what IP address means, and how string addresses are processes in the Internet.
- ✔️ You understand what API means and how it works.
- ✔️✔️ You can make a simple Flask application.

### Cloud Technology

Basics:
- 🥚 You can describe the differences between on-premises and Clouds Infrastructure.
- 🥚 You know the main cloud providers today: AWS, GCP, and Azure.
- 🥚 You can explain what it means for an application to be deployed on the cloud.
- 🥚 You can decide if the Cloud is needed for your tasks.
- 🥚 You have the idea of costs in Cloud.
- 🥚🥚 You know how the Cloud Technology is used for ML and Data Science.

Advanced:
- ✔️ You know how to control and limit your costs in Cloud, and what offers free tier. 
- ✔️ You know the difference between IaaS, PaaS, SaaS.
- ✔️ You know and can describe common Cloud services:
    - Computing
    - Storage
    - Networking
- ✔️✔️ You understand the difference between different deployment options.
- ✔️✔️ You understand load balancing and scalability.


### Deployment

- 🥚 You can create an account and login on Google Cloud Platform console.
- 🥚 You can navigate in Google Cloud Platform console
- 🥚🥚 You now several options for deploying application to cloud
- ✔️ You can configure you application for deploying to Google App Engine.
- ✔️ You can deploy your to Google App Engine.
- ✔️✔️ You can use additional Google Cloud service for your needs


## Prep work

Basic part:

- 🥚 Create a free account on the [Google Cloud Platform](https://cloud.google.com/?hl=en).
- 🥚 Spend some time there to explore the interface.


🥚 [**You can watch guide video 1, covering the basic preparation work for Google Cloud Platform**](https://drive.google.com/file/d/1palgfhF2oDtJNOHNVLKc7gaqhriFsTS9/view?usp=drive_link)

- 🥚 Read about web applications.
- 🥚🥚 Get the general understanding of Flask framework.


🥚 [**You can watch guide video 2, about web application and explanation of Flask framework**](https://drive.google.com/file/d/1M4OA7-_yBLbbq6_ukxWJXdKjbbGMiSRk/view?usp=drive_link)

Advanced part. During the workshop you will work in small groups to deploy a simple web application, similar to the demonstration part. If you find this interesting, you can get more out of the workshop and prepare your own code as a web application for deployment. 
- ✔️ Explore provided [basic Flask application](helloworld). 
- ✔️ Modify the code of the `my_basic_computation` function in the `app.py` module, edit the HTML template to add your desired functionality. 
- ✔️ If you are using additional packages for your app, add them to `requirements.txt`. Run this command from your application directory and it will make `requirements.txt` with only modules you use
```bash
pip install pipreqs
pipreqs .
```
if you face some issues there is a classic way for generating `requirements.txt`, but it may generate a bigger file:
```bash
pip freeze > requirements.txt
```
- ✔️ Create a GitHub repository and push your working app there.
- ✔️ Try cloning your app repository to a new folder (or project in an IDE), installing packages, running your code:
```bash
git clone <your_repo_name>
cd <your_repo_name>
pip install -r requirements.txt
flask run
```
- ✔️ Ensuring your web application is working properly.

✔️ [**You can watch guide video 3, with example of making a simple Flask application**](https://drive.google.com/file/d/1bCbOs40nZXfOggHYOHZQxJyG3pqSViIp/view?usp=drive_link)


## Workshop Outline

### Icebreaking & Workshop Overview (all together)

> ~5 min

The workshop instructor enters the web browser and enters the name of any site. The site context is displayed in the browser.
Question for a 5-minute discussion:
- What just happened?

After discussion, the workshop instructor provides an understandable answer if needed and introduces the outline of this workshop. 

### Networking (all together)

> ~ 10 min

- Introduction to the [networking learning objectives](README.md#networking).
- 7 layer network architecture (with a focus on the application layer)
- Requests and responses
- API
- Web application, Flask
- Discussion: how much should a programmer/data scientist know about networking?

### Cloud (all together)

> ~ 15 mins

- Introduction to the [cloud learning objectives](README.md#cloud-technology).
- Discussion - what cloud services we use daily?
- What cloud is. Difference between local infrastructure and clouds. 
- History note. GCP, AWS, Azure.
- Types of cloud services: IaaS, PaaS, SaaS.
- Several ways of deploying an application to cloud.
- Discussion: do we always need cloud for our applications?
- Pros and cons of Cloud

### Deployment demonstration (all together)

> ~ 12 mins

Instructor introduces the [deployment objectives](README.md#deployment).
Instructor shows a demonstration, taking steps described in [Deployment](Deployment_AppEngine.md) document.

You will be able to reach just-deployed application from your local device using the address, that will be shared.

### [Deployment breakout activity](Deployment_AppEngine.md) (small groups) 

> ~ 20 mins

You will work in small groups to repeat the deployment process.
You will either deploy your prepared app or provided sample application. You are not expected to finish all the required steps, but it is a reachable goal. In case you did not have enough time, you can finish deployment after the workshop.

All required steps and commands are described in this [Deployment](Deployment_AppEngine.md) document.

In the end, you will obtain an address with a working application you can share.

After breakout:
- Sharing your deployed applications, and seeing each other work
- Breakout discussion

### More on cloud (all together)

> ~ 12 mins

- Advanced topic for App Engine Deployment - Storage, CI/CD
- Note about Cloud costs, free tier, billing, and setting limits
- Cloud services: Computing, Storage, Networking
- Cloud for ML
- Big Data
- Cloud Marketplace
- Scaling, Load Balancing, Kubernetes
- Examples / Case studies - big scale services, deployed in Cloud. (i.e. Spotify)

### Questions

> ~ 5 mins
