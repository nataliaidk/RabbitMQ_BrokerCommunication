
class KotkiEvent:
    def out():
        print("wywolano classe event")

class PieskiEvent:
    pass

class KaczkiEvent:
    pass

class SlonieEvent:
    pass
def get_event_channel(event_class):
    return event_class.__name__.replace("Event", "")

# Sprawdzamy nazwę klasy i generujemy nazwę kanału
print(get_event_channel(KotkiEvent))  # "EventType1"
print(get_event_channel(PieskiEvent))  # "EventType2"
