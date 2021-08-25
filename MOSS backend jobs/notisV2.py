import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "ssrg.job.status@gmail.com"
EMAIL_PASSWORD = "ndxsas021hlnsan005rmrsuv002"


msg = EmailMessage()
msg['Subject']="MOSS Sample Job Notification using smtp"
msg['From']=EMAIL_ADDRESS
msg['To']= "rmrsuv002@myuct.ac.za, hlnsan005@myuct.ac.za, ndxsas021@myuct.ac.za"
msg.add_alternative("""\
 <!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>A Basic HTML5 Template</title>
  <meta name="description" content="A simple HTML5 Template for new projects.">
  <meta name="author" content="SitePoint">

  <meta property="og:title" content="A Basic HTML5 Template">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.sitepoint.com/a-basic-html5-template/">
  <meta property="og:description" content="A simple HTML5 Template for new projects.">
  <meta property="og:image" content="image.png">

  <link rel="icon" href="/favicon.ico">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <!-- your content here... -->
  <h1>Our future email Template this is html find sample report attached</h1>


</body>
</html>
""", subtype='html')

with open("samplereport.pdf", 'rb') as f:
    file_data = f.read()
    file_name = f.name


msg.add_attachment(file_data, maintype='application', subtype= 'octet-stream', filename= file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #login to mail server
    smtp.send_message(msg)