#!/usr/bin/env python
import pika, sys, os, time, json


class SlonieEvent:
    def __init__(self, data):
        self.data = data

def get_event_channel(event_class):
    return event_class.__name__.replace("Event", "")

def consume_event(event_class):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel_name = get_event_channel(event_class)
    channel.queue_declare(queue=channel_name)

    def callback(ch, method, properties, body):
        data = json.loads(body)
        event = event_class(data)
        print(f"Consumed {event.__class__.__name__}: {event.data}")

    channel.basic_consume(queue=channel_name, on_message_callback=callback, auto_ack=True)

    print(f"Waiting for {channel_name} events...")
    channel.start_consuming()

if __name__ == '__main__':
    try:
            time.sleep(2)
            consume_event(SlonieEvent)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)