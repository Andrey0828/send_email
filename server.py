from flask import Flask, request, jsonify
from flask_cors import CORS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config import PASSWORD

app = Flask(__name__)
CORS(app)


@app.route('/receive_object', methods=['POST'])
def receive_object():
    data = request.json
    sender_email = "steamscroller_yandex@mail.ru"
    sender_password = PASSWORD
    recipient_email = "snowy.06@mail.ru"

    message = f"""
    <html>
        <head></head>
        <body>
            <h2 style="color: #3498db;">Portfolio</h2>
            <p><strong>Имя:</strong> {data['name']}</p>
            <p><strong>Почта:</strong> {data['email']}</p>
            <p><strong>Сообщение:</strong> {data['message']}</p>
        </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg['Subject'] = 'Portfolio'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.attach(MIMEText(message, 'html'))

    smtp_server = 'smtp.mail.ru'
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)

    server.quit()
    return jsonify({'message': 'Object received successfully'})


if __name__ == '__main__':
    app.run(debug=True)
