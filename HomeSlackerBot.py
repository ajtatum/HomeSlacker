import os
import logging
import time
import json
from slackclient import SlackClient

logging.basicConfig()

AppID = os.getenv('Slack_AppID')
ClientID = os.getenv('Slack_ClientID')
ClientSecret = os.getenv('Slack_ClientSecret')
SigningSecret = os.getenv('Slack_SigningSecret')
VerificationToken = os.getenv('Slack_VerificationToken')
OAUTHAccessToken = os.getenv('Slack_OAUTHAccessToken')
BotUserOAuthToken = os.getenv('Slack_BotUserOAuthToken')
ChannelID = os.getenv('Slack_TestChannelID')

slack_client = SlackClient(BotUserOAuthToken)

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
        lifxResponse = "Room {}. Light {}. Status {}.".format(messageArray[0], messageArray[1], messageArray[2])

        slack_client.api_call(
            "chat.postMessage",
            channel=channelId,
            text=lifxResponse
        )