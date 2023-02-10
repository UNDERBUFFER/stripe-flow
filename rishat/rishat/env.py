import os

from dotenv import load_dotenv

load_dotenv('.env')

ENV = {
    'DB_CONNECTION_STRING': os.getenv('DB_CONNECTION_STRING', ''),
    'STRIPE_API_KEY': os.getenv('STRIPE_API_KEY', ''),
    'SUCCESS_PAYMENT_URL': os.getenv('SUCCESS_PAYMENT_URL', 'http://localhost:7070/success'),
}
