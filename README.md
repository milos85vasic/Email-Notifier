# Email Notifier

Send messages to chosen email addresses. Used mainly as tool for reporting.

## How to use

- Clone the project
- In project root create configuration.py with the following structure (as example):

```python
configurations = {
    "notifier1": {
        "smtp_server": "mail.example.com",
        "username": "user",
        "password": "password",
        "sender": "notifier@example.com",
        "receiver": "receiver@example.com"
    }
}
```

- Run command:
```
$ python notify.py "This is a sample message."
```

or

```
$ python notify.py "This is a sample message." --configuration="notifier1"
```

If notifier configuration name is not provided, notifier will send to all configurations!

- To use multiple configurations:

```
$ python notify.py "This is a sample message." --configuration="notifier1, notifier2, notifier3"
```

- Or with pipeline:
```
$ some_command | python notify_pipe.py
```

or

```
$ some_command | python notify_pipe.py --configuration="notifier1"
```