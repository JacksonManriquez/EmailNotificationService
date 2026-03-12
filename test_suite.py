import requests

data = {
    "email": "pukuku101@gmail.com",
    "subject": "Login Notification",
    "message": "You have successfully signed in."
}

requests.post("http://192.168.4.37:3002/send-email", json=data)