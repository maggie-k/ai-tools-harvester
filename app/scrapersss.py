import requests
import bs4

from playwright.sync_api import sync_playwright

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


try:
	print("\nScraping in progress...")

	with sync_playwright() as p:	
		browser= p.chromium.launch() 
		# the browser variable, only accessible inside the with block
		
		page= browser.new_page()

		print("\nConnecting to website...")
		page.goto("https://aitoolsdirectory.com/")		

		# waits automatically for selector to appear
		print("\nWaiting for page to load...")
		page.wait_for_load_state("networkidle")

		print("\nExtracting elements...")
		elements= page.query_selector_all("h3")
		print(f"\nFound {len(elements)} elements\n")

		skip = (
			'Featured Tool: Artlist',
    		'Featured Tool: i10x',
    		'AI Tools Newsletter'
		)

		for el in elements:
			text = el.inner_text().strip()
			if any(s in text for s in skip):
				continue
			
			print(text)
		
		print("\nScraping completed successfully!")

		# with block ends here
		# with sync_playwright() context manager auto-closes everything when it exists

except Exception as e:
	print(f"Error: {e}")
	import traceback
	traceback.print_exc()

# status messages

'''
try:

	options= webdriver.ChromeOptions()
	options.add_argument('--headless')	

	# initializes Chrome browser with automanaged ChromeDriver 
	driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
		options=options)	
	print("Driver initialized successfully\n")	

	# navigate to the target website
	print("Navigating to website...\n")	
	driver.get("https://aitoolsdirectory.com/")	
	print("Page loaded\n")
	#print(driver.page_source[:2000])

	# scroll or interact first
	#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# wait-time for JS to load
	time.sleep(5)

	# find all elements with class 'sv-title_info'
	elements= driver.find_elements(By.TAG_NAME, "h3")
	print(f"Found {len(elements)} elements\n")

	# extract and print text from each element
	for el in elements:
		print(el.text)

except Exception as e:
	print(f"Error: {e}")
	import traceback
	traceback.print_exc()

finally:
	if 'driver' in locals():
		driver.quit() # closes browser and cleans up'''

'''
res= requests.get("https://aitoolsdirectory.com/")

print(res)
#print(res.text[:2000])

soup= bs4.BeautifulSoup(res.text, 'lxml')

#print(soup)

result= soup.select('.sv-title__info')

print(result)'''

'''
[result for item in items if condition]
↓
for item in items:
    if condition:
        result.append(...)'''
