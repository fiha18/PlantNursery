# PlantNursery
This is a Nursery Marketplace API by using django rest framework

first step is to install all the requirements necessary to run this project.
I would suggest to work in a virtual environment so that all the changes made in amy library will not affect the systems.

Creating virtual environment

python -m venv <env_name>

To run this project you need to write below code :

pip install -r requirements.txt
The database files in the project need to be migrated
python manage.py makemigrations
python manage.py migrate

Running the server in local host

python manage.py runserver

Some facts about REST Framework  :
REST - REpresentational State Transfer
To perform http methods :
    get()
    put()
    post()
    delete()

I created urls which are connected to apis and apis are populating its data from Serializer.
Serializing the model can be viewed inside django admin as well as django rest API.
I used REST APIs to perform tasks.

I used Many to Many Relationship between Plant Database, Nursery Database and Users Database

Sign Up for User :
http://127.0.0.1:8000/api/RegisterUser/

Sign Up for Nursery :
http://127.0.0.1:8000/api/RegisterNursery/

Add a plant to Nursery by selecting from Plant database :
http://127.0.0.1:8000/api/NurseryPlant/

List All Plants User have :
http://127.0.0.1:8000/api/Users/<user_unique_id>

A user used to view a plant from Nursery : having Nursery Unique id -
http://127.0.0.1:8000/api/Nursery/<nursery_unique_id>

A user can place order :
http://127.0.0.1:8000/api/UserPlant/
