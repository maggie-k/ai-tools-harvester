from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def scrape_tools():

	try:
		print("\nScraping in progress...")

		with sync_playwright() as p:	
			browser= p.chromium.launch(headless=True)			
			context= browser.new_context()
			page= browser.new_page()

			page.set_default_timeout(90000)
			page.set_default_navigation_timeout(90000)

			print("\nConnecting to website...")
			page.goto("https://aitoolsdirectory.com/")
			
			print("\nWaiting for page to load...")
			page.wait_for_load_state("networkidle")	

			page_num= 1
			max_pages=10

			data= []

			while page_num <= max_pages:

				print(f"\n{'='*50}")
				print(f"\n--- Scraping Page {page_num} ---")
				print(f"\n{'='*50}")
				
				cards= page.query_selector_all(".sv-tile__info")

				skip = (
					'Featured Tool: Artlist',
		    		'Featured Tool: i10x',
		    		'AI Tools Newsletter'
				)

				print("\nExtracting elements...")

				for card in cards:					
					name_el= card.query_selector("h3")
					cat_el= card.query_selector("div.sv-badge.sv-badge__1.sv-badge__1__1.clickable")
					desc_el= card.query_selector(" div p")
					link_el= card.query_selector("a")				

					if link_el:
						href= link_el.get_attribute("href")
						print(f"\nVisiting: {href}")
						
						detail_page= context.new_page()
						detail_page.set_default_timeout(90000)
						detail_page.goto(f"https://aitoolsdirectory.com{href}", timeout=90000, wait_until="domcontentloaded")
						

						try:
							link_el1= detail_page.wait_for_selector("div.sv-product-page__string a", timeout=5000) 
							actual_link= link_el1.get_attribute("href").strip() if link_el1 else "N/A" 							

						except (PlaywrightTimeoutError, TimeoutError):
							print("⚠️ Website link not found on page")
							actual_link= f"https://aitoolsdirectory.com{href}".strip()

						print(f"Actual site link: {actual_link}")
						
						detail_page.close()
						page.wait_for_load_state("networkidle")
						time.sleep(1)


					name_text= name_el.inner_text().strip() if name_el and name_el.inner_text() not in (skip) else "N/A"
					cat_text= cat_el.inner_text().strip() if cat_el else "N/A"
					desc_text= desc_el.inner_text().strip() if desc_el else "N/A"

					print(f" • {name_text}")
					print(f"   {cat_text}")
					print(f"   {desc_text}")
					print(f"   {actual_link}")

					data.append({
						"name": name_text,
						"category": cat_text,
						"description": desc_text,
						"website": actual_link
						})
				
				next_page_num= page_num+1
				next_link= page.query_selector(f'a[href="/?page={next_page_num}"]')

				if next_link and next_link.is_visible():
					print(f"\n-> Moving to page {next_page_num}...")
					next_link.click()
					page.wait_for_load_state("networkidle")
					time.sleep(1)
					page_num+=1
				else:
					print("\nReached the last page!")
					break
			
			df=pd.DataFrame(data) 

			print(df.tail(5))

			print(f"\n{'='*50}")	
			print("\nScraping completed successfully!")
			print(f"Total items collected: {len(data)}")
			print(f"Total pages scraped: {page_num}")			

	except Exception as e:
		print(f"Error: {e}")	
		traceback.print_exc()

	return df


if __name__== "__main__":
	scrape_tools()
	#df= scrape_tools()
	#df.to_csv("scraped_data1.csv", index=False)
	print("\n Work Done!")
