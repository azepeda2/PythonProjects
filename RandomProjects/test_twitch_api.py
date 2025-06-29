import irc.bot
import irc.strings

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, username, token):
        # Replace with your actual information
        server = 'irc.chat.twitch.tv'
        port = 6667
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)
        self.channel = '#' + channel

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # This method is called when a message is sent in the channel
        print(e.source.nick + ": " + e.arguments[0])

if __name__ == "__main__":
    # Replace with your Twitch username, OAuth token, and the channel you want to join
    username = 'elnenedrow'
    token = '39yf8tnqlcrqhade7q1izjee09uruc'
    channel = 'elnenedrow'

    bot = TwitchBot(channel, username, token)
    bot.start()

#oauth 39yf8tnqlcrqhade7q1izjee09uruc
#type bearer