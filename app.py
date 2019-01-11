from flask import Flask, request, Response #import main Flask class and request object
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
def notify():
    message = request.args.get('message') #if key doesn't exist, returns None
    channelID = request.args.get('channel', default=config['Slack']['TestChannelID'])

    hsb = HomeSlackerBot()
    HomeSlackerBot.PostMessage(hsb, channelID, message)

    return 'HomeSlacker is on it!'

@app.route('/read', methods=['POST'])
def read():
    message = request.args.get('message') #if key doesn't exist, returns None
    channelID = request.args.get('channel', default=config['Slack']['TestChannelID'])

    hsb = HomeSlackerBot()
    HomeSlackerBot.ReadMessage(hsb, channelID, message)

    return 'HomeSlacker is on it!'

@app.route('/slack', methods=['POST'])
def inbound():
    #if request.form.get('token') == SLACK_WEBHOOK_SECRET:
    print(request.form)
    channel = request.form.get('channel_name')
    username = request.form.get('user_name')
    text = request.form.get('text')
    inbound_message = username + " in " + channel + " says: " + text
    print(inbound_message)

    #hsb = HomeSlackerBot()
    #HomeSlackerBot.ReadMessage(hsb, channel, inbound_message)

    return Response(), 200

if __name__ == '__main__':
    app.run() #run app in debug mode on port 5000