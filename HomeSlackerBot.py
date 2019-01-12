import os
import logging
import time
import json
from pifx import PIFX
from slackclient import SlackClient
import SlackRequest

logging.basicConfig()

AppID = os.getenv('Slack_AppID')
ClientID = os.getenv('Slack_ClientID')
ClientSecret = os.getenv('Slack_ClientSecret')
SigningSecret = os.getenv('Slack_SigningSecret')
VerificationToken = os.getenv('Slack_VerificationToken')
OAUTHAccessToken = os.getenv('Slack_OAUTHAccessToken')
BotUserOAuthToken = os.getenv('Slack_BotUserOAuthToken')
ChannelID = os.getenv('Slack_TestChannelID')
LifxAccess = PIFX(os.getenv('Lifx_PersonalAccessToken'))

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

    def LifxStatus(self, SlackRequest):
        logging.info("Reading message from Slack Channel {}. Message {}".format(SlackRequest.ChannelId, SlackRequest.Text))

        messageArray = SlackRequest.Text.split()
        
        lifxRoom = messageArray[0]
        lifxLight = messageArray[1]
        lifxState = messageArray[2]

        LifxAccess.set_state(selector="group:{},label:{}".format(lifxRoom, lifxLight), power="{}".format(lifxState))
        
        lifxResponse = "{} set: Room {}. Light {}. Status {}.".format(SlackRequest.UserName, lifxRoom, lifxLight, lifxState)

        slack_client.api_call(
            "chat.postMessage",
            channel=SlackRequest.ChannelId,
            text=lifxResponse
        )