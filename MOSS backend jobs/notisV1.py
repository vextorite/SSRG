import smtplib

EMAIL_ADDRESS = "ssrg.job.status@gmail.com"
EMAIL_PASSWORD = "ndxsas021hlnsan005rmrsuv002"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() #identifies us with the maill server we are using
    smtp.starttls()#encrypt traffic
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #login to mail server

    subject = "Testing python email"
    body = "Did this work?"
    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(EMAIL_ADDRESS, "rmrsuv002@myuct.ac.za", msg)