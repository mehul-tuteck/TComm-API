from passlib.context import CryptContext;
import random, smtplib, twilio;
from twilio.rest import Client;
from email.message import EmailMessage;



def generate_hash_password(password : str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto");
    hash_password = pwd_context.hash(password);
    print(hash_password);

    return hash_password;


def generate_random_otp():
    return random.randint(1000, 9999);
    
    
def send_otp_in_email(otp : int, email : str):
   message = EmailMessage();
   message["Subject"] = "4-digits OTP";
   message["From"] = "aritrikagoswami15tuteck@gmail.com";
   message["To"] = email;
   message.set_content(f"Your OTP is: {otp}");

   server = smtplib.SMTP("smtp.gmail.com", 587);
   server.starttls();

   server.login("aritrikagoswami15tuteck@gmail.com", "gwjnuvrzwpwyutpq"); 
   server.send_message(message);
  


def send_otp_in_phone(otp : int, phone : str):  
        #Create a Twilio client
        client = twilio.rest.Client("ACc92ca64ce89ce86f0880635ed5ca8f6c", "43d293aa2c38d183e4925ccab7a6bcc9"); 

        #Send the OTP
        message = client.messages.create (
            body = "Your 4-digits OTP is: "+ str(otp),
            to = phone,
            from_ = "+13252465690"
        )
        #print("message.sid is: ", message.sid);
        