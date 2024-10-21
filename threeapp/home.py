#from django.core.mail import send_mail

#send_mail(
 #   "Subject here",
 #   "Here is the message.",
 #   "jeevagan077@gmail.com",
#    ["jeevagan077@gmail.com"],
  #  fail_silently=False,
#)

import sendgrid
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient(api_key='E2F810258B3053B5FE5590BE185418DD4A81D75E5193A83410DA7F29678008691AC49D36DE57B02DEA523BB1822449F2')
from_email = 'jeevagan077@gmail.com'
to_email = 'thestupid077@gmail.com'
subject = 'Subject here'
content = 'Here is the message.'

message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject=subject,
    plain_text_content=content
)

response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)