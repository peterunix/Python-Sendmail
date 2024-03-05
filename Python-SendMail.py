#!/usr/bin/python3
# This sends emails through a CLI! That's it.
# Use the "-h" flag to see the usage.
import smtplib,ssl
import sys, getopt

def usage():
    print(f'{sys.argv[0]} -I smtp.mail.com -i 587 -u test@mail.com -p "supersecurepassword" -r recpient@gmail.com -s "Subject" -m "HELLO WORLD!!"')

# Get the users cli args and catch the error if an invalid arg is passed
try:
    commandLineArgs = sys.argv[1:]
    #"-I -i -s -u -p -m -h"
    unixOptions = "I:i:s:u:p:r:m:h"
    opts, args = getopt.getopt(commandLineArgs, unixOptions)
except getopt.GetoptError as e:
    print(f"ERROR: {e}")
    usage()
    sys.exit(2)

# Create new variables to store the users args
for opt, arg in opts:
    if opt == "-h":
        usage()
        sys.exit(0)
    elif opt == "-I":
        smtpServer = arg
    elif opt == "-i":
        smtpPort = arg
    elif opt == "-u":
        username = arg
    elif opt == "-p":
        password = arg
    elif opt == "-s":
        subject = arg
    elif opt == "-m":
        message = arg
    elif opt == "-r":
        recipient = arg

# Exit if the user didn't input all arguments
mandatory_options = ["-I","-i","-u","-p","-r","-s","-m"]
for opt in mandatory_options:
    if not any(opt in o for o in opts):
        print(f"Error: {opt} option missing. Review usage with -h")
        usage()
        sys.exit(2)


# Sending the email with ssl or tls depending on port number
if smtpPort == "465":
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtpServer, smtpPort) as smtp:
        smtp.login(username, password)
        msg = f'Subject: {subject}\n\n{message}'
        smtp.sendmail(username, recipient, msg)
elif smtpPort == "587":
    with smtplib.SMTP(smtpServer, smtpPort) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username, password)
        msg = f'Subject: {subject}\n\n{message}'
        smtp.sendmail(username, recipient, msg)
else:
    print("This program only works with port 587 (TLS) and 465 (SSL)")
    print("If you want to use unencrypted port 25, edit this code block")
