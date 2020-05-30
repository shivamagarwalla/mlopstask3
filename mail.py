  #mail.py
  import smtplib 

	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

	# start TLS for security 
	s.starttls()   

	# Authentication 
	s.login("sender_email", "password")
 
	# message to be sent 
	message = "Your Model is Ready"

	# sending the mail 

	s.sendmail("sender_mail", "developr_mail", message)
	# terminating the session 

	s.quit()
