import os
import logging
import time
import json
from slackclient import SlackClient

logging.basicConfig()

AppID = os.environ['Slack_AppID']
ClientID = os.environ['Slack_ClientID']
ClientSecret = os.environ['Slack_ClientSecret']
SigningSecret = os.environ['Slack_SigningSecret']
VerificationToken = os.environ['Slack_VerificationToken']
OAUTHAccessToken = os.environ['Slack_OAUTHAccessToken']
BotUserOAuthToken = os.environ['Slack_BotUserOAuthToken']
ChannelID = os.environ['Slack_TestChannelID']

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
    def PostMessage(self, channelId, message):
        logging.info("Posting message to Slack Channel {} with message {}".format(channelId, message))

        slack_client.api_call(
            "chat.postMessage",
            channel=channelId,
            text=message
        )

    def ReadMessage(self, channelId, message):
        logging.info("Reading message from Slack Channel {}. Message {}".format(channelId, message))

        slack_client.api_call(
            "chat.readMessage",
            channel=channelId,
            text="I can respond."
        )

    def LifxStatus(self, channelId, message):
        logging.info("Reading message from Slack Channel {}. Message {}".format(channelId, message))

        messageArray = message.split()
        lifxResponse = "Room {}. Light{}. Status {}.".format(messageArray[0], messageArray[1], messageArray[2])

        slack_client.api_call(
            "chat.postMessage",
            channel=channelId,
            text=lifxResponse
        )