import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#target site for parsing, requests

url = 'https://pythonjobs.github.io/'
site = requests.get(url)

soup = BeautifulSoup(site.content, 'lxml')
results = soup.find(id='container')

job_elements = results.find_all('section', class_='job_list')

for job_element in job_elements:
    job_titles = job_element.find_all('h1', string=lambda text:'python' in text.lower())
    job_location = job_element.find_all('span', class_='info')[0]
    job_date = job_element.find_all('span', class_='info')[1]
    job_company = job_element.find_all('span', class_='info')[3]
    
    job_more = job_element.find('a', class_='go_button')
    job_more_url = urljoin(url, job_more['href']) if job_more else ''
    
    for job_title in job_titles:
        print(job_title.text.strip())
        print(job_location.text.strip())
        print(f'Start date: {job_date.text.strip()}')
        print(job_company.text.strip())
        print(job_more_url)
        if job_more_url:
            job_link = requests.get(job_more_url)
            job_soup = BeautifulSoup(job_link.content, 'lxml')
            job_contacts = job_soup.find_all('div', class_='contact')
            for job_contact in job_contacts:
                job_contact_details = job_contact.find_all('div', class_='field')
                for field in job_contact_details:
                    print(field.text.strip())

        print()