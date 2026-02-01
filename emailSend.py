# NOT IN USE


from smtplib import SMTP
from flask import Flask, request, render_template
from email.message import EmailMessage

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/contact", methods=["GET", "POST"])
def send_email():
    if request.method == "POST":
        fromName = request.form.get("name")
        fromEmail = request.form.get("email")
        fromMessage = request.form.get("message")

        # fromEmail = ""
        emailTo = ""
        subject = f"New message from {fromName} of {fromEmail} from Portfolio website"
        user = ""
        password = "your_app_password_here"  # Use an app password or environment variable for security

        msg = EmailMessage()
        msg.set_content(fromMessage)
        msg["Subject"] = subject
        msg["From"] = user
        msg["To"] = emailTo
        msg["Reply-To"] = fromEmail

        smtp = SMTP("smtp.gmail.com", 587)
        smtp.set_debuglevel(1)

        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user=user, password=password)
        smtp.send_message(msg)
        smtp.quit()

    return render_template("ContactMe.html")

if __name__ == "__main__":
    app.run(debug=True)