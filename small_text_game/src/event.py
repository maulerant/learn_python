class Event:
    name = 'abstract'

    def __init__(self, position, data):
        self.position = position
        self.data = data


class KickEvent(Event):
    name = 'kick'
