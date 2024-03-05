# SendMail.py
Send emails using the command prompt. This should work on Linux, Windows, and MacOS.
It will automatically send emails as either SSL or TLS depending on the port thats used. Unencrypted SMTP support isn't built into this.

# Usage
Python-SendMail.py -I smtp.mail.com -i 587 -u test@mail.com -p "supersecurepassword" -r recpient@gmail.com -s "Subject" -m "HELLO WORLD!!"

# Installation
On the releases page I compiled the script into a Windows binary using PyInstaller.
Build it into your own EXE unless you're lazy and trust a random guy online

Hope this useful for someone! - Peter
