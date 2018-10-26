import os
import logging
import time

import configparser

config = configparser.ConfigParser()
config.read('config.json')

from slackclient import SlackClient

logging.basicConfig()

AppID = config['SLACK']['AppID']
ClientID = config['SLACK']['ClientID']
ClientSecret = config['SLACK']['ClientSecret']
SigningSecret = config['SLACK']['SigningSecret']
VerificationToken = config['SLACK']['VerificationToken']
OAUTHAccessToken = config['SLACK']['OAUTHAccessToken']
BotUserOAuthToken = config['SLACK']['BotUserOAuthToken']
ChannelID = config['SLACK']['TestChannelID']

slack_client = SlackClient(BotUserOAuthToken)


#if slack_client.rtm_connect(with_team_state=False):
#    print("Successfully connected, listening for events")
#    while True:
#        print(slack_client.rtm_read())
#         
#        time.sleep(1)
#else:
#    print("Connection Failed")

slack_client.api_call(
    "chat.postMessage",
    channel=ChannelID,
    text="I have a domain name! homeslacker.com :tada:"
)