import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def fetch_xing_data():
    base_url = "https://www.xing.com/jobs/search?sc_o=losp_jobs_search_button_click&sc_o_PropActionOrigin=losp_job_search&location=germany"

    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--headless=new")  # Optional: run in headless mode

    driver = webdriver.Chrome(options=options)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    jobs = []
    for page in range(1, 4):
        url = f"{base_url}&page={page}"
        # print(f"Scraping page {page}: {url}")  
        driver.get(url)
        time.sleep(10)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_list = soup.select('ol.results-styles__List-sc-e4577d73-0 > li')
        
        for job in job_list:
            try:
                a_tag = job.find('a', {'data-testid': 'job-search-result'})
                if not a_tag:
                    continue

                title = a_tag.find('h2')
                title_text = title.text.strip() if title else 'N/A'
                company = a_tag.find('p', class_='job-teaser-list-item-styles__Company-sc-4c7b5190-7')
                company_name = company.text.strip() if company else 'N/A'
                location = a_tag.find('p', class_='job-teaser-list-item-styles__City-sc-4c7b5190-6')
                location_text = location.text.strip() if location else 'N/A'

                url = a_tag['href']
                if url.startswith('/'):
                    url = f"https://www.xing.com{url}"

                jobs.append({
                    'title': title_text,
                    'company': company_name,
                    'location': location_text,
                    'url': url
                })

            except Exception as e:
                print("Error parsing job:", e)

    driver.quit()
    print(json.dumps(jobs, indent=2, ensure_ascii=False))
    return jobs

fetch_xing_data()
