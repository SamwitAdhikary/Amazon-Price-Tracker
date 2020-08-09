import requests
import smtplib
from bs4 import BeautifulSoup


URL = 'https://www.amazon.in/American-Tourister-AMT-SCH-02/dp/B07CJCGM1M/ref=sr_1_1?crid=1N9Q8H3L4BTWF&dchild=1&keywords=american+tourister+backpacks&qid=1596970107&sprefix=ame%2Caps%2C609&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers= headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[2:5])

    if(converted_price < 700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('youremail@gmail.com', 'YourPassword')

    subject = 'Price fell down!!'

    body = 'Check the amazon link https://www.amazon.in/American-Tourister-AMT-SCH-02/dp/B07CJCGM1M/ref=sr_1_1?crid=1N9Q8H3L4BTWF&dchild=1&keywords=american+tourister+backpacks&qid=1596970107&sprefix=ame%2Caps%2C609&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'FromEmail@gmail.com',
        'ToEmail@gmail.com',
        msg
    )

    print('EMAIL HAS BEEN SENT')

    server.quit()

check_price()