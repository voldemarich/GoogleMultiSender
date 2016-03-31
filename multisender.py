#!/usr/bin/python
__author__ = 'voldemarich'

'''
This is the script to make mass email delivery
using google mail SMTP server.
Requires google account.
Script reads two files - emails and msgs in its working directory
Then the random text chosen from msgs file (texts are separated with ========)
is sent to each email from emails file.

Please do not use for spaming and other fraudulent purposes.
Licensed as public domain.
'''

import smtplib, getpass, random


def get_email_list(emailfile):
    f = open(emailfile, "r", encoding='utf-8')
    email_lst = []
    for line in f:
        email_lst += [line]
    return email_lst


def get_randomized_msg_list(msgfile, separator):
    f = open(msgfile, "r", encoding='utf-8')
    msg_lst = []
    cur_msg = "".encode('utf-8')
    for line in f:
        if not line.startswith(separator):
            cur_msg += (line).encode('utf-8')
        else:
            msg_lst += [cur_msg]
            cur_msg = "".encode('utf-8')
    return msg_lst


def send_mass_emails_random_pick(smtp_ssl_sender, sendermail,  listemails, listmessages): # smpt_sender should be SSL
    if(not isinstance(smtp_ssl_sender, smtplib.SMTP_SSL)):
        raise Exception("Not an SSL smtp provided!")
    for email in listemails:
        smtp_ssl_sender.sendmail(sendermail, email, random.choice(listmessages))


elst = get_email_list("emails")
mlst = get_randomized_msg_list("msgs", "========")


sender = smtplib.SMTP_SSL(
    'smtp.gmail.com'
)
print("Google automatized mail sending script. Please authorize yourself.")
lo = input("Login: ")
pw = getpass.getpass("Password: ")
sender.login(lo, pw)
send_mass_emails_random_pick(sender, lo+"@gmail.com", elst, mlst)
sender.close()