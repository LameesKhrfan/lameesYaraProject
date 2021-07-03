import smtplib
username='User Name'
password=input('pleas enter your password: ')
sender='from@gmail.com'
reciver='to@gmail.com'
subject='title the mail'
mailContent="this is an e-mail message to be sent in python"
header="to:"+reciver +'\n' +'From:'+sender +'\n'+'Subject:'+subject+'\n'
message=header+mailContent
try:
    smtpObj=smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(sender,password)
    smtpObj.sendmail(sender,reciver,message)
    smtpObj.close()
    print('Successfully sent email')
except Exception:
    print('Error:unable to send email')
