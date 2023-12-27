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
