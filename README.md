
This app consists of login and password to see the API-view of user details and activity periods. 
It can be accessed by from https://assignment-ftl.herokuapp.com/

username : Assignment

Password : assign@123

The API end point is directly accessed by " https://assignment-ftl.herokuapp.com/userdetailview-api/ "

Purpose of Assignement: 

	-- To design the web API using python and Django consisting details of user and respective activity periods
    
	-- Creating the API endpoint of production ready and hosted somewhere like heroku etc.

Procedure steps : 

Firstly, need to install and run python in command prompt(cmd) of local instance.

	-- Here, the assignment is build in windows below are steps to install python in windows
    
		1. Visit https://www.python.org/downloads/
        
		2. Choose the version and click on download
        
		3. After download run the application and install the python
        
		4. To verify whether the python is installed correctly open the cmd window and execute command /* python --version */

Then install Django and check the version in cmd by executing the below commands

    /* pip install django */	- to install django

    /* django-admin --version */	- to check the version

For this project we use IDE as the visualstudio code and this is downloaded by below link
https://code.visualstudio.com/download - run and install for windows

By migrating to the location where the project need to be placed follow below commands

	/* django-admin startproject project_name */	# creates the new projects in the folder you are present

	migrate to the project folder and continue

	/* python manage.py runserver */ 	 	# for checking whether project is executing run
	copy the local host url and run in the webbrowser to check for errors 
	
	/* django-admin startapp app_name */		# creates the new app, to execute code.

After opening the project folder in the Visualstudio code you can see different python file under project and application created. 

settings.py(project_name)

    INSTALLED_APPS = ['app_name']	# add this to access the app in the project

urls.py(project_name)

    urlpatterns = [path('',include(app_name.urls))]		# include the app_name.urls to have extension of urls created in the app

CREATING THE MODELS AND MIGRATING TO DATABASE

Models.py(app_name)
The tables are created for database to store the data and retrieve when it is necessary 

for this project two models are created namely User and ActivityPeriod 

    User Model
	    - id (characterfield, primarykey, maximumlength=10)	# Employee id of the user
	    - real_name (characterfield, maximumlength=50)		# Name of the user
	    - tz (characterfield, default=UTC)			# timezone of the user

    User ActivityPeriod
	    - user (foreignkey,on_delete=models.CASCADE)# used to access User Model
	    - start_time(characterfield, maxlength=50) 	# start time of the activity period of user
	    - end_time(characterfield, maxlength=50) 	# end time of the activity period of user

admin.py(app_name) - registers the models

	- admin.site.register(User)
	- admin.site.register(ActivityPeriod)

To migrate these to database we need to run below command in the cmd

	/* python manage.py makemigrations */		# look for any changes in the database and displays with some id like 0001
	/* python manage.py sqlmigrate app_name id */	# commits the changes to database
	/* python manage.py migration */		# saves the changes to the database and ready to use

If we want to update, delete the database values can be acheived by djangoadmin webpage for that we need to create superuser by floowing command

	/* python manage.py createsuperuser*/		# username, gmail and password to be given

CUSTOM MANAGEMENT COMMAND TO POPULATE DATABASE

We can populate database by command prompt using conding functionality

1. Create new app in the same project - /* django-admin startapp app_name_db */

2. Create folder managements and subfolder commands in app

3. in subfolder need to create python files for scripting our functionalities to execute custom management commands

In this assignment created two python files namely - add_user.py and add_activityperiods.py
These can be executed by floowing commands 

	/* python manage.py add_user "id" "real_name" "tz" */				    # creates the user to database 
	/* python manage.py add_activityperiods "id" "start_time" "end_time" */	# assigns the activity periods for respective user

DESIGN OF API

settings.py(project_name)

    INSTALLED_APPS = ['rest_framework']	# add this to access the rest_framwork functionality

Create the new folder in app_name namely serializer.py, to execute the rest_framework. 

1. Django's serialization framework provides a mechanism for translating Django models into other formats

2. For example: In this assignment, models are converted into json format

serializers.py(app_name)
Created two serializer for the two models namely ActivitySerializer and UserSerializer

    ActivitySerializer - It holds the fields and data of model ActivityPeriod
    UserSerializer	   - It holds the fields and data of model User by inheriting the ActivitySerializer 

urls.py(app_name)

create the url to access the API endpoint 

The API endpoint of this assignment is - " https://assignment-ftl.herokuapp.com/userdetailview-api/ "

views.py(app_name)

1. The views are information brokers of application
2. The view decides what data gets delivered to the url. 

For this assignment, 

    @api_view(["GET"])
    def userdetailview(request):
	    #TODO
	    #Retrieves data from serializers and returns as response(data)

Tests(app_name)

The unit test code snippets are implemented by creating the folder call tests.

	/* python manage.py test */ 	# The test codes are executed 


DEPLOY TO MAKE PRODUCTION READY USING HEROKU CLI

Firstly, open the heroku application and create a new app(heroku_app_name)

In settings of that add the python as Buildpack

Add some more files in the project folder - mentioned as below

    runtime.txt 		# version of python
    requirements.txt	# The required packages for the app to deploy is listed and used to migrate the code
    Procfile - web: gunicorn project_name.wsgi --log-file - 	# copy the same with respective project_name

Open the cmd prompt and follow the below mentioned steps

	/* heroku login */				# which automates to browser to login to your account
	/* heroku git:remote -a heroku_app_name */	# The heroku is directed to app where the code need to deplp
	/* git init */					# Initilises the git in project folder
	/* git remote -v */				# to check whether user in exact repository
	/* git status */				# displays any changes made to the code
	/* git add . */					# if any changes are made then it adds all the changes to git
	/* git commit -m "some comment" */		# it commits all the changes to repository
	/* git push heroku master */			# Finally the code would be deployed to app and can able to access the application.

MIGRATE DATABASE
settings.py(project_name)

Database connection settings import all the required fields from heroku app- resources- postgres

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '5432',
        }
    }

After changing first run all the above commands and then additionally continue with below commands

	/* heroku run python manage.py makemigrations */
	/* heroku run python manage.py migrate*/
	/* heroku run python manage.py createsuperuser */   #for accessing the database at server side


		
	
