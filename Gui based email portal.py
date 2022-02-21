import tkinter
import smtplib 
from email.mime.text import MIMEText
import imaplib
import datetime
import email
import mysql.connector as mysqlc

db = mysqlc.connect(host="localhost", user="root", passwd="ol9E", database="ModiMail")  
cursor= db.cursor()

user_id = ""
user_password = ""
receiver_id= ""
mail_subject= ""
mail_body= ""
sender_id= ""
sender_mailsubject= ""

login_id = ""
login_password = ""

loginaccess = 0

def search_bysubject():
    user = user_id
    password = user_password
    subject_search = sender_mailsubject
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
                    
                    Fromfrom= mail[from_start:from_end]
                    Subjectsubject= mail[subject_start:subject_end]
                    Bodybody= mail[body_start:body_end]
                    
                    view_mailbox1.insert(1.0, '__________________________________________________________________\n\n')
                    
                    view_mailbox1.insert(1.0,  Bodybody,'\n', '\n')
                    view_mailbox1.insert(1.0, 'Body : ')
                    view_mailbox1.insert(1.0,  Subjectsubject, '\n', '\n')
                    view_mailbox1.insert(1.0, 'Subject : ')
                    view_mailbox1.insert(1.0,  Fromfrom, '\n', '\n')
                    view_mailbox1.insert(1.0, 'From : ')
                    
                    view_mailbox1.place(x='200', y='530')
                    
                except UnicodeEncodeError as e: 
                    pass

def check_mailsubject():
        
    global sender_mailsubject
    sender_mailsubject= sendermailsubject.get()
    search_bysubject()
    
def sortbysubject():
    Sendersmailaddress.place_forget()
    sendermailid.place_forget()
    nextbutton.place_forget()
    error3.place_forget()
    
    view_mailbox.place_forget()
    mailsubject.place(x='50', y='420')
    sendermail_subject.place(x='385', y='425')
    nextbutton1.place(x='600', y='460')
    

def search_byid():
    user = user_id
    password = user_password
    user_search = sender_id
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

    test_bytes = search('FROM', user_search , con) 

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
                
                    Fromfrom= mail[from_start:from_end]
                    Subjectsubject= mail[subject_start:subject_end]
                    Bodybody= mail[body_start:body_end]
                    
                    view_mailbox.insert(1.0, '__________________________________________________________________\n\n')
                    
                    view_mailbox.insert(1.0,  Bodybody,'\n', '\n')
                    view_mailbox.insert(1.0, 'Body : ')
                    view_mailbox.insert(1.0,  Subjectsubject, '\n', '\n')
                    view_mailbox.insert(1.0, 'Subject : ')
                    view_mailbox.insert(1.0,  Fromfrom, '\n', '\n')
                    view_mailbox.insert(1.0, 'From : ')
                    
                    view_mailbox.place(x='200', y='530')
                                
                except UnicodeEncodeError as e:
                    pass


def check_senderid():
    sender__id= senderid.get()
    
    if sender__id=="":
        error3.place(x='420', y='455')
    elif sender__id[-4:]!= '.com':
        error3.place(x='440', y='445')
    else:
        error3.place_forget()
        global sender_id
        sender_id= senderid.get() 
        search_byid()
    
def sortbyaddress():
    mailsubject.place_forget()
    sendermail_subject.place_forget()
    nextbutton1.place_forget()
    view_mailbox1.place_forget()
    Sendersmailaddress.place(x='50', y='420')
    sendermailid.place(x='470', y='425')
    nextbutton.place(x='600', y='480')
    
def view_mail_selection():
    receivermailid.place_forget()
    r_id.place_forget()
    sub_ject.place_forget()
    sub.place_forget()
    bo_dy.place_forget()
    body.place_forget()
    send.place_forget()
    send_conformation.place_forget()
    send_failure.place_forget()
    send_failure2.place_forget()
    bysendersaddress.place(x='100', y='365')
    bymailsubject.place(x='505', y='365')
    
def send_mail():
    try:
        
        useremailaddress= user_id
        useremailpassword= user_password
        receiversemailaddress= receiver_id
        subject= mail_subject
        body= mail_body
        
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
        msg['To']= receiversemailaddress
        
        smtp.sendmail(useremailaddress, receiversemailaddress, msg.as_string())
        smtp.quit()
        
        date_time = str(datetime.datetime.now()).split()
        date,time = date_time
        time= time.split(".")
        time=time[0]

        cursor.execute("insert into sentmails( Date, Time, Sent_To, Sent_From, Subject, Body)values('{}','{}','{}','{}','{}','{}')".format(date, time, receiversemailaddress, useremailaddress, subject, body))
        db.commit()
        
        send_conformation.place(x='120', y='580')
        send_failure.place_forget()
        send_failure2.place_forget()
        
    except:
        send_failure.place(x='100', y='580')
        send_failure2.place(x='90', y='620')
        send_conformation.place_forget()

def check_receiverid():
    
    receiver__id= receiverid.get()
    
    if receiver__id == "" :
        error2.place(x='330',y='390')
        
    elif receiver__id[-4:]!= '.com':
         error2.place(x='330',y='390')
            
    else:
        error2.place_forget()
        global receiver_id, mail_subject, mail_body
        receiver_id= receiverid.get()
        mail_subject= subject.get()
        mail_body= body.get("1.0",'end-1c')
        send_mail()

def send_mail_entry():
    bymailsubject.place_forget()
    bysendersaddress.place_forget()
    Sendersmailaddress.place_forget()
    sendermailid.place_forget()
    nextbutton.place_forget()
    error3.place_forget()
    view_mailbox.place_forget()
    mailsubject.place_forget()
    sendermail_subject.place_forget()
    nextbutton1.place_forget()
    view_mailbox1.place_forget()
    receivermailid.place(x='50',y='360')
    r_id.place(x='440', y='365')
    sub_ject.place(x='50',y='420')
    sub.place(x='440', y='425')
    bo_dy.place(x='50',y='450')
    body.place(x='415', y='455')
    send.place(x='150', y='530')
    
def serviceselection():
    service.place(x='50',y='270')
    sendmail.place(x='150', y='310')
    viewmail.place(x='300', y='310')

def check_id_password():
    user__id = userid.get()
    user__password = userpassword.get()

    if user__id == "" or user__password == "" :
        error1.place(x='330',y='185')
    
    elif user__id[-10:]!='@gmail.com' :
        error1.place(x='330',y='185')
       
    else:
        error1.place_forget()
        global user_id, user_password
        user_id = userid.get()
        user_password = userpassword.get()
        serviceselection()


def check_login_id_password():
    login__id= loginid.get()
    login__password= loginpassword.get()
    cursor.execute("SELECT * FROM loginids where Loginid = '{}' and Loginpassword = '{}'".format(login__id, login__password))
    value=cursor.fetchall()
    if len(value) == 1 :
        error4.place_forget()
        global login_id, login_password
        login_id = login__id
        login_password = login__password
        global loginaccess
        loginaccess=1
        window_login.destroy()
    else:
        error4.place(x='60',y='100')        
        

window_login = tkinter.Tk()
window_login.geometry("500x200")
window_login.title('Login To Modi Mail')
window_login.iconbitmap(r'C:\\Users\\Chaitanya\\Documents\\Python Scripts\\GUI_Email_Portal\\modimail pic.ico')
window_login.configure(background='#006341')

loginid= tkinter.StringVar()
loginpassword= tkinter.StringVar()

welc=tkinter.Label(window_login , text="LOGIN TO MODI MAIL", fg="#f0ebd2", bg='#006341', font=("glacial indifference", 18,'bold'))
welc.pack()

loginappid=tkinter.Label(window_login, text="Please Enter Your Username :", fg="#f0ebd2", bg='#006341', font=("Rubik One", 10,'bold'))
loginappid.place(x='10',y='50')

l_id = tkinter.Entry(window_login, textvariable = loginid, width=40) 
l_id.place(x='205', y='50')

loginapppassword=tkinter.Label(window_login, text="Please Enter Your Password :", fg="#f0ebd2", bg='#006341', font=("Rubik One", 10,'bold'))
loginapppassword.place(x='10',y='80')

l_password = tkinter.Entry(window_login, textvariable = loginpassword, width=40, show="#") 
l_password.place(x='205', y='80')

loginbutton = tkinter.Button(text='Login', fg='white', bg='#5271ff', command=check_login_id_password, font=("Rubik One", 16,'bold'), height = 1, width = 6)
loginbutton.place(x='270', y='125')

error4 =tkinter.Label(window_login, text=" Invalid Login Details !!! Please Re-enter The Details. ", fg="#ff5757", bg='#006341', font=("Rubik One", 11,'bold'))
 
window_login.mainloop()



if loginaccess == 1 :
        
    window = tkinter.Tk()
    window.title('Modi Mail')
    window.state("zoomed")
    window.iconbitmap(r'C:\\Users\\Chaitanya\\Documents\\Python Scripts\\modimail pic.ico')
    window.configure(background='#65b4ab')

    userid= tkinter.StringVar()
    userpassword= tkinter.StringVar()
    receiverid= tkinter.StringVar()
    subject= tkinter.StringVar()
    senderid= tkinter.StringVar()
    sendermailsubject= tkinter.StringVar()

    welc=tkinter.Label(window, text="MODI MAIL", fg="#fff763", bg='#65b4ab', font=("glacial indifference", 44,'bold'))
    welc.pack()

    cred=tkinter.Label(window, text="To proceed Please Enter Your Credentials :", fg="white", bg='#65b4ab', font=("Playfair Display", 20, 'bold'))
    cred.place(x='50',y='70')

    mailid=tkinter.Label(window, text="Please Enter Your Gmail Address :", fg="black", bg='#65b4ab', font=("Rubik One", 16,'bold'))
    mailid.place(x='50',y='120')

    u_id = tkinter.Entry(window, textvariable = userid, width=45) 
    u_id.place(x='400', y='125')

    mailpassword=tkinter.Label(window, text="Please Enter Your Gmail Password :", fg="black", bg='#65b4ab', font=("Rubik One", 16,'bold'))
    mailpassword.place(x='50',y='155')

    u_password = tkinter.Entry(window, textvariable = userpassword, width=45, show="#") 
    u_password.place(x='415', y='160')

    error1=tkinter.Label(window, text=" Invalid Credentials !!! Please Re-enter The Credentials. ", fg="red", bg='#65b4ab', font=("Rubik One", 14,'bold'))
 
    submit= tkinter.Button(text='Submit', fg='white', bg='#5271ff', command=check_id_password, font=("Rubik One", 16,'bold'), height = 1, width = 10)
    submit.place(x='600', y='220')

    service=tkinter.Label(window, text="Please Select A Service :", fg="white", bg='#65b4ab', font=("Playfair Display", 20, 'bold'))

    sendmail= tkinter.Button(text='Send Mail', fg='white', bg='#5271ff', command= send_mail_entry, font=("Rubik One", 16,'bold'), height = 1, width = 10)

    viewmail= tkinter.Button(text='View Mail', fg='white', bg='#5271ff', command= view_mail_selection, font=("Rubik One", 16,'bold'), height = 1, width = 10)

    receivermailid=tkinter.Label(window, text="Please Enter The Receiver's Mail Id :", fg="black", bg='#65b4ab', font=("Rubik One", 16, 'bold'))

    r_id=tkinter.Entry(window, textvariable = receiverid, width=45)

    error2=tkinter.Label(window, text=" Invalid Credential !!! Please Re-enter The Credential. ", fg="red", bg='#65b4ab', font=("Rubik One", 14,'bold'))
 
    sub_ject=tkinter.Label(window, text="Please Enter The Subject Of The Mail :", fg="black", bg='#65b4ab', font=("Rubik One", 16, 'bold'))

    sub=tkinter.Entry(window, textvariable = subject, width=100) 

    bo_dy=tkinter.Label(window, text="Please Enter The Body Of The Mail :", fg="black", bg='#65b4ab', font=("Rubik One", 16, 'bold'))

    body=tkinter.Text(window, width=80, height= 20) 

    send= tkinter.Button(text='Send Mail', fg='white', bg='#5271ff', command=check_receiverid, font=("Rubik One", 16,'bold'), height = 1, width = 10)

    send_conformation=tkinter.Label(window, text="Email Sent ✓", fg="#439d1c", bg='#65b4ab', font=("Playfair Display", 25, 'bold'))

    send_failure=tkinter.Label(window, text="Email Not Sent ❌ ", fg="#ff1616", bg='#65b4ab', font=("Playfair Display", 25, 'bold'))

    send_failure2=tkinter.Label(window, text="Correct The Details", fg="#ff1616", bg='#65b4ab', font=("Playfair Display", 25, 'bold'))

    bysendersaddress= tkinter.Button(text='View Mail By Senders Mail Address', fg='white', bg='#5271ff', command=sortbyaddress, font=("Rubik One", 16,'bold'), height = 1, width = 30)

    bymailsubject= tkinter.Button(text='View Mail By Mail\'s Subject', fg='white', bg='#5271ff', command=sortbysubject, font=("Rubik One", 16,'bold'), height = 1, width = 30)
 
    Sendersmailaddress=tkinter.Label(window, text="Please Enter The Sender's Mail Address :", fg="black", bg='#65b4ab', font=("Rubik One", 16, 'bold'))

    sendermailid= tkinter.Entry(window, textvariable = senderid, width=45)

    nextbutton= tkinter.Button(text='Next', fg='white', bg='#5271ff', command=check_senderid, font=("Rubik One", 16,'bold'), height = 1, width = 10)

    error3=tkinter.Label(window, text=" Invalid Credential !!! Please Re-enter The Credential. ", fg="red", bg='#65b4ab', font=("Rubik One", 14,'bold'))

    view_mailbox= tkinter.Text(window, width=100, height= 12, font=("Rubik One", 12,'bold'), fg='black', bg='#03989e')

    mailsubject=tkinter.Label(window, text="Please Enter The Mail\'s Subject :", fg="black", bg='#65b4ab', font=("Rubik One", 16, 'bold'))

    sendermail_subject= tkinter.Entry(window, textvariable = sendermailsubject, width=45)

    nextbutton1= tkinter.Button(text='Next', fg='white', bg='#5271ff', command=check_mailsubject, font=("Rubik One", 16,'bold'), height = 1, width = 10)

    view_mailbox1= tkinter.Text(window, width=100, height= 15, font=("Rubik One", 12,'bold'), fg='black', bg='#03989e')

    window.mainloop()
    

db.close()



'''

Login page password: Chaitanya

'''







