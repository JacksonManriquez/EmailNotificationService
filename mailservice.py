from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
# Simply creates a list of blocked emails that the program cannot send to.
def load_blacklist():
    with open("blacklist.txt") as f:
        return set(line.strip() for line in f)
    


app = Flask(__name__)

# Example email and password
EMAIL_ADDRESS = "saltedhampukuku@gmail.com"
EMAIL_PASSWORD = "oaxm zncs oiau jvhi"

#calls blacklist
Black_List = load_blacklist()

def send_email(to_email, subject, message):
    #Adds unsubscribe link to email.
    unsubscribe_link = f"http://3.129.216.60:3002/blacklist?email={to_email}"
    message_with_link = message + f"\n\nTo stop receiving these emails click:\n{unsubscribe_link}"

    msg = MIMEText(message_with_link)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    #Checks for blocked address
    if to_email in Black_List:
        return { "error": "Email address blocked"}

    # Makes api request to gmail and sends email on your behalf
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


@app.route("/blacklist", methods=["GET"])
def blacklist_email():

    email = request.args.get("email")

    if not email:
        return "No email provided", 400

    Black_List.add(email)

    with open("blacklist.txt", "a") as f:
        f.write(email + "\n")

    return "Email successfully unsubscribed."




if __name__ == "__main__":
    # Runs on EC2 server currenty, can be changed to local, switch to commetned line. De bug allows program to be changed
    app.run(host='0.0.0.0', port=3002, debug=True)
    #app.run(port=3002, debug=True)
