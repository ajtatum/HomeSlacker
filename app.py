from flask import Flask, request #import main Flask class and request object
import json
from HomeSlackerBot import HomeSlackerBot

app = Flask(__name__) #create the Flask app

with open('config.json', 'r') as f:
    config = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return "<h1>HomeSlacker</h1>"

#@app.route('/messsage', methods=['GET'])
#def message():

@app.route('/notify')
def querystring():
    message = request.args.get('message') #if key doesn't exist, returns None
    channelID = request.args.get('channel', default=config['Slack']['TestChannelID'])

    hsb = HomeSlackerBot()
    HomeSlackerBot.PostMessage(hsb, channelID, message)

    return 'HomeSlacker is on it!'

if __name__ == '__main__':
    app.run() #run app in debug mode on port 5000