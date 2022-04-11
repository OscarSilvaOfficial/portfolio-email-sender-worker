import os
from dotenv import load_dotenv

load_dotenv()

ROOT_EMAIL=os.environ.get('EMAIL')
ROOT_PASSWORD=os.environ.get('PASSWORD')
KAFKA_BROKERS=[os.environ.get('KAFKA_BROKER_URL')]