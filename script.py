import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://cust.edu.pk/our_team/'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant elements and extract the URLs
team_members = soup.select('.our-team-item .content-team a')

# Gather the URLs
urls = [member['href'] for member in team_members]

# Scrape details from each URL
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_element = soup.select_one('.title')
    title = title_element.text.strip() if title_element else 'N/A'

    email_element = soup.select_one('.extra-info .email a')
    email = email_element.text.strip() if email_element else 'N/A'

    phone_element = soup.select_one('.extra-info .fa-phone')
    phone = phone_element.next_sibling.strip() if phone_element else 'N/A'

    print(f"Title: {title}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
