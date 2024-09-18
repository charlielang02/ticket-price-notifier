import requests
from bs4 import BeautifulSoup
import smtplib
from db import store_price_history, get_all_users

def get_ticket_prices(artist_name):
    url = f"https://example.com/search?q={artist_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tickets = []
    for ticket in soup.find_all('div', class_='ticket-info'):
        price = ticket.find('span', class_='price').text
        section = ticket.find('span', class_='section').text
        if 'pit' in section.lower():
            tickets.append({'price': price, 'section': section})
    return tickets

def send_notification(email, artist, ticket_info):
    msg = f"Pit tickets for {artist} are now {ticket_info['price']}."
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email@gmail.com', 'your-password')
        server.sendmail('your-email@gmail.com', email, msg)

def check_prices():
    users = get_all_users()
    for user in users:
        email, artist = user
        current_prices = get_ticket_prices(artist)
        for ticket in current_prices:
            send_notification(email, artist, ticket)
            store_price_history(artist, ticket['price'], ticket['section'])
