from twilio.rest import Client
import random

account_sid = 'your sid'
auth_token = 'your token'

def sendOTP(number):
    six_digit_number = random.randint(100000, 999999)  # Range for 6-digit numbers
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body= f"Your OTP(One Time Passwword) of FitnessX is *{six_digit_number}* 🤫🤐 *Don't share it with anyone*",
    to=f'whatsapp:+91{number}'
    )
    print(message.sid)
    return six_digit_number
    
