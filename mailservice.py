from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

def load_blacklist():
    with open("blacklist.txt") as f:
        return set(line.strip() for line in f)
    


app = Flask(__name__)

EMAIL_ADDRESS = "saltedhampukuku@gmail.com"
EMAIL_PASSWORD = "oaxm zncs oiau jvhi"




def send_email(to_email, subject, message):


    Black_List = load_blacklist()
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    if to_email in Black_List:
        return { "error": "Email address blocked"}

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

@app.route("/send-email", methods=["POST"])
def email_endpoint():

    data = request.json

    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    if not email or not message:
        return jsonify({"error": "Missing email or message"}), 400

    success = send_email(email, subject, message)

    if success:
        return jsonify({"status": "Email sent"})
    else:
        return jsonify({"status": "Failed to send email"}), 500




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3002, debug=True)

