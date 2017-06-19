#!/usr/bin/env python

import logging
import pika
import os
import sys
import time

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)


connection_url = '%s://%s:%s@%s:%s%s%s' % (
  os.environ['RABBITMQ_PROTOCOL'],
  os.environ['RABBITMQ_USERNAME'],
  os.environ['RABBITMQ_PASSWORD'],
  os.environ['RABBITMQ_HOSTNAME'],
  os.environ['RABBITMQ_PORT'],
  os.environ['RABBITMQ_VHOST'],
  os.environ.get('RABBITMQ_EXTRA_PARAMS', '')
)

class Receiver(object):
    def __init__(self, url_params):
        self.url_params = url_params
        self._connection = None
        self._channel = None
        self.queue = 'hello'
        self.exchange = ''

    def connect(self):
        LOGGER.info('Connecting to: %s' % self.url_params)
        self._connection = pika.BlockingConnection(pika.connection.URLParameters(self.url_params))

    def receive(self):
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.queue)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    receiver = Receiver(connection_url)

    while True:
       time.sleep(5)
