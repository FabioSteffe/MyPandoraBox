## Flask

basic hello world with flask
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello world'
```

run flask app (default method)
```
export FLASK_ENV=development # enables live reload
export FLASK_DEBUG=true # enables live reload
FLASK_APP=app.py flask run
FLASK_APP=app.py FLASK_DEBUG=true flask run # enable debug mode
```

run flask app (with main):
- define main in app.py
```
if __name__ == '__main__':
  app.run()
```
- run using python3 app.py








