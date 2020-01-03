import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'http://amazon.in/Apple-iPhone-11-64GB-Purple/dp/B07XVL4P83?ref_=ast_sto_dp&th=1&psc=1%3F'

headers = {
    "USER AGENT":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
price = []
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    try:
        title = soup.find(id="productTitle").get_text()
    except AttributeError:
        print("Product Title")

    try:
        price = soup.find(id="priceblock_ourprice").get_text()
    except AttributeError:
        print("Priceblock Ourprice")

    stripped_price = price.strip("₹ ,")
    replaced_price = stripped_price.replace(",","")
    find_dot = replaced_price.find(".")
    to_convert_price = replaced_price[0:find_dot]
    converted_price = int(to_convert_price)

    print(converted_price)

    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dravyagohil@gmail.com', 'mkslnmkbaaigcjdy') #insert your email and password

    subject = 'Price fell down'
    body = 'Check the amazon link http://amazon.in/Apple-iPhone-11-64GB-Purple/dp/B07XVL4P83?ref_=ast_sto_dp&th=1&psc=1%3F'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'dravyagohil@gmail.com',            #sender email
        'dravyagohil@gmail.com',            #receiver email
        msg
    )
    print('Hey Email has Been Sent')

    server.quit()

check_price()