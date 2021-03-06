
class ClassName(object):
    """docstring for """
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name


class TextChannel(object):
    """Channel class, reads commands from file"""
    def __init__(self, name="TextChannel"):
        super(TextChannel, self).__init__()
        self.name = name 
        self.messages = []
        with open("messages.txt", "r") as f:
            for line in f:
                self.messages.append(line)


    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0
