# -*- coding: utf-8 -*-

from easykiwi import KiwiClient

# pylint: disable=invalid-name

client = KiwiClient()

with client.connect('amqp://127.0.0.1') as comm:
    # Send an RPC message with identifier 'fib'
    print(' [x] Requesting fib(30)')
    response = comm.rpc_send('fib', 30).result()
    print(f' [.] Got {response!r}')

    # Send an RPC message with identifier 'fac'
    print(' [x] Requesting fac(3)')
    response = comm.rpc_send('fac', 3).result()
    print(f' [.] Got {response!r}')
    