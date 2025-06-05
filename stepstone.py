# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def fetch_stepstone_data():
#     url = "https://www.stepstone.de/work/full-time/backend-developer/in-germany?radius=30&searchOrigin=Homepage_top-search&whereType=autosuggest"

#     options = webdriver.ChromeOptions()
#     options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0")
#     options.add_argument('--disable-blink-features=AutomationControlled')

#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     time.sleep(10)

#     jobs = []

#     try:
#         job_articles = driver.find_elements(By.CSS_SELECTOR, 'article[data-at="job-item"]')

#         for job in job_articles:
#             try:
#                 title_elem = job.find_element(By.CSS_SELECTOR, 'a[data-at="job-item-title"]')
#                 title = title_elem.text.strip()
#                 url = title_elem.get_attribute("href")

#                 company = "N/A"
#                 company_elems = job.find_elements(By.CSS_SELECTOR, '[data-at="job-item-company-name"], div[class*="company"]')
#                 if company_elems:
#                     company = company_elems[0].text.strip()

#                 jobs.append({
#                     "title": title,
#                     "company": company,
#                     "url": url
#                 })

#             except Exception as e:
#                 print("Skipped one job due to error:", e)

#     except Exception as e:
#         print("Error while scraping:", e)

#     driver.quit()

#     print(json.dumps(jobs, indent=2, ensure_ascii=False))
#     return jobs

# fetch_stepstone_data()


import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def fetch_stepstone_data():
    url = "https://www.stepstone.de/work/in-germany?radius=30&searchOrigin=Resultlist_top-search"
    
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0")
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(10)  

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    jobs = []

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
            print("Skipped one job due to error:", e)

    driver.quit()
    print(json.dumps(jobs, indent=2, ensure_ascii=False))
    return jobs

fetch_stepstone_data()
