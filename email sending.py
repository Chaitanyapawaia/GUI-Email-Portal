import smtplib 
from email.mime.text import MIMEText

useremailaddress= input("Enter Your Gmail Id : ")
useremailpassword= input("Enter Your Gmail Password : ")
receiveersemailaddress= input("Enter Receiver's Gmail Id : ")
subject= input("Enter the subject of the mail : ")
body= input("Enter the body of the mail : ")


smtp = smtplib.SMTP('smtp.gmail.com')
smtp.set_debuglevel(0)
smtp.connect('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login(useremailaddress, useremailpassword )

text_subtype = 'plain'
content= body
msg = MIMEText(content, text_subtype)
msg['Subject']= subject
msg['From']= useremailaddress
msg['To']= receiveersemailaddress
    
smtp.sendmail(useremailaddress, receiveersemailaddress, msg.as_string())
smtp.quit()