# Easykiwi

Easykiwi is a Python Framework for developing Queue Messaging Application in a declarative approach, it depends on the **kiwipy** python library, in fact it turns this library into a container friendly framework.

## Requirements

- Python 3.6+
- RabbitMQ

## Defining Application

```python
from easykiwi import Kiwi

app = Kiwi()
```

## Adding RPCs

```python
@app.add_rpc
def fib(comm, num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    return fib(comm, num - 1) + fib(comm, num - 2)

```

## Adding Tasks

```python
@app.add_task
def callback(_comm, task):
    print((" [x] Received %r" % task))
    time.sleep(task.count(b'.'))
    print(" [x] Done")
```

## Adding Broadcast

```python
@app.add_broadcast
def subscriber(_comm, body, sender, subject, _corr_id):
    print("Broadcast received:")
    print("sender:\t{}\nsubject:{}\nbody:\t{}\n".format(
        sender, subject, body))
```

## Running Application

```python
app.run(remote='127.0.0.1')
```

# Running Application from Console Script

Yon can save your `app` in a **app.py** file or save it in an **KIWI_APP** environment variable, and then from the terminal execute the following.

```
kiwi run --remote 127.0.0.1
```

This command is a more container friendly approach to run this messaging service.
