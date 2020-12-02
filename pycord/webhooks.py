
from pycord import DiscordData
from requests import post as POST

class DiscordWebhook:
  def __init__(self, id, token):
    self.id = id
    self.token = token

  def sendData(self, discordData):
    result = None

    if isinstance(discordData, DiscordData) and discordData.usable():
      postUrl = self.url()

      queryString = "?"

      for k, v in discordData.parameters().items():
        queryString += f"{k}={v},"

      if 1 < len(queryString):
        postUrl += queryString[:-1] # Remove the last comma character.

      # Send off the request.
      result = POST(postUrl, data=discordData.formData())

    return result

  def url(self):
    return f"https://discordapp.com/api/webhooks/{self.id}/{self.token}"
