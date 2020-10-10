# Resale Value Prediction and Management

Resale Value Prediction and Management was [Animesh Gupta](https://github.com/strange-hawk/) and my Database management project. 
We both were bored with a simple management system that required basic database transactions, so we decided to apply a bit of machine learning and web scraping to our project. 
This project allows users to buy and sell their used properties and cars, and also predict the prices for their items. We scraped prices of vehicles and real estates from OLX, 
we localised our search to vadodara only, had about 1500 rows of data for each, trained 2 models and deployed them using django. I am not linking the API here due to security issues. 


# Features!

  - Uploading properties and vehicles for sale
  - Buying properties and vehicles
  - Finding resale values of vehicles and properties based on a few parameters


# Tech

 uses the following:

* Django - as the backend for the services
* pandas - for working with the csv
* bootstrap - for the frontend
* TensorFlow - For the model
* Scikit-learn - For the model
* joblib - For saving and loading the model


# Installation
ResaleValuePrediction requires django 3.0 to run.

For linux users
```sh
$ git clone https://github.com/TanmayAmbadkar/ResaleValuePrediction.git
$ cd gccc-dashboard
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

For windows users with conda
```sh
$ git clone https://github.com/TanmayAmbadkar/ResaleValuePrediction.git
$ cd gccc-dashboard
$ conda create -n myenv python=3.8
$ conda activate myenv
$ pip install -r requirements.txt
```

To test the app

```sh
$ python manage.py makemigrations && python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Open a browser tab and write http://localhost:8000/ to see the website.

If you want to deploy the app, you can use the following tutorial to deploy it on an AWS EC2 machine using apache - [tutorial](https://medium.com/saarthi-ai/ec2apachedjango-838e3f6014ab)
