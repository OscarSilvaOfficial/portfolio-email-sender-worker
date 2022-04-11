from app.factories.email_sender import Factory
from app.main.forms.contact import ContactPayload

def send_mail(payload: ContactPayload):
  sender = Factory.email_sender()
  subject = 'Contato Portfólio'
  message = f'Nome: {payload.name}\nEmail: {payload.email}\nMensagem: {payload.message}'
  sender.send(subject, message)
  return { "message": "Email enviado com sucesso" }