from json import loads
from app.main.forms.contact import ContactPayload


class ContactSerializer:
  
  def __init__(self, contact_message: str) -> None:
    self.__contact_message = contact_message
    
  def serialize(self) -> ContactPayload:
    return ContactPayload(**loads(self.__contact_message))
