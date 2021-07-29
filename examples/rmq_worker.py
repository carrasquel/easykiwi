# -*- coding: utf-8 -*-
import time

from easykiwi import Kiwi

print(' [*] Waiting for messages. To exit press CTRL+C')

app = Kiwi()


@app.add_task
def callback(_comm, task):
    print(f' [x] Received {task!r}')
    time.sleep(task.count('.'))
    print(' [x] Done')
    return task


if __name__ == "__main__":

    app.run(remote="127.0.0.1")
