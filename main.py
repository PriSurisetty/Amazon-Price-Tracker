from bs4 import BeautifulSoup
import requests
import smtplib
import os


# ------------------------ Getting the price of the product & title ------------------------ #

amazon_link = os.environ.get("LINK")
response = requests.get(amazon_link, headers={
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/127.0.0.0 Safari/537.36"}
    )
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

dollars_element = soup.find(class_="a-price-whole")
cents_element = soup.find(class_="a-price-fraction")

dollars = dollars_element.text.replace('.', '')
cents = cents_element.text

price = float(f"{dollars}.{cents}")

title_element = soup.find(name="title")
title = title_element.text[12:]

# ------------------------ Using SMTP to send a deal alert ------------------------ #

BUYING_PRICE = 160

my_email = os.environ.get("USERNAME")
my_password = os.environ.get("PASSWORD")

if price < BUYING_PRICE:
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Secures connection
            connection.login(user=my_email, password=my_password)
            message = f"Subject:Amazon Price Alert!\n\n{title} is now ${price}!\n{amazon_link}"
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=message.encode('utf-8')  # Encode the message to han`dle special characters
            )
    except Exception as e:
        print(f"An error occurred: {e}")

