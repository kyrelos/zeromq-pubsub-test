import logging
import os

import zmq


def main():
    context = zmq.Context()
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("subscriber")
    publisher_addess = os.getenv("ZMQ_PUB_ADDR", "tcp://localhost:5400")
    socket = context.socket(zmq.SUB)
    socket.connect(publisher_addess)
    topicfilter = b"app-metrics"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    while True:
        topic, data = socket.recv_multipart()
        logger.info(f"{data}")


if __name__ == '__main__':
    main()
