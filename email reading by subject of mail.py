import imaplib
import email 
  
user = input("Enter Your Gmail Address : ")
password = input("Enter The password Of Your Gmail Id : ")
subject_search = input("Enter The Subject Of The Mail : ")
imap_url = 'imap.gmail.com'

def get_body(msg): 
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True) 
   
def search(key, value, con):  
    result, data = con.search(None, key, '"{}"'.format(value)) 
    return data 
  
def get_emails(result_bytes): 
    msgs = [] 
    for num in result_bytes[0].split(): 
        typ, data = con.fetch(num, '(RFC822)') 
        msgs.append(data) 
    return msgs 
 
con = imaplib.IMAP4_SSL(imap_url)  

con.login(user, password)  

con.select('Inbox')  

test_bytes = search('SUBJECT', subject_search , con) 

msgs = get_emails(test_bytes) 
  

for msg in msgs[::-1]:  
    for sent in msg: 
        if type(sent) is tuple:
            try:
                              
                content = str(sent[1], 'utf-8')
                mail=str(content)
                mail=mail[-2000:]
                subject_start=mail.find("Subject:")
                from_start=mail.find("From:")
                subject_start= subject_start+9
                from_start=from_start+ 6
                from_end=mail.find("Date:")
                subject_end=mail.find("To:")
                from_end=from_end-2
                subject_end= subject_end-2
                body_start=mail.find('Content-Type: text/plain; charset="UTF-8"')
                body_start=body_start + 44
                body_end= mail.find('Content-Type: text/html; charset="UTF-8"')
                body_end= body_end-33
                
                print( "From:", mail[from_start:from_end])
                print( "Subject:", mail[subject_start:subject_end])
                print('body:', mail[body_start:body_end])
                
                
            except UnicodeEncodeError as e: 
                pass