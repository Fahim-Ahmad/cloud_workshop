# Cloud Workshop

In this workshop, you will explore and try Cloud Technology. You should have knowledge of Python, algorithms, and computational thinking. You may know SDLC and Data Science. Probably, you have written a lot of code. This workshop will focus on what happens after your code leaves your local computer, in theory and practice.

## Objectives

After the workshop:

### Networking

- You can explain what happens when you enter a site name in your browser.
- You know about the 7 layers of networking to an extent a programmer should know.
- You understand how a program on your computer reaches other computers through the Internet.
- You can explain application layer GET and POST requests and responses.
- You understand what API means and how it works.

### Cloud Technology

- You can describe the differences between on-premises and Cloud Infrastructure.
- You know the main cloud providers today: AWS, GCP, and Azure.
- You know the difference between IaaS, PaaS, SaaS.
- You can explain what it means for an application to be deployed on the cloud.
- You can decide if the Cloud is needed for your tasks.
- You know and can describe common Cloud services:
    - Computing
    - Storage
    - Networking
- You understand load balancing and scalability.
- You know how to control and limit your costs in Cloud
- You know how the Cloud could be used for ML and Data Science.

### Deployment

- You can create an account on Google Cloud Platform.
- You can start a virtual machine (VM) on GCP.
- You can log in to this machine, clone your code, install packages, and run your application as a service.
- You can obtain an IP address of your VM with a working application and share it.

## Prep work (optional)

How to prepare before the workshop, to get the most out of it:

- Create a free account on the [Google Cloud Platform](https://cloud.google.com/?hl=en).
- Spend some time there to explore the interface.
- If you want to practice deploying your own application during the workshop, you should follow these steps:
    - Make your application a web application. If you are new to this, please explore [basic Flask application](helloworld) provided with this workshop. You can modify the code of the `my_basic_computation` function in the `app.py` module, edit the HTML template to add your desired functionality. In the application [README](helloworld/README.md), you can find more detail. 
    - If you need additional packages for your app, add them to `requirements.txt`. You can generate `requirements.txt` using pip:
    ```bash
    pip freeze > requirements.txt
    ```
    - Create a GitHub repository and push your working app there.
    - Try cloning the repository to a new folder (or project in an IDE), installing packages, running your code:
    ```bash
    pip install -r requirements.txt
    flask run
    ```
    and ensuring everything works as should be.


## Workshop Outline

### Icebreaker & Workshop Overview (all together)

> ~5 min

The workshop instructor enters the web browser and enters the name of any site. The site context is displayed in the browser.
Question for a 5-minute discussion:
- What just happened?

After discussion, the workshop instructor provides an understandable answer if needed and introduces the outline of this workshop. 

### Networking (all together)

> ~ 8 min

- Introduction to the [networking learning objectives](README.md#networking).
- 7 layer network architecture (with a focus on the application layer)
- Requests and responses
- API
- Discussion: how much should a programmer/data scientist know about networking?

### Cloud (all together)

> ~ 12 mins

- Introduction to the [cloud learning objectives](README.md#cloud-technology).
- What cloud is. Difference between local infrastructure and clouds. 
- History note. GCP, AWS, Azure.
- Types of cloud services: IaaS, PaaS, SaaS
- Example of deployed application (explanation and scheme of online shopping application working in the cloud)
- Discussion: do we always need cloud for our applications?
- Pros and cons of Cloud

### Deployment demonstration (all together)

> ~ 12 mins

Instructor introduces the [deployment objectives](README.md#deployment).
Instructor shows a demonstration:
- starting a VM in Google Cloud Platform
- entering into it with SSH, cloning the [helloworld](helloworld) repository
- installing Flask and gunicorn (note about why do we need it)
- running gunicorn with the application as a service
- getting the IP address of VM with the working application, 
You will be able to reach just-deployed application from your local device using this IP address.

### Deployment breakout activity (small groups) 

> ~ 20 mins

You will repeat the process, either with your prepared app or with the proposed sample application. Each group could be provided with application to deploy. You are not expected to finish all the required steps, but it is a reachable goal. You will be provided with step-by-step instruction and commands for deployment. In case you did not have enough time, you can finish deployment after the workshop.
In the end, you will obtain an IP address with a working application you can share.
- Breakout discussion

### More on cloud (all together)

> ~ 12 mins

- Note about Cloud costs, free tier, billing, and setting limits
- Cloud services: Computing, Storage, Networking
- Load balancing and Scalability of the Cloud
- Examples / Case studies
- Cloud for ML and AI

### Questions

> ~ 5 mins
