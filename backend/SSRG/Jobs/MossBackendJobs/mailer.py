import smtplib
from email.message import EmailMessage
from generateHtml import emailHtmlBody

#WILL BE STORED AS ENVIROMENT VARIABLES
EMAIL_ADDRESS = "ssrg.job.status@gmail.com"
EMAIL_PASSWORD = "ndxsas021hlnsan005rmrsuv002"




def sendNotification(recipient, jobID, jobStatus, exportFilePath):
    '''
    The function sends out HTML emails to the user with the respective MOSS job
    The sendNotification function takes in four parameters namely:
    recipient - Email address of user that submitted the MOSS job
    jobID -  Unique identifier of submitted job
    exportFilePath - Path of pdf report attachment
    '''
    msg = EmailMessage()
    msg['From']=EMAIL_ADDRESS # SSRG email
    msg['To']=recipient  # email address of person receiving the mail
    msg['Subject']=f"MOSS Job {jobID}, Status: {jobStatus}" # subject of the email
    msg.add_alternative(emailHtmlBody(recipient, jobID, jobStatus), subtype ='html')
    if(jobStatus == 'done'):
        with open(exportFilePath, 'rb') as f:
            file_data = f.read()
            file_name = f'MossReport_{jobID}.pdf'
        msg.add_attachment(file_data, maintype='application', subtype= 'octet-stream', filename= file_name )
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #login to mail server
        smtp.send_message(msg)