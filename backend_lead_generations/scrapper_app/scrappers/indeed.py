
import json
from selenium import webdriver
import time

url = "https://in.indeed.com/l-bengaluru,-karnataka-jobs.html?vjk=8ed460d70b61cb07"


def fetch_jobs_data():
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0")
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(options=options)
    
    # First visit to set domain
    driver.get("https://in.indeed.com")
    
    # Set all cookies from your manual session
    cookies = [
        {'name': 'indeed_rcc', 'value': 'CTK'},
        {'name': 'CTK', 'value': '1hkfvm1thgpe59m4'},
        {'name': 'RF', 'value': 'TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtTbVG6_PXz1bK5jTfcrhazY='},
        {'name': '_cfuvid', 'value': 'YdgPvC39if6QOqRQkbMBckS8n3ZXAlPQhKtdWZ.csh4-1749020839939-0.0.1.1-604800000'},
        {'name': 'cf_clearance', 'value': '3hnx6QT7O2G3Q8fzgXPiZFe8e9cD6SxUdDj8ke2LECI-1749020838-1.2.1.1-P1nDvEayV9kMnzblKOFfl0pl4KVeMYPeHajuus69J_T0n07iCTohCjJJ.ozt5rviokWlvn.wF2fIlYd83wCAxnSJOi_D.r7QhdM5jlzZNiN.MWjEr7RZFrWKtVW_eb9OSxN2uXIpnRhp7U4kP07kdp4LcAUxdeDYMgCfL8T1PgWLrWaGOX1DOArI46jOoJsZhSsXm4tYBuuZFaExSVibVsOnnrv7TO8D8ZtCT2YFpj0XGzRaYzk1IS0GvJnakzNk3vogm80QK7Pg9SO8Rj1C_melDxKEuXSfkBkV02OQmnvI7NVneGCpTKhkBBePgTlPiLsHBWm54gUgZdbHgUb7v5x_8bMs23ZkND3X_T_unGUGfbm8wibgX8n_8Y3k9aQM'},
        {'name': 'LC', 'value': 'co=IN'},
        {'name': 'LOCALE', 'value': 'en_IN'},
        {'name': 'MICRO_CONTENT_CSRF_TOKEN', 'value': 'BEXVi3kKcZeXL0ueR6ldL9fgzPHvZmat'},
        {'name': 'PPID', 'value': ''},
        {'name': 'g_state', 'value': '{"i_p":1748933980844,"i_l":1}'},
        {'name': '__cf_bm', 'value': 'xkC8SY7m4idPPMEeTRkGopwr8j44BMHHyNowixpyZG8-1749019997-1.0.1.1-c.QRoeKvpWj9KmKxMALRKSU2PYFzIr7Ux6blyqBs3Gl2_9jpf0URsHc7yyfCJcBcdXJgXqfEt7COih7.i94xJjHCHK1IcAQHeZYOcJiWBp8'}
    ]
    
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Couldn't add cookie {cookie['name']}: {e}")
    
    # Now visit your target URL with cookies
    driver.get(url)
    time.sleep(5)  # Allow page to load
    
    # Your scraping code here
    
    driver.quit()
    
    
# # fetch_jobs_data()
# from playwright.sync_api import sync_playwright
# import random
# import time

# def playwright_bypass():
#     with sync_playwright() as p:
#         # Use real Chrome instead of Chromium
#         browser = p.chromium.launch(
#             channel="chrome",
#             headless=False,
#             args=[
#                 '--disable-blink-features=AutomationControlled',
#                 f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 115)}.0.0.0 Safari/537.36'
#             ]
#         )
        
#         context = browser.new_context(
#             viewport={'width': 1920, 'height': 1080},
#             locale='en-US'
#         )
        
#         # Correct cookie format with domain and path
#         cookies = [
#             {
#                 'name': 'indeed_rcc',
#                 'value': 'CTK',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'CTK',
#                 'value': '1hkfvm1thgpe59m4',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'RF',
#                 'value': 'TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtTbVG6_PXz1bK5jTfcrhazY=',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': '_cfuvid',
#                 'value': 'YdgPvC39if6QOqRQkbMBckS8n3ZXAlPQhKtdWZ.csh4-1749020839939-0.0.1.1-604800000',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'cf_clearance',
#                 'value': '3hnx6QT7O2G3Q8fzgXPiZFe8e9cD6SxUdDj8ke2LECI-1749020838-1.2.1.1-P1nDvEayV9kMnzblKOFfl0pl4KVeMYPeHajuus69J_T0n07iCTohCjJJ.ozt5rviokWlvn.wF2fIlYd83wCAxnSJOi_D.r7QhdM5jlzZNiN.MWjEr7RZFrWKtVW_eb9OSxN2uXIpnRhp7U4kP07kdp4LcAUxdeDYMgCfL8T1PgWLrWaGOX1DOArI46jOoJsZhSsXm4tYBuuZFaExSVibVsOnnrv7TO8D8ZtCT2YFpj0XGzRaYzk1IS0GvJnakzNk3vogm80QK7Pg9SO8Rj1C_melDxKEuXSfkBkV02OQmnvI7NVneGCpTKhkBBePgTlPiLsHBWm54gUgZdbHgUb7v5x_8bMs23ZkND3X_T_unGUGfbm8wibgX8n_8Y3k9aQM',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'LC',
#                 'value': 'co=IN',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'LOCALE',
#                 'value': 'en_IN',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'MICRO_CONTENT_CSRF_TOKEN',
#                 'value': 'BEXVi3kKcZeXL0ueR6ldL9fgzPHvZmat',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'PPID',
#                 'value': '',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': 'g_state',
#                 'value': '{"i_p":1748933980844,"i_l":1}',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             },
#             {
#                 'name': '__cf_bm',
#                 'value': 'xkC8SY7m4idPPMEeTRkGopwr8j44BMHHyNowixpyZG8-1749019997-1.0.1.1-c.QRoeKvpWj9KmKxMALRKSU2PYFzIr7Ux6blyqBs3Gl2_9jpf0URsHc7yyfCJcBcdXJgXqfEt7COih7.i94xJjHCHK1IcAQHeZYOcJiWBp8',
#                 'domain': '.indeed.com',
#                 'path': '/'
#             }
#         ]
        
#         context.add_cookies(cookies)
        
#         page = context.new_page()
#         page.goto(url, timeout=60000)
#         time.sleep(5)
        
#         if "Verification" in page.title():
#             # Try solving automatically
#             try:
#                 page.frame_locator('iframe[title*="challenge"]').get_by_role("checkbox").click()
#                 time.sleep(2)
#             except:
#                 print("Manual CAPTCHA solution required")
#                 input("Press Enter after solving...")
        
#         print(page.content())
#         browser.close()
# playwright_bypass()



