#!/usr/bin/env python
import pika, time, json
class KotkiEvent:
    def __init__(self, data):
        self.data = data

def get_event_channel(event_class):
    return event_class.__name__.replace("Event", "")

def publish_event(event):
    channel_name = get_event_channel(event.__class__)
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=channel_name)
    
    message = json.dumps(event.__dict__)
    channel.basic_publish(exchange='', routing_key=channel_name, body=message)
    print(f"Published event {event.__class__.__name__} on {channel_name}")
    connection.close()

while True:
    event = KotkiEvent({"message": "Kocham kotki v2"})
    publish_event(event)
    time.sleep(3)