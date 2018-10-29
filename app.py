from flask import Flask, request #import main Flask class and request object
import json
from flask_heroku import Heroku
from HomeSlackerBot import HomeSlackerBot

app = Flask(__name__) #create the Flask app
heroku = Heroku(app)

with open('config.json', 'r') as f:
    config = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

#@app.route('/messsage', methods=['GET'])
#def message():

@app.route('/notify')
def query_example():
    message = request.args.get('message') #if key doesn't exist, returns None

    hsb = HomeSlackerBot()
    HomeSlackerBot.PostMessage(hsb, message)

    return '''<h1>The message value is: {}</h1>'''.format(message)

if __name__ == '__main__':
    app.run(port=80) #run app in debug mode on port 5000