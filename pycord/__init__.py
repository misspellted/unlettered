
def tfs(value):
  return str.lower(str(value))

class DiscordData:
  CHARACTER_MAXIMUM = 2000
  EMBEDS_MAXIMUM = 10

  def __init__(self, wait=False):
    self.wait = wait
    self.userName = None
    self.passWord = None
    self.content = None
    self.avatarUrl = None
    self.textToSpeech = False
    self.fileContents = None
    self.embeds = None
    self.jsonPayload = None
    self.allowedMentions = None

  def message(self, text):
    if text and isinstance(text, str):
      self.content = text

      if DiscordData.CHARACTER_MAXIMUM < len(self.content):
        self.content = self.content[:DiscordData.CHARACTER_MAXIMUM]

      # And we can only send one of content, file, or embeds, so...
      self.fileContents = None
      self.embeds = None

  def contents(self, fileContents):
    if fileContents:
      self.fileContents = fileContents

      # And we can only send one of content, file, or embeds, so...
      self.content = None
      self.embeds = None

  def embed(self, embedded):
    if embedded:
      if self.embeds is None:
        self.embeds = list()

      # But only permit the maximum embeds allowed.
      if len(self.embeds) < DiscordData.EMBEDS_MAXIMUM:
        self.embeds.append(embedded)

      # And we can only send one of content, file, or embeds, so...
      self.content = None
      self.embeds = None

  def usable(self):
    # Indicate whether or not the data to send is something worthwhile sending...
    worthwhile = False

    if not worthwhile:
      worthwhile = self.content is not None

    if not worthwhile:
      worthwhile = self.fileContents is not None

    if not worthwhile:
      worthwhile = self.embeds is not None

    return worthwhile

  def parameters(self):
    # What good is it to grab parameters if this is something that's not usable?
    if not self.usable():
      return None

    params = dict()

    params["wait"] = tfs(self.wait)

    return params

  def formData(self):
    # Why jsonify something that's not usable?
    if not self.usable():
      return None

    this = dict()

    # For now, only support sending a message.. but we can do so much more!
    # https://discord.com/developers/docs/resources/webhook#execute-webhook
    if self.content is not None:
      this["content"] = self.content

    return this
