from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#Linkedin Application Credentials
CLIENT_ID = '86i3d1h6g61i6a'
CLIENT_SECRET = 'QDkZNMIuaLCEnejJ'  
# URL of the job search page 
url = 'https://www.linkedin.com/jobs/search/?currentJobId=3477085336&geoId=103644278&keywords=softwareengineer&location=United%20States&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true'

driver = webdriver.Chrome()
driver.get(url)
for i in range(20):  # Range can be altered according to the number of listing needed.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to be loaded

html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
job_listings = soup.find_all('div', {'class': 'job-search-card'}, {'class': 'base-search-card'})
data = {'Title': [], 'Company': [], 'Location': [], 'Job Link': []}
for job in job_listings:
    title = job.find('h3', {'class': 'base-search-card__title'}).text.strip()
    company = job.find('a', {'class': 'hidden-nested-link'}).text.strip()
    location = job.find('span', {'class': 'job-search-card__location'}).text.strip()
    anchor_tag = job.find('a', class_='base-card__full-link')
    href_link = anchor_tag['href']
    
    data['Title'].append(title)
    data['Company'].append(company)
    data['Location'].append(location)
    data['Job Link'].append(href_link)
   
job_df = pd.DataFrame(data)
print(job_df)
job_df.to_excel('/Users/Desktop/Spring 2024/job_listings1.xlsx', index=False)
#job_df.to_excel('job_devlist.xlsx', index=False)
print("Job listings exported to Excel successfully.")
