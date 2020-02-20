from small_text_game.src.event import Event


class EventManager:
    _instance = None
    subscribers = None

    def __init__(self):
        if not EventManager._instance:
            self.subscribers = {}

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = EventManager()
        return cls._instance

    def unbind(self, event_name, subscriber, callback):
        subscriber_info = {'object': subscriber, 'callback': callback}
        if subscriber_info in self.subscribers[event_name]:
            self.subscribers[event_name].remove(subscriber_info)

    def bind(self, event_name, subscriber, callback):
        if event_name not in self.subscribers.keys():
            self.subscribers[event_name] = []
        subscriber_info = {'object': subscriber, 'callback': callback}
        if subscriber_info not in self.subscribers[event_name]:
            self.subscribers[event_name].append(subscriber_info)

    def dispatch(self, event):
        if self.is_event(event) and event.name in self.subscribers.keys():
            for subscriber_info in self.subscribers[event.name]:
                getattr(subscriber_info['object'], subscriber_info['callback'])(event)

    def is_event(self, event):
        return Event in event.__class__.__bases__
