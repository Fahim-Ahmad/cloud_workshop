## Deployment to Cloud

![gcp logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/330px-Google_Cloud_logo.svg.png)


This manual is for using cloud services of [Google Cloud platform (GCP)](https://cloud.google.com/?hl=en).

# Deployment using Google Cloud App Engine

In this manual, you will go through a step-by-step process of deploying web flask application to Google Cloud App Engine. We will use Standard Environment of App Engine, and configure our app for minimal resource usage. 

This deployment is based on the [Google App Engine Standard for Python3 documentation](https://cloud.google.com/appengine/docs/standard/python3/runtime). 

## [There is a short version of this manual, with much less screenshots](Deployment_AppEngine_short.md)

## Table of Contents

1. [Create account and login to GCP](#1-create-account-and-login-to-gcp)
2. [Enter Google Cloud Shell](#2-enter-google-cloud-shell)
3. [Authorize to GCLOUD command line interface](#3-authorize-to-gcloud-command-line-interface)
4. [Clone your project with Git](#4-clone-your-project-with-git)
5. [Enter project folder and check context](#5-enter-project-folder-and-check-context)
6. [App Engine application structure](#6-app-engine-application-structure)
7. [Open Google Cloud Editor](#7-open-google-cloud-editor)
8. [Prepare your application for deployment](#8-prepare-your-application-for-deployment)
9. [App Engine Deployment](#9-app-engine-deployment)
10. [Visit just created endpoint of your application](#10-visit-just-created-endpoint-of-your-application)
11. [Explore Google Cloud App Engine Console with information and logs](#11-explore-google-cloud-app-engine-console-with-information-and-logs)
12. [Modifying app](#12-modifying-app)
13. [Shutting application down](#13-shutting-application-down)
14. [Advanced topics](#14-advanced-topics)
    1. [Updating your application, CI/CD](#141-updating-your-application-cicd)
    2. [Storage options](#142-storage-options)


## 1. Create account and login to GCP

Go to the [Google Cloud Platform](https://cloud.google.com/) site.

![alt text](images/Deployment_AppEngine/image-34.png)

Press "Get started for free" and follow the registration process.

![alt text](images/Deployment_VM/image-1.png)

You will need to enter your personal data, and credit card for validation, no money will be charged.

You also must specify Tax information: "Personal"

**NOTE**: On payments and costs: GCP requires your credit card to register. It offers [3 month free use, and 300$ credits](https://cloud.google.com/free/docs/free-cloud-features). After free use ends you will not be charged, unless you willingly switch to paid account. So before 3 month trial ends you have nothing to worry about. 

After that, if you switch to paid there is some thing you need to know: there is a so called [free tier](https://cloud.google.com/free/docs/free-cloud-features), that offer a considerable number of services for free. For example it offer running of F1 machine, that we will use for our App Engine Deployment, for total of 28 hours per day.  Having pet project hosted with low performance options costs little, but you have to be careful. By mistake on unknowing you may switch on some costly service you can get charged, so what you should do is set the budget limit in the cloud for example for $1 - %5, so if you reach this amount you will receive e-mail with notification. Setting a budget limit is shown in the tutorial_1 video. 

## 2. Enter Google Cloud Shell 

![alt text](images/Deployment_AppEngine/image.png)

Press on the **Activate Cloud Shell** button on right top of the screen.

You will see cloud shell opening in the bottom of the screen

And after it starts you will the the shell terminal window:

![alt text](images/Deployment_AppEngine/image-32.png)

This is a linux terminal, based on small VM in the Cloud, for you to work with various task.

Try typing in some commands:

![alt text](images/Deployment_AppEngine/image-33.png)

## 3. Authorize to GCLOUD command line interface

In the terminal enter:
```bash
gcloud auth list
```
It may show this window, where you press Authorize

![alt text](images/Deployment_AppEngine/image-21.png)

It may take you you you to pop-up window where you will need to choose your corresponding google account.

![alt text](images/Deployment_AppEngine/image-37.png)

You are authorized.

## 4. Clone your project with Git

Type commands (replace with your repo):
```bash
git clone https://github.com/MIT-Emerging-Talent/cloud_workshop
```
![alt text](images/Deployment_AppEngine/image-38.png)

## 5. Enter project folder and check context

Enter
```bash
cd cloud_workshop
cd helloworld
```
Use `ls` command to see the folder context
```bash
ls
```

You should see the context of your application

![alt text](images/Deployment_AppEngine/image-39.png)

## 6. App Engine application structure

To deploy your application to App Engine app need to have structure similar to the picture, where `app.yaml` is a special configuration file for Google App Engine. You can check the [official docs](https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service#structuring_your_web_service_files) for reference.

![alt text](images/Deployment_AppEngine/image-6.png)

It may contain other files, like python modules.
In the requirements.txt there should at least one line for flask:
```
Flask==3.0.3
```
As in this `helloworld` app. If you use additional libs they should be here.

So you will need to rename `app.py` to `main.py`.
You will need to create `app.yaml` with deployment configuration.
You will need to add `img\` to this configuration file, so application will be able to work with the static files from this folder 
> Note: it is a common way to have all static files in `static\` but now is would require changing code and templates.


## 7. Open Google Cloud Editor

Press **Open Editor** that is next to the right top of the Shell terminal 

![alt text](images/Deployment_AppEngine/image-40.png)

![alt text](images/Deployment_AppEngine/image-41.png)

On some browsers it may say that Editor must be opened in the separate tab, so press **Open in separate tab**

This editor look a lot like VSCode, so navigating there should not be a problem. Folders tab to the left, edit window to the right, and a tool bar like VSCode. 

## 8. Prepare your application for deployment

Let's navigate to our `helloworld` folder with application.

![alt text](images/Deployment_AppEngine/image-42.png)

First, let's rename `app.py` to `main.py`, as required by App Engine.

![alt text](images/Deployment_AppEngine/image-11.png)

![alt text](images/Deployment_AppEngine/image-12.png)

Now let's create `app.yaml`, that is the main configuration for App.

Press **New file**.

![alt text](images/Deployment_AppEngine/image-43.png)

![alt text](images/Deployment_AppEngine/image-44.png)

Now you copy this configuration to your `app.yaml`:

```yaml
# For using Python 3.12
runtime: python312

# The F1 instance class is the basic and lowest-cost instance class available in Google App Engine. 
# It is included in the free tier, making it cost-effective for projects with minimal resource requirements.
instance_class: F1

# We do not expect now any big traffic for our app, so for future cost saving this is most minimal settings.
# However, it's essential to monitor your application's performance and adjust the scaling settings 
# as needed based on actual usage patterns. You may need to change this stetting if your app became popular.
automatic_scaling:
  min_instances: 0
  max_instances: 1

handlers:
  # This configures Google App Engine to serve the files in the app's static
  # directory.
- url: /static
  static_dir: static

  # This configures Google App Engine to use additional img static directory.
- url: /img
  static_dir: img

  # This handler routes all requests not caught above to your main app. It is
  # required when static routes are defined, but can be omitted (along with
  # the entire handlers section) when there are no static files defined.
- url: /.*
  script: auto
```

This code is slightly changed, compared to the presented in [official docs](https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service#configuring_your_web_service_for_app_engine). Here instance_class and scaling is manually specified, and added `img\` static directory. 

![alt text](images/Deployment_AppEngine/image-45.png)

Now let add small modification to our `main.py`

Click on `main.py` and navigate to `my_basic_computation` function

![alt text](images/Deployment_AppEngine/image-46.png)

Change this code line `result_string = internal_variable.title()` as follows:
```python
result_string = internal_variable.title() + ', and Good Luck!!'
```

![alt text](images/Deployment_AppEngine/image-47.png)

Now everything is ready.

## 9. App Engine Deployment

Return to the terminal. If it is open in another tab, just return to this tab, otherwise press **Open Terminal** on the header of the editor window part.

![alt text](images/Deployment_AppEngine/image-48.png)

![alt text](images/Deployment_AppEngine/image-49.png)

and you can see the context of the `helloworld` folder is changed

you can use `cat <filename>` command to print file context to screen
```bash
cat app.yaml
```

![alt text](images/Deployment_AppEngine/image-50.png)

Now lets run the cloud command to deploy our app
```bash
gcloud app deploy
```
It may ask you for the region to create your deployment.

![alt text](images/Deployment_AppEngine/image-30.png)

You can basically choose any region, you may prefer region closer to you. Select **17** us-central for example.

After that, it will ask for confirmation:

![alt text](images/Deployment_AppEngine/image-51.png)

Press Y, and you will see the app is being deployed.

![alt text](images/Deployment_AppEngine/image-52.png)

And after a while, it is done:

![alt text](images/Deployment_AppEngine/image-53.png)


## 10. Visit just created endpoint of your application

Copy address from this line:

![alt text](images/Deployment_AppEngine/image-54.png)

and paste it to the new tab of your browser:

![alt text](images/Deployment_AppEngine/image-55.png)

You can alternatively enter:
```bash
gcloud app browse
```
It will either open new tab with the application address, our output clickable address of it:

![alt text](images/Deployment_AppEngine/image-1.png)


The app is working! 

![alt text](images/Deployment_AppEngine/image-56.png)

Let's try to input data and see if our code modification works:

![alt text](images/Deployment_AppEngine/image-57.png)

![alt text](images/Deployment_AppEngine/image-58.png)

> Note: you could check the app deployed in this tutorial [here](https://mitcloudworkshop.uc.r.appspot.com/) 

## 11. Explore Google Cloud App Engine Console with information and logs

Return to the Google Cloud Platform Console tab. You should still be in the terminal. Close the terminal by pressing "X" on the top right of the terminal window. 

![alt text](images/Deployment_AppEngine/image-59.png)

Enter the Search box and type **App Engine**

![alt text](images/Deployment_AppEngine/image-60.png)

Click on "App Engine"

You see the dashboard for this service

![alt text](images/Deployment_AppEngine/image-61.png)

In the summary, you can see that our app received several requests and is now idle. If you refresh the tab with app several time, and then refresh this page this is what you will see:

![alt text](images/Deployment_AppEngine/image-62.png)

On the navigation panel to the right, you can navigate to different components of App Engine. For example in **Instances** you can see the VM running your app. In the **Version** you can see and modify versions of your app.

## 12. Modifying app

Open terminal, open editor, and make an edit index.html:

![alt text](images/Deployment_AppEngine/image-63.png)

Change `<h1> <img src="/img/mit.png" alt="MIT Logo"> Hello {{ processed_data1 }}!</h1>` to:
```html
    <h1> <img src="/img/mit.png" alt="MIT Logo"> Thank you {{ processed_data1 }}!</h1>
```
![alt text](images/Deployment_AppEngine/image-64.png)

If you what change `main.py` the way you want.

Now return to terminal and navigate to the app folder

![alt text](images/Deployment_AppEngine/image-66.png)

Enter
```bash
glcoud app deploy
```
![alt text](images/Deployment_AppEngine/image-67.png)

Check the app link to see if it has updated.

![alt text](images/Deployment_AppEngine/image-68.png)


## 13. Shutting application down

Close the terminal on Google Cloud Platform. Go the **Setting** page of **App Engine**.

![alt text](images/Deployment_AppEngine/image-69.png)

Click on Disable Application.

![alt text](images/Deployment_AppEngine/image-70.png)

![alt text](images/Deployment_AppEngine/image-72.png)

Enter your app ID (same as project ID) (it is shown next to the App ID field).

![alt text](images/Deployment_AppEngine/image-73.png)

![alt text](images/Deployment_AppEngine/image-74.png)

You can enable your application at any time.

## 14. Advanced topics:

### 14.1. Updating your application, CI/CD

- First, if you plan to use your app with App Engine, you may wish to have your application in the App Engine structure, like it is [here](https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service), with `app.yaml`. Then the simplest way would be manual pulling the repository to Google Cloud, as we did here, and deploying it. You may write a simple bash(linux terminal processor) script. In our case it will require this commands
```bash
cd cloud_workshop
git pull
cd helloworld
gcloud app deploy
```

- More advanced way is using CI/CD. Continuous Integration / Continuous Deployment is setting when pushes to main of local repository automatically updates running application. It require several step:
    - Use Cloud Repositories. [You can make a Cloud Repositories that mirrors GitHub repository.](https://cloud.google.com/source-repositories/docs/mirroring-a-github-repository). Mirroring mean any changes to GitHub will automatically appear in Google Cloud Source Repository,
    - [Deploy an app from Cloud Source Repositories to App Engine](https://cloud.google.com/source-repositories/docs/deploy-app-engine)
    - [Automate App Engine deployments with Cloud Build](https://cloud.google.com/source-repositories/docs/automate-app-engine-deployments-cloud-build)
    - more info could be seen on the original documentation [here](https://cloud.google.com/source-repositories/docs/quickstarts) and [here](https://cloud.google.com/source-repositories/docs/integration-overview), or other sources.

### 14.2. Storage options

Note that App Engine deployment are stateless. There is no way for them to store information locally, like deployment presented here. You can use third-party APIs as a solutions and use Google Cloud services like Google Cloud Datastore, Cloud SQL, and Cloud Storage that allow you to store data persistently. These services enable you to store and retrieve data between requests, making your application stateful if needed.

- Cloud Storage provides scalable and durable object storage for storing unstructured data such as images, videos, documents, and backups. App Engine applications can utilize Cloud Storage to store and serve static assets, user-uploaded files, application logs, and large datasets. 
- Cloud Datastore: Designed as a highly scalable NoSQL database, Cloud Datastore offers App Engine applications a robust and fully managed solution for storing and querying structured data. 
- Cloud SQL: As a fully managed relational database service, Cloud SQL enables App Engine applications to leverage the power of traditional SQL databases like MySQL, PostgreSQL, and SQL Server. With Cloud SQL, developers can easily create, manage, and scale relational databases without worrying about infrastructure management. 

To use this option you will need to use API and corresponding libraries in your code, so it may require rewriting some parts of your application. More info could be read in [documentation](https://cloud.google.com/appengine/docs/standard/storage-options).
Note that options may incur costs after the free trial period, but some of them also have an amount of free tier allowance.