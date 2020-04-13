### API
###### Application programming interface

- hide implementation of application
- control access to data
- standardized way to access data

Process accessing APIs (client-server communication):
- Client sends a request to the API server
- The API server parses that request
- Assuming the request is formatted correctly, the server queries the database for the information or performs the action in the request
- The server formats the response and sends it back to the client
- The client renders the response according to its implementation

Internet protocol(IPs)
- protocol for sending data from one host to another across internet
  - IP addresses are uniques
- TCP:Transmission control protocol
- FTP: transfer files between server and client
- HTTP: transfer text and hyperlinks

RESTful API(representationla state transfer)
- stateless: API calls are independent
- there must be a client and a server
- uniform interface : a representation for every resource (JSON, HTML, Text and send to client info about how to read it , app/content)
- cachable and layered system: we can cache info in order to make interaction faster, when possible we can use cache and make it stateful in order to work a bit faster

### HTTP and Flask basics

HTTP protocol (Hypertext transfer protocol)
- connectionless : open connection to server port , get response, close connection
- stateless: no link between succession requests
- NOT sessionless: we can store cookies in order to store context between sequential requests
- media independent: we can send any kind of media, client and server need o know how to process the media
- Elements:
  - URL are subsets of URI
  - Requests and responses
  - Status codes

Universal Resource Identifiers (URIs): An example URI is http://www.example.com/tasks/term=homework. 
It has certain components:
- Scheme: specifies the protocol used to access the resource, HTTP or HTTPS. In our example http.
- Host: specifies the host that holds the resources. In our example www.example.com.
- Path: specifies the specific resource being requested. In our example, /tasks.
- Query: an optional component, the query string provides information the resource can use for some purpose such as a search parameter. In our example, /term=homework.

HTTP requests:
- method: GET,POST(create),PUT(modify),PATCH(modify partially),DELET,OPTION
- path: www.google.com/maps
- HTTP version: HTTP/2.0
- Headers (optional)
- Body (Optional)

Status codes and message:
- 1xx : informational
- 2xx : success
  - 200 ok
  - 201 created
- 3xx : redirection
  - 304 not modified
- 4xx : client error
  - 400 bad request
  - 401 not authorized
  - 404 not found
- 5xx : server error
  - 500 internal server error

curl: 
- -X or --request COMMAND
- -d or --data DATA
- -F or --form CONTENT
- -u or --user USER[:PASSWORD]
- -H or --header LINE

### Organize API endpoints

- organize by resource
- use nouns not verbs
  - `https://example.com/tasks`
  - `https://example.com/tasks/5`


### CORS

`No 'Access-Control-Allow-Origin' header is present on the requested resource`

request to website on a different server. 

- same origin policy
- block requests from malicious js
- triggered when: 
  - different domains
  - different subdomains
  - different ports
  - different protocols
- preflight OPTIONS requests
  - do i have the rights to access this resource?
  - if CORS not enabled
    - browser will send no request
- protect users

CORS utilizes headers to specify what the server will allow:
- Access-Control-Allow-Origin
  - What client domains can access its resources. For any domain use *
- Access-Control-Allow-Credentials
  - Only if using cookies for authentication  in which case its value must be true
- Access-Control-Allow-Methods
  - List of HTTP request types allowed
- Access-Control-Allow-Headers
  - List of http request header values the server will allow, particularly useful if you use any custom headers

### Flask-CORS

`pip3 install -U flask-cors`

```
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    #CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) #resource specific usage

    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
    @app.route('/messages')
    @cross_origin() #route specific usage
    def get_messages():
        return jsonify({'message':'Hello, World!'})

```

flask basic APIs (parameter and methods):
```
@app.route('/entrees/<int:entree_id>')
def retrieve_entree(entree_id):
    return 'Entree %d' % entree_id

@app.route('/hello', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        return create_greeting()
    else:
        return send_greeting()
```

pagination:  
```

@app.route('/entrees', methods=['GET','POST'])
def get_entrees ():
  page = request.args.get('page', 1 , int)
  if page>50:
    abort(404)
    
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404
        
```

### Unit Test in flask

```
class AppNameTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)
        self.assertTrue(..)

# Make the tests conveniently executable
if __name__ == "__main__":
unittest.main()
```
Run the test suite, by running `python test_file_name.py` from the command line.  


components that are typically included in good API documentation:

- Introduction
- Getting Started
  - Base URL
  - API Keys /Authentication (if applicable)
- Errors
  - Response codes
  - Messages
  - Error types
- Resource endpoint library
  - Organized by resource
  - Include each endpoint
  - Sample request
  - Arguments including data types
  - Response object including status codes and data types

All good, well-documented projects have a README.md file that should clearly explain the project and how to get started with it to any developers who may want to use or contribute to the project. Depending on your personal style preferences and project type, the structure and exact contents will differ, but the structure below is a good starting place.

- Project Title
  - Description of project and motivation
  - Screenshots (if applicable), with captions
  - Code Style if you are following particular style guides
-Getting Started
  - Prerequisites & Installation, including code samples for how to download all pre-requisites
  - Local Development, including how to set up the local development environment and run the project locally
  - Tests and how to run them
- API Reference. If the API documentation is not very long, it can be included in the README
- Deployment (if applicable)
- Authors
- Acknowledgements



