import os, sys, logging, time, json
from pifx import PIFX
from slackclient import SlackClient
from Models.SlackRequest import SlackRequest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("HomeSlackerBot.log"),
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger()

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
        logger.info("Posting message to Slack Channel {} with message {}".format(channelId, message))

        slack_client.api_call(
            "chat.postMessage",
            channel=channelId,
            text=message
        )

    def ReadMessage(self, channelId, message):
        logger.info("Reading message from Slack Channel {}. Message {}".format(channelId, message))

        slack_client.api_call(
            "chat.readMessage",
            channel=channelId,
            text="I can respond."
        )

    def LifxStatus(self, SlackRequest):
        logger.info("Reading message from Slack Channel {}. Message {}".format(SlackRequest.ChannelId, SlackRequest.Text))

        messageArray = SlackRequest.Text.split()
        
        lifxRoom = messageArray[0]
        lifxLight = messageArray[1]
        lifxState = messageArray[2]
        lifxColor = None

        logger.info(messageArray)

        lifxResponse = ""

        try:
            lifxColor = messageArray[3]
            LifxAccess.set_state(selector="group:{},label:{}".format(lifxRoom, lifxLight), power="{}".format(lifxState), color="{}".format(lifxColor))
            lifxResponse = "{} set: Room {}. Light {}. Status {}. Color {}.".format(SlackRequest.UserName, lifxRoom, lifxLight, lifxState, lifxColor)
        except:
            logger.info("No color specified")
        finally:
            LifxAccess.set_state(selector="group:{},label:{}".format(lifxRoom, lifxLight), power="{}".format(lifxState))
            lifxResponse = "{} set: Room {}. Light {}. Status {}.".format(SlackRequest.UserName, lifxRoom, lifxLight, lifxState)

        slack_client.api_call(
            "chat.postMessage",
            channel=SlackRequest.ChannelId,
            text=lifxResponse
        )