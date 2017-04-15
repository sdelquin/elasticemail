import elasticemail

# send simple email to one recipient
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "This is the body"
)
print(r)

# send simple email to several recipients
r = elasticemail.send(
    ["email1@address.com", "email2@address.com"],
    "This is the subject",
    "This is the body"
)
print(r)

# send email with html in the body
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "<h1>The title</h1>"
    "<p>The body including html tags</p>"
)
print(r)

# send email with one attached file
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "This is the body",
    "photo.jpg"
)
print(r)

# send email with several attached files
r = elasticemail.send(
    "email@address.com",
    "This is the subject",
    "This is the body",
    ["photo.jpg", "photo2.jpg"]
)
print(r)
