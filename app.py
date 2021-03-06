from flask import Flask, request, Response, jsonify #import main Flask class and request object
import os, sys, json, logging
from HomeSlackerBot import HomeSlackerBot
from Models.SlackRequest import SlackRequest

app = Flask(__name__) #create the Flask app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("HomeSlackerApp.log"),
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger()

@app.route('/', methods=['GET'])
def home():
    return "<h1>HomeSlacker</h1>"

#@app.route('/messsage', methods=['GET'])
#def message():

@app.route('/notify')
def notify():
    message = request.args.get('message', default="") 
    channelID = request.args.get('channel', default=os.getenv('Slack_TestChannelID'))

    hsb = HomeSlackerBot()
    HomeSlackerBot.PostMessage(hsb, channelID, message)

    return 'HomeSlacker is on it!'

@app.route('/read', methods=['POST'])
def read():
    message = request.args.get('message', default="")
    channelID = request.args.get('channel', default=os.getenv('Slack_TestChannelID'))

    hsb = HomeSlackerBot()
    HomeSlackerBot.PostMessage(hsb, channelID, message)

    return Response(), 200

@app.route('/slack', methods=['POST'])
def slack():
    logger.info(jsonify(request.form.to_dict()))

    sr = SlackRequest()
    sr.ChannelName = request.form.get('channel_name')
    sr.ChannelId = request.form.get('channel_id')
    sr.UserName = request.form.get('user_name')
    sr.UserId = request.form.get('user_id')
    sr.Text = request.form.get('text')

    hsb = HomeSlackerBot()
    HomeSlackerBot.LifxStatus(hsb, sr)

    return Response(), 200

@app.route('/lifxtest', methods=['GET'])
def lifxtest():
    logger.info(jsonify(request.args.to_dict()))

    sr = SlackRequest()
    sr.ChannelName = request.args.get('channel_name')
    sr.ChannelId = request.args.get('channel_id')
    sr.UserName = request.args.get('user_name')
    sr.UserId = request.args.get('user_id')
    sr.Text = request.args.get('text')

    hsb = HomeSlackerBot()
    HomeSlackerBot.LifxStatus(hsb, sr)

    return Response(), 200
    

if __name__ == '__main__':
    app.run(debug=os.getenv('Debug', default=True)) #run app in debug mode on port 5000