# POC - RabbitMQ in Python


#### Run RabbitMQ service with docker
```bash
chmod 770 scripts/run_rabbitmq.sh
./scripts/run_rabbitmq.sh
```

#### Run Producer & Consumer:
```bash
./scripts/receive.sh   # First, run this
./scripts/send.sh
```

#### RabbitMQ Overview:
[http://localhost:15672/#/](http://localhost:15672/#/)


<hr>

#### docs:

- [Introduction to Pika](https://pika.readthedocs.io/en/stable/intro.html)
- [RabbitMQ with Docker](https://www.rabbitmq.com/download.html)
- [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html)
