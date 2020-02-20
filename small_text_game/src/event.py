class Event:
    name = 'abstract'

    def __init__(self, position, data):
        self.position = position
        self.data = data


class KickEvent(Event):
    name = 'kick'


class MessageEvent(Event):
    name = 'message'

    def __init__(self, position, data):
        super().__init__(position, data)
        if not isinstance(self.data, list):
            self.data = [self.data]
