class Notifier:
    def send(self, message):
        raise NotImplementedError
    
class EmailNotifier(Notifier):
    def send(self, message):
        print(f'Email: {message}')

class SMSNotifier(Notifier):
    def send(self, message):
        print(f'SMS: {message}')

class PushNotifier(Notifier):
    def send(self, message):
        print(f'Push: {message}')

def notify_all(notifiers, message):
    for n in notifiers:
        n.send(message)

notifiers = [EmailNotifier(), SMSNotifier(), PushNotifier()]
notify_all(notifiers, 'Привет')

    
