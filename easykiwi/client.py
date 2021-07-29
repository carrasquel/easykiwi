# -*- coding: utf-8 -*-

import kiwipy


class KiwiClient:

    def __init__(self, remote="127.0.0.1"):

        self.remote = remote

    def connect(self, remote="127.0.0.1"):

        self.remote = remote

        self.comm = kiwipy.connect('amqp://{}'.format(self.remote))

        return self.comm

    def broadcast_send(self, *args, **kwargs):

        return self.comm.broadcast_send(*args, **kwargs)

    def rpc_send(self, *args, **kwargs):

        return self.comm.rpc_send(*args, **kwargs)

    def task_send(self, *args, **kwargs):

        return self.comm.task_send(*args, **kwargs)    
