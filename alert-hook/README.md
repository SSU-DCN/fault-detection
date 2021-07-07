## Alert-hook
Send AlertManager's events to Tacker.
## How to run
* First change the authentication information in keystone.py. You can create new openstack's user for that
* Change the port in app.py if needed ( The first two steps can be improved by adding to local env)
* Install Python’s virtual environment (https://docs.python-guide.org/dev/virtualenvs/) 
* Run following commands:
```
$ virtualenv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 app.py
```
