# -*- coding: utf-8 -*-
import sys

from easykiwi import KiwiClient

# pylint: disable=invalid-name

message = ' '.join(sys.argv[1:]) or 'Hello World!'

client = KiwiClient()

with client.connect('amqp://127.0.0.1') as comm:
    result = comm.task_send(message).result(timeout=5.0)
    print(result)
    