# -*- coding: utf-8 -*-

from easykiwi import Kiwi

app = Kiwi()


@app.add_broadcast
def on_broadcast_send(_comm, body, sender, subject, __):
    print(' [x] listening on_broadcast_send:')
    print(f' body: {body}, sender {sender}, subject {subject}\n')



@app.add_broadcast(filters=['purchase.*'])
def on_broadcast_filter(_comm, body, sender=None, subject=None, __=None):
    print(' [x] listening on_broadcast_filter:')
    print(f' body: {body}, sender {sender}, subject {subject}\n')


if __name__ == '__main__':
    
    app.run(remote='127.0.0.1')
    