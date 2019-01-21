import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


class Mail:
    def __init__(self, receiver_email, username, comment):
        """Initialize an mail object"""
        self.receiver_email = receiver_email
        self.username = username
        self.comment = comment
        self.sender_email = "manorlds.testmail@gmail.com"
        self.password = os.environ['MAIL_PASSWORD']

    def notify_change_in_incident_status(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "iReporter - status change"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        html = """\
        <html>
        <body>
            <p><h6>Hello {0},</h6><br>
            Greetings. Hope this mail from iReporter finds you in good health.<br>
            <h3> This email is to notify you that your redflag has got some good attention from the iReporter admin. Go to platform for further details.
        <br><span style="margin: 0 auto !important; color:#0f97d0">Red-flag detail: {1}</span></h3>
            <a href="http://www.iReporter.com">iReporter</a>
            for more details
            </p>
        </body>
        </html>
        """.format(self.username, self.comment)

        message.attach(MIMEText(html, "html"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, message.as_string()
            )

    def welcome_new_user(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "iReporter - Welcome"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        html = """\
        <html>
        <body>
            <p><h6>Hello {0},</h6><br>
            Greetings.<br>
            <h2> Welcome To iReporter! A Stand against corruption.</h2>
            <a href="http://www.iReporter.com">iReporter</a>
            </p>
        </body>
        </html>
        """.format(self.username, self.comment)

        message.attach(MIMEText(html, "html"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, message.as_string()
            )
