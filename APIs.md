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











