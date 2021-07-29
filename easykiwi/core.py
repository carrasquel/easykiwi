# -*- coding: utf-8 -*-

import logging
import time
import sys

import kiwipy

from ._singleton import Singleton


class Kiwi(Singleton):

    def __init__(self):

        self._rpcs = list()
        self._tasks = list()
        self._broadcasts = list()

        self._remote = '127.0.0.1'

    def add_rpc(self, name=None):

        def decorator(f):

            if not name:

                name = f.__name__

            rpc = (f, name,)
            self._rpcs.append(rpc)

            return f
        
        return decorator

    def add_task(self):

        def decorator(f):

            self._tasks.append(f)

            return f
        
        return decorator

    def add_broadcast(self):

        def decorator(f):

            self._broadcasts.append(f)

            return f
        
        return decorator

    def _add_rpcs(self):

        for f, name in self._rpcs:

            self.comm.add_rpc_subscriber(f, name)

    def _add_tasks(self):

        for task in self._tasks:

            self.comm.add_task_subscriber(task)

    def _add_broadcasts(self):

        for broadcast in self._broadcasts:

            self.comm.add_broadcast_subscriber(broadcast)

    def run(self):

        self.comm = kiwipy.connect("amqp://{}".format(self.remote))

        self._add_rpcs()
        self._add_tasks()
        self._add_broadcasts()

        try:      
            while True:
                time.sleep(0.25)

        except (KeyboardInterrupt, SystemExit):
            logging.warning("Manual Shutting down!!!")
            self.comm.close()
            time.sleep(0.25)
            
            sys.exit()
        