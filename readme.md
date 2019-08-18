Example of EventStream with Flask


I'm writing this in Python 3 using virtual environments.


Setup Virtual Environment in the root folder of this repo.

cd flask-eventsource-example
python3 -m venv env


Activate the virtual environment
. env/bin/activate

Now that the virtual environment is activated you can download and use the correct flask modules needed for this example.
pip install Flask


You can run the server with the command

FLASK_APP=app.py flask run
