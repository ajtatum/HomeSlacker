import os
import logging
import time
import json
from slackclient import SlackClient

with open('config.json', 'r') as f:
    config = json.load(f)

logging.basicConfig()

AppID = config['Slack']['AppID']
ClientID = config['Slack']['ClientID']
ClientSecret = config['Slack']['ClientSecret']
SigningSecret = config['Slack']['SigningSecret']
VerificationToken = config['Slack']['VerificationToken']
OAUTHAccessToken = config['Slack']['OAUTHAccessToken']
BotUserOAuthToken = config['Slack']['BotUserOAuthToken']
ChannelID = config['Slack']['HomeSlackerChannel']

slack_client = SlackClient(BotUserOAuthToken)


#if slack_client.rtm_connect(with_team_state=False):
#    print("Successfully connected, listening for events")
#    while True:
#        print(slack_client.rtm_read())
#         
#        time.sleep(1)
#else:
#    print("Connection Failed")
class HomeSlackerBot:
    def PostMessage(self, message):
        slack_client.api_call(
            "chat.postMessage",
            channel=ChannelID,
            text=message
        )