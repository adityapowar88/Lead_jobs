
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup



def fetch_stepstone_data():
    base_url = "https://www.stepstone.de/work/in-germany?radius=30&searchOrigin=Resultlist_top-search"
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0")
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(options=options)
    
    
    jobs = []
    for page in range(1, 2): 
        url = base_url + str(page)
        driver.get(url)
        time.sleep(8)  

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_articles = soup.select('article[data-at="job-item"]')
        
        for job in job_articles:
            try:
                title_elem = job.select_one('a[data-at="job-item-title"]')
                title = title_elem.text.strip() if title_elem else "N/A"
                url = title_elem['href'] if title_elem and title_elem.has_attr('href') else "N/A"

                company_elem = job.select_one('[data-at="job-item-company-name"], div[class*="company"]')
                company = company_elem.text.strip() if company_elem else "N/A"

                jobs.append({
                    "title": title,
                    "company": company,
                    "url": url
                })

            except Exception as e:
                print(f"Skipped job due to error: {e}")

    driver.quit()    
    return jobs

