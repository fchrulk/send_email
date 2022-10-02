# Send Email from Gmail via Python
- Multiple recipients
- Add attachments if needed
## Installation
- cd to your working directory<br>
`cd my-working-directory && git clone https://github.com/fchrulk/send_email.git`
- cd to your working directory

### General
```
from send_email import send_email

sender = 'sender@gmail.com'
sender_pass = 'password'
recipients = ['recipient1@gmail.com', 'recipient2@gmail.com']
subject = 'Test Email via Python by fchrulk'
content = \ 
"""
This email is sent automatically using Python 3.9

Thank you.
"""

send_email(sender, 
           sender_pass, 
           recipients, 
           subject, 
           content)
```
Output:<br>
`Email sent to recipient1@gmail.com, recipient2@gmail.com!`

### With Attacments
```
from send_email import send_email

sender = 'sender@gmail.com'
sender_pass = 'password'
recipients = ['recipient@gmail.com']
subject = 'Test Email with Attachments via Python by fchrulk'
content = \ 
"""
This email is sent automatically using Python 3.9

Thank you.
"""
attachments = ['filename_1.pdf', 'filename_2.xlsx']

send_email(sender, 
           sender_pass, 
           recipients, 
           subject, 
           content, 
           attachments)
```
Output:<br>
`Email sent to recipient@gmail.com!`