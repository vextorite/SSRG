import smtplib
from email.message import EmailMessage

#WILL BE STORED AS ENVIROMENT VARIABLES
EMAIL_ADDRESS = "ssrg.job.status@gmail.com"
EMAIL_PASSWORD = "ndxsas021hlnsan005rmrsuv002"

def sendMail(recipient, status, exportFilePath):
    msg = EmailMessage()
    msg['Subject']="MOSS Sample Job Notification using smtp"
    msg['From']=EMAIL_ADDRESS
    msg['To']=recipient
    # we will have status here to decide what html to send done using ifs
    if(status==True):
        msg.add_alternative("""<h1>This job has been completed</h1>
         <p>please find your report attached below</p>""")
        with open(exportFilePath, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype= 'octet-stream', filename= file_name)
    
    else:
        msg.add_alternative("""<h1>This job is processing</h1>
         <p>please find your report attached below</p>""")

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #login to mail server
        smtp.send_message(msg)