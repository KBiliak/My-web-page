import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "pythonlangdevua@gmail.com"
password = "bljrgrgctvwvopkx"

receiver = "pythonlangdevua@gmail.com"
context = ssl.create_default_context()



with smtplib.SMTP_SSL(host, port, context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
