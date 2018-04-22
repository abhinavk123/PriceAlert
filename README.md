# Price Alert
A Web App for price alert on various online stores. The user can set the price alert on any item and set a price limit so whenever price goes below the price limit user will get an email about it.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine

### Prerequisites
1.Python 3.6

2.Flask(Pythond mini Web Framework),Beautifulsoup

3.MongoDB( Database Used)

4.MailGun API(Need an account on mailgun for getting your own API key and domian).

To run it on your local machine.
* First set your API URL and API key in
```
src/models/constants.py
```
* Start the MongoDB
* Run the file to start server.
```
src/run.py
```
* At last go to
```
http://127.0.0.1:4990 or port at which server is running.
```
# Built With

## FrontEnd
* HTML
* CSS
* [Bootsstrap](https://getbootstrap.com/)

## BackEnd
* [Flask](http://flask.pocoo.org/) - Flask is a micro web framework written in Python and based on the Werkzeug toolkit and Jinja2 template engine
* [MongoDB](https://www.mongodb.com/)


