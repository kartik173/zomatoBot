import smtplib
from email.message import EmailMessage

class Mail:
    
    def __init__(self, recieverId, content):
        self.id = recieverId
        self.content = content
    
    def send(self):
        
        # sender credentials
        sender_address = 'kartik10messi@gmail.com'
        sender_pass = 'K@rtik123'
    
        # construct email
        message = EmailMessage()
        message['From'] = sender_address
        message['To'] = self.id
        message['Subject'] = 'Top 10 restraunt list'
        message.set_content(self.content, subtype='html')
        
        # Send the message via local SMTP server.
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_address, sender_pass)
            s.send_message(message)
        
       
        print('Mail Sent')
    
    