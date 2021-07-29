# -*- coding: utf-8 -*-

import logging
import time
import sys

import kiwipy

from ._singleton import Singleton


class Kiwi(Singleton):

    def __init__(self):

        self.remote = '127.0.0.1'
        
        self._rpcs = list()
        self._tasks = list()
        self._broadcasts = list()

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

    def add_broadcast(self, filters=[]):

        def decorator(f):

            broadcast = (f, filters)
            self._broadcasts.append(broadcast)

            return f
        
        return decorator

    def _add_rpcs(self):

        for f, name in self._rpcs:

            self.comm.add_rpc_subscriber(f, name)

    def _add_tasks(self):

        for task in self._tasks:

            self.comm.add_task_subscriber(task)

    def _add_broadcasts(self):

        for f, filters in self._broadcasts:

            if filters:
                filtered = kiwipy.BroadcastFilter(f)
                
                for filter in filters:
                    
                    filtered.add_subject_filter(filter)
                
                self.comm.add_broadcast_subscriber(filtered)
            else:
                self.comm.add_broadcast_subscriber(f)

    def run(self, remote='localhost', secured=False):

        self.remote = remote

        if "amqp://" in self.remote:
            url = self.remote
        elif "amqps://" in self.remote:
            url = self.remote
        else:
            url = 'amqp://{}'.format(self.remote)

        if secured:
            url = url.replace("amqp://", "amqps://")
            
        self.comm = kiwipy.connect(url)

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
        