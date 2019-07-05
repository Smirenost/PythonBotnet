from pexpect import pxssh


class Bot:

    # initializing a new client bot
    def __init__(self, host, user, password):
        self.host = host  # IP of bot host
        self.user = user
        self.password = password
        self.session = self.ssh()

    # SSH for client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print("Failed to connect.")
            print(e)

    # Sending command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# send a command to all bots in the botnet
def command_bot(cmd):
    for bot in botnet:
        attack = bot.send_command(cmd)
        print("Output from " + bot.host)
        print(attack)


# List of bots in botnet
botnet = []


def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)
