import json
from dataclasses import asdict
import pika


from models.person import Person


def get_data_to_send() -> str:
    person = Person("James", 30, "Norway")
    return json.dumps(asdict(person))


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange="", routing_key="hello", body=get_data_to_send())
    print(" [x] Sent data to queue 'hello'")


if __name__ == "__main__":
    main()
