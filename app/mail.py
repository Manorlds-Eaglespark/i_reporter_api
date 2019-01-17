import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, receiver_email, username, comment):
        """Initialize an mail object"""
        self.receiver_email = receiver_email
        self.username = username
        self.comment = comment
        self.sender_email = "manorlds.testmail.com"
        self.password = os.environ.get("SECRET_KEY")

    def notify_change_in_incident_status(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
 
        html = """\
        <html>
        <body>
            <p>Hello {0},<br>
            Greetings. Hope this mail from iReporter finds you in good health.<br>
            <h2 > This email is to notify you that your redflag has got some good attention from the iReporter admin. Go to platform for further details.
        Red-flag detail: {1}</h2>
            <a href="http://www.iReporter.com">iReporter</a> 
            for more details
            </p>
        </body>
        </html>
        """.format(self.username, self.comment)

        part_mail = MIMEText(html, "html")

        message.attach(part_mail)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def welcome_new_user(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        html = """\
        <html>
        <body>
            <p>Hello {0},<br>
            Greetings. Hope this mail from iReporter finds you in good health.<br>
            <h2> Welcome To iReporter! A Stand against corruption.</h2>
            <a href="http://www.iReporter.com">iReporter</a> 
            </p>
        </body>
        </html>
        """.format(self.username, self.comment)

        part_mail = MIMEText(html, "html")

        message.attach(part_mail)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
