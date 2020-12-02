
from pycord import DiscordData
from pycord.webhooks import DiscordWebhook

# For now, the config.py file is ignored from the repository. So, you'll need to recreate it.
from config import WEBHOOK_ID, WEBHOOK_TOKEN

azFxBot = DiscordWebhook(WEBHOOK_ID, WEBHOOK_TOKEN)

message = DiscordData()
message.content = "hello from a packaged somewhere"

result = azFxBot.sendData(message)

if result is not None:
  print(result)
