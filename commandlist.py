


  class CommandList(object):
    def __init__(self):
      super(CommandList, self).__init__()
      self.commands =[]



    def next(self):
        pass

    def append(self, command):
        self.commands.apend(command)

    def length(self):
        return len(self.commands)
