import requests
from bs4 import BeautifulSoup
import smtplib
import time

# website url to monitor
url = 'https://matinf.pmf.unibl.org/%d0%bd%d0%be%d0%b2%d0%be%d1%81%d1%82%d0%b8/'

# recipients' email addresses
recipients_emails = ['katarina.despotovic@student.pmf.unibl.org']

# email credentials
email = 'sajt.novosti.faks@gmail.com' # TREBA DOZVOLITI MANJE SIGURNE APLIKACIJE NA GMAILU
password = 'niundarhttgesrxh'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# element to monitor
element_to_monitor_id = 'category-posts-3-internal'

"""
# send first email
subject = 'Mat i inf (novosti)'
message = "servis is up" # naslov u subject a link u body
body = f'Subject: {subject}\n\n{message}'
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email, password)
    for recipient in recipients_emails:
        server.sendmail(email, recipient, body)
"""
        
# read previous website content from file
with open("current_content.txt", 'r', encoding='utf-8') as f:
    previous_content = f.read()
"""
while True:
"""
# get current website content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
li_elements = soup.find('ul', id=element_to_monitor_id).find_all('li') # izvuci i linkove
current_content = [li.text for li in li_elements]

# check for changes
if str(current_content) != previous_content:

    with open("current_content.txt", 'w', encoding='utf-8') as f:
        f.write(str(current_content))


    # send email to recipients
    subject = 'Mat i inf (novosti)'
    message = str(current_content) # naslov u subject a link u body
    body = f'Subject: {subject}\n\n{message}'
    body = body.encode('utf-8')
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email, password)
        for recipient in recipients_emails:
            server.sendmail(email, recipient, body)
"""
    # wait for a certain time before checking again
    time.sleep(60)
"""
