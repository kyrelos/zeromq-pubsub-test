import json
import logging
import time
import os

import zmq


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("publisher")
    context = zmq.Context()
    publisher_bind_address = os.getenv("ZMQ_BIND_ADDRESS", "tcp://*:3000")

    publisher = context.socket(zmq.PUB)
    publisher.bind(publisher_bind_address)
    while True:
        topic = b"app-metrics"
        messagedata = {
            'hostname': '6398ba165f36', 'environment': 'staging', 'service_name': 'test',
            'event_uuid': '37731817-36fb-4060-b479-0a2beac7c26a'
        }

        logger.info(f"topic={topic}, data={messagedata}")
        data = json.dumps(messagedata).encode("utf-8")
        publisher.send_multipart((topic, data))
        time.sleep(1)


if __name__ == '__main__':
    main()
