import requests

data = {
    "email": "example@gmail.com",
    "subject": "Login Notification",
    "message": "You have successfully signed in. \n Please dont read this"
    
}

requests.post("http://3.129.216.60:3002/send-email", json=data)