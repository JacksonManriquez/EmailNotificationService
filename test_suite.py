import requests

data = {
    "email": "pukuku101@gmail.com",
    "subject": "Login Notification",
    "message": "You have successfully signed in."
}

requests.post("http://localhost:5001/send-email", json=data)