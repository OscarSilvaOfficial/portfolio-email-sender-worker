from app.main.configs.enviroment import KAFKA_BROKERS
from app.main.serializer.contact_serializer import ContactSerializer
from kafka import KafkaConsumer
from app.main.contacts import send_mail

consumer = KafkaConsumer('contact', group_id="email-sender-group", bootstrap_servers=KAFKA_BROKERS)

while True:
  for message in consumer:
    contact = ContactSerializer(message.value).serialize()
    send_mail(contact)
  