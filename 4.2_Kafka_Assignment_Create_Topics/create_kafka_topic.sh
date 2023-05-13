#!/bin/bash

docker compose exec broker kafka-topics --create --topic event1 --bootstrap-server broker:9092
docker compose exec broker kafka-topics --create --topic event2 --bootstrap-server broker:9092
docker compose exec broker kafka-topics --create --topic event4 --bootstrap-server broker:9092
docker compose exec broker kafka-topics --create --topic event3 --bootstrap-server broker:9092

docker compose exec broker kafka-topics --list --bootstrap-server broker:9092

docker compose exec broker kafka-topics --describe --bootstrap-server broker:9092

