import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailCredentials():
  
  def __init__(self, email_sender, email_sender_pass) -> None:
    self.__sender_address = email_sender
    self.__sender_pass = email_sender_pass
  
  @property
  def email(self):
    return self.__sender_address
  
  @property
  def password(self):
    return self.__sender_pass
  
class SMTPServerInfo():
  
  def __init__(self, smtp_server: str = 'smtp.gmail.com', smtp_port: int = 587):
    self.__smtp_server = smtp_server
    self.__smtp_port = smtp_port
    
  @property
  def server(self):
    return self.__smtp_server
  
  @property
  def port(self):
    return self.__smtp_port
  

class EmailSender():
  
  def __init__(self, credentials: EmailCredentials, smtp: SMTPServerInfo) -> None:
    self.__credentials = credentials
    self.__smtp = smtp
    
  def __load_email_content(self, subject: str, mail_content: str) -> str:
    content = MIMEText(mail_content, 'plain')
    message = MIMEMultipart()
    message['From'] = self.__credentials.email
    message['To'] = self.__credentials.email
    message['Subject'] = subject
    message.attach(content)
    return message.as_string()

  def send(self, subject: str, message: str) -> None:
    text = self.__load_email_content(subject, message)
    session = smtplib.SMTP(self.__smtp.server, self.__smtp.port) 
    session.starttls()
    session.login(self.__credentials.email, self.__credentials.password)
    session.sendmail(self.__credentials.email, self.__credentials.email, text)
    session.quit()
