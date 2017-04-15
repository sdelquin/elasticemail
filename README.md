# Elastic Email

Wrapper in python to send mails with transactional service ElasticEmail.

## Configuration

1. Set up a virtualenv with *python3*.
2. Set the corresponding values in the configuration file:
    ```console
    $> cp config.py.example config.py
    ```
4. Install the requirements:
    ```console
    $> pip install requirements.txt
    ```

## Use

```python
import elasticemail

# send simple email to one recipient
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "This is the body"
)

# send simple email to several recipients
r = elasticemail.send(
    ["email1@address.com", "email2@address.com"],
    "This is the subject",
    "This is the body"
)

# send email with html in the body
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "<h1>The title</h1>"
    "<p>The body including html tags</p>"
)

# send email with one attached file
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "This is the body",
    "photo.jpg"
)

# send email with several attached files
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "This is the body",
    ["photo.jpg", "photo2.jpg"]
)
```
