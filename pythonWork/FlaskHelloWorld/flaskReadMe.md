https://flask.palletsprojects.com/en/1.1.x/quickstart/

## What is flask?
Flask --> micro web framework for python
--> provides simple way to create web apps and APIs using python

usually contains:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

1. `from flask import Flask` --> imports Flask class --> an instance of the flask class will be our Web Server Gateway Interface app
2. `app = Flask(__name__)` --> create an instance of flask
--> if single module --> use __name__
--> if using a package hardcode the name
    --> in yourapplication/app.py you should create it with one of the two versions below:
    `app = Flask('yourapplication')`
    `app = Flask(__name__.split('.')[0])`
3. `@app.route('/')` --> tell flask what URL should trigger our function
4. function!


##run on windows
1. open power shell
2. cd into project
3. add env ` $env:FLASK_APP = "hello.py"`
4. run `.venv\Scripts\activate` to go into venv
5. If you need to run  `pip install Flask`
6. run `flask run`
7. its live now! you can go to the url 




## To Run
unix
```
$ export FLASK_APP=hello.py
$ flask run
```

Windows Command Prompt
```
cd to C:\path\to\app
set FLASK_APP=hello.py
```
Windows PowerShell
```
cd to C:\path\to\app
 $env:FLASK_APP = "hello.py"
```
Alternative
```
export FLASK_APP=hello.py
$ python -m flask run
```

