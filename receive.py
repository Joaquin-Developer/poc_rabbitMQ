import sys
import json
import pika


from models.person import Person


def print_data(data: str):
    data = json.loads(data)
    person = Person(**data)
    print(" [x] Received data:", vars(person))


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    callback = lambda ch, method, properties, body: print_data(body)

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
