from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

EMAIL_ADDRESS = "saltedhampukuku@gmail.com"
EMAIL_PASSWORD = "oaxm zncs oiau jvhi"


def send_email(to_email, subject, message):

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        return True

    except Exception as e:
        print("Email error:", e)
        return False






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

