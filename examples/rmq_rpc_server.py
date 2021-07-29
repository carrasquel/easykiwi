# -*- coding: utf-8 -*-

from easykiwi import Kiwi

app = Kiwi()


@app.add_rpc
def fib(_comm, num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(_comm, num - 1) + fib(_comm, num - 2)


@app.add_rpc
def fac(_comm, num):
    result = 1
    if num > 1:
        result = num * fac(_comm, num - 1)
    return result


if __name__ == '__main__':
    
    app.run(remote="127.0.0.1")
