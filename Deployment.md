# Deployment to Cloud

![gcp logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/330px-Google_Cloud_logo.svg.png)


We will use [Google Cloud platform (GCP)](https://cloud.google.com/?hl=en) for this practical part.

# Deployment to VM as persistent service

## 1. Ensuring your application is ready 

Open terminal. Clone your repository to the empty folder. Enter the directory with your app. Install flask, and other needed packages.
```bash
git clone <your_repo_name>
cd <your_repo_name>
pip install -r requirements.txt  # or just use pip install flask, if you are using only flask
flask run
```

![alt text](images/Deployment/image_01.png)

If flask run properly you will be able to reach your app at this [address](http://127.0.0.1:5000/).

![alt text](images/Deployment/image_02.png)


## 2. Creating account and login to GCP

Go to the [Google Cloud Platform](https://cloud.google.com/) site.

![alt text](images/Deployment/image.png)

Press "Get started for free" and follow the registration process.

![alt text](images/Deployment/image-1.png)

You will need to enter your personal data, and credit card for validation, no money will be charged.

**NOTE:** on payments and costs: GCP it requires you credit card to register. It offers [3 month free use, and 300$ credits](https://cloud.google.com/free/docs/free-cloud-features). After free use ends you will not be charged, unless you willingly switch to paid account. So before 3 month trial ends you have nothing to worry about. 

After that, if you switch to paid there is some thing you need to know: there is a so called [free tier](https://cloud.google.com/free/docs/free-cloud-features), thar offer a considerable amount of services for free. For example it offer running one "e2-micro" VM instance (the same we will be running now) with 30Gb disk, external IP, and 1Gb traffic for free. Having pet project hosted on a low performance VM costs little, but you have to be careful. By mistake on unknowing you may switch on some costly service you can get charged, so what you should do is set the budget limit in the cloud for example for $1 - %5, so if you reach this amount you will receive e-mail with notification. Setting a budget limit will be shown in the guide video. 

## 3. Navigating to Compute section of GCP console

After you log in you will get into the console. This is a web interface that allow us work with Cloud. 

![alt text](images/Deployment/image-4.png)

You see an info panel with some metrics. On the left by pressing ≡ on the left right corner you can open the Navigational panel.

![alt text](images/Deployment/image-2.png)

As you can see there is a lot of services. Let's now go the Compute Engine->VM where you can configure and start your Virtual Machine.

![alt text](images/Deployment/image-3.png)

You may need to enable Compute Engine API 

![alt text](images/Deployment/image-5.png)


## 4. Configuring VM we want to start

![alt text](images/Deployment/image-8.png)

In this section press "Create instance" and you will open to the new VM configuration page.

![alt text](images/Deployment/image-7.png)

Configuration. Carefully check configuration, if you miss anything here you will probably face issues later:

1. Enter instance name

![alt text](images/Deployment/image-22.png)

2. For machine type select: **e2-micro**

![alt text](images/Deployment/image-6.png)

3. Click on *Change* button in the **Boot disk** section

![alt text](images/Deployment/image-20.png)

In the operation system select **"Ubuntu"**
In the version select **Ubuntu 24.04 LTS x86/64**
> Note: You may choose other versions, like 22.04 or 23.04, they differs by the version of installed software, like python version 

Leave other fields to default and click **Select**

![alt text](images/Deployment/image-26.png)

4. Enable check-boxes "*Allow HTTP traffic*" and "*Allow HTTPS traffic*" in the **Firewall** section

![alt text](images/Deployment/image-9.png)

5. Leave other options to default and click "**CREATE**"

![alt text](images/Deployment/image-27.png)

## 5. Starting VM

![alt text](images/Deployment/image-24.png)

You should see VM appears in the list, and starting. After it starts, you will see a green ✅ mark in Status.

![alt text](images/Deployment/image-11.png)

Click on the name to enter the details of VM

![alt text](images/Deployment/image-12.png)

## 6. Login into VM with SSH

Click on SSH button here. This will connect to this VM using SSH protocol.

![alt text](images/Deployment/image-13.png)

You may be asked to authorize SSH

![alt text](images/Deployment/image-28.png)

Note - in some cases it may require login in to your Google account in pop-up window

After authorizing you shall see this VM terminal:

![alt text](images/Deployment/image-29.png)

## 7. Updating system and installing needed programs

Now you will work inside your VM using linux terminal
Check you have git and python
```bash
git
python3 --version
```
You should see that we have Python 3.12 installed. Now we need to install pip, python package installer
```bash
sudo apt update
sudo apt install python3-pip
```

![alt text](images/Deployment/image-30.png)

It will ask you to confirm, so enter **Y**

Next step is installing **venv** - a virtual environment for python, that will allow us to run virtual environment for our application. 
```bash
sudo apt install python3.12-venv
```

Also we will need to install **gunicorn**, a production server for running our application on VM.
```bash
sudo apt install gunicorn
```

Now you have all you need
![alt text](images/Deployment/image-44.png)


## 8. Cloning repository with git clone

Now clone your repository from github

```bash
git clone <your_repo_name>  #Replace <your_repo_name> with repository you wish to clone
```

In your repository enter your application directory
```bash
cd <your_repo_name>/<app_folder> #Replace with application directory
```
![alt text](images/Deployment/image-33.png)

Now let's create a virtual environment with python, and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```
![alt text](images/Deployment/image-35.png)

## 9. Installing packages

Now we are inside the virtual environment and will install packages
Now let's install required packages
```bash
pip install -r requirements.txt
```
![alt text](images/Deployment/image-36.png)


## 10. Starting flask server with gunicorn for the first time and checking it works

We will use gunicorn for running flask application. 
It is a production server that provides better performance and scalability and is a common practice.

Lets run our application

```bash
sudo venv/bin/python -m gunicorn -b 0.0.0.0:80 app:app
```
![alt text](images/Deployment/image-43.png)

Now lets return to the Google Cloud console

![alt text](images/Deployment/image-38.png)

Click on "VM instances" on the left column, to return to VM list

![alt text](images/Deployment/image-39.png)

You can see column "External IP", and once you move your mouse there, there will be "Copy" icon. Click on it to copy this address.


Now open the new window and paste this address to the address bar

![alt text](images/Deployment/image-40.png)

Note: be sure the address is HTTP, not HTTPS. We are only providing HTTP, so the address must be "http://34.136.174.45" (replace with your IP address)

Now you can see the application is working:

![alt text](images/Deployment/image-41.png)

Let's send POST request with name:

![alt text](images/Deployment/image-42.png)

Excellent!

## 11. Configuring gunicorn as a service 

Press Ctrl-C to terminate gunicorn, if it is running.
Exit venv shell
```bash
deactivate
```

We will use systemd service to make our application run permanently.

First you need to get the absolute path of your app
```bash
pwd
```
![alt text](images/Deployment/image-48.png)

You will need to create this file, using nano editor:
```bash
nano demo.service
```
![alt text](images/Deployment/image-45.png)

Copy this text, and make necessary edits.
```
[Unit]
Description=My Flask Application
After=network.target

[Service]
# Replace with your username
User=sirius7_ai

# Replace with your app directory absolute path
WorkingDirectory=/home/sirius7_ai/cloud_workshop/helloworld
# 
ExecStart=sudo venv/bin/python3 -m gunicorn -b 0.0.0.0:80 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```
![alt text](images/Deployment/image-51.png)

Press Ctrl-X to exit. Press **Y** to save the file, and **Enter** to confirm

![alt text](images/Deployment/image-52.png)

Add your user to SUDOER list (grant him admin rights for this task).
Run
```bash
sudo visudo
```
Scroll down and below `root    ALL=(ALL:ALL) ALL` add this line `sirius7_ai ALL=(ALL) NOPASSWD: /home/sirius7_ai/cloud_workshop/helloworld/venv/bin/python3`, replacing username and directory name
```
# User privilege specification
root    ALL=(ALL:ALL) ALL
sirius7_ai ALL=(ALL) NOPASSWD: /home/sirius7_ai/cloud_workshop/helloworld/venv/bin/python3
```

![alt text](images/Deployment/image-50.png)

Press Ctrl-X to exit and **Y** to confirm save. 

Now copy `demo.service` file to system folder
```bash
sudo cp demo.service /etc/systemd/system/
```
Reload systemd service, so it sees your new unit
```bash
sudo systemctl daemon-reload
```
Enable your demo.service:
```bash
sudo systemctl enable demo.service
```
Now it will automatically start with boot.
And start it now:
```bash 
sudo systemctl start demo.service
```
You can check the status of your demo.service:
```bash
sudo systemctl status demo.service
```

Now if you exit SSH terminal, your gunicorn server with your app will work. If you stop and start again your VM it will run, but the IP address will change.

# Advanced topics

## 1. Static IP

VM that you have in Google Cloud does have Ephemeral External IP. It means that if you restart it the address wil change. Google Cloud may also restart your VM due to maintenance, that will aslo lead to change of IP address. 
However you can reserve a Static IP address for your VM. Follow this steps to assing a static IP to your VM:
1. Navigate to the VM Instance Settings: Go to the Google Cloud Console and navigate to the Compute Engine > VM instances page.
2. Select your VM: Click on the name of the VM for which you want to change the IP address.
3. Stop the VM: If your VM is running, you need to stop it before you can edit its settings. Click the "Stop" button at the top of the page to stop the VM.
4. Edit the VM configuration: After the VM is stopped, click the "Edit" button at the top of the page to edit its configuration.
5. Change the external IP to static: In the "Network Interfaces" section, locate the external IP address assignment. Change it from "Ephemeral" to "Static". If you don't have a static IP reserved yet, you can reserve one by selecting "Create IP Address" and then choosing "Static" as the type.
6. Save your changes: Once you've made the necessary changes, click the "Save" button to apply them.
7. Start the VM: After saving the changes, you can start the VM again by clicking the "Start" button.

## 2. Hostname

Google Cloud does not provide hostname. If you have hostname you can use a Cloud DNS service to configure DNS record pointing your hostname to VM static IP address. More info is in the suggested study part of this workshop.

## 3. Continuous Deployment

For a presented way of deployment there are several Continuous Integration/ Continuous Deployment options. They are a bit of the scope, but here is some of the options:
1. Manual. This approach doesn't require any additional tools or applications beyond Git for version control and the necessary scripts or commands to pull changes from the repository and restart the application.Just git pull and restart the service:
```bash
git pull
sudo systemctl restart demo.service
```
This could be made as a script for usability

2. Git Webhooks:
You'll need a webhook receiver application or service running on your VM to receive payloads from the Git repository whenever changes are made. This could be a simple web server or an application designed to handle webhook events.

3. CI/CD Pipeline with Jenkins, GitLab CI/CD, or GitHub Actions::
You'll need a webhook receiver application or service running on your VM to receive payloads from the Git repository whenever changes are made. This could be a simple web server or an application designed to handle webhook events.

## 4. Containers

Containers are like virtual machines, but lighter and more flexible. They package everything an app needs to run - code, runtime, libraries - into a single unit that can run anywhere. While they're a bit trickier to learn than traditional VMs. You need to know what is Docker and how it works to use them, and they offer some benefits.

Google Cloud has some tools to make container deployment easier:

- **Cloud Run**: Lets you deploy containers in a easy way.
- **Cloud Build**: Handles the creating of containers and CI/CD pipelines.
