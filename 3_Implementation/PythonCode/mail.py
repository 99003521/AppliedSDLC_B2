import smtplib  
# creates SMTP session 
s = smtplib.SMTP('ragulperi@gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("ragulperi@gmail.com", "Krishna0918$") 
  
# message to be sent 
message = "Testing ksro bhaiiiii"
  
# sending the mail 
s.sendmail("ragulperi@gmail.com", "jocago3836@mayhco.com", message) 
  
# terminating the session 
s.quit() 