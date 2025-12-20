from playwright.sync_api import sync_playwright
import traceback
import time
#import pandas as pd

# crawl through the pages (emoticon/video for social media??)

try:
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)

        context= browser.new_context()
        #page= context.new_page()           
        page= browser.new_page()

        # Setting user-agent to mimic real browser
        #page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"})

        page.goto("https://aitoolsdirectory.com/")

        page.wait_for_load_state("networkidle")
        #time.sleep(5)

        page_num=1
        max_pages=10

        data= []        

        while page_num<= max_pages:
            print(f"\n{'='*50}")
            print(f"\n--- Scraping Page {page_num} ---")
            print(f"\n{'='*50}")

            # grabbing parent container first
                    
            cards= page.query_selector_all(".sv-tile__info")

            for card in cards:
                # finding elements within each card

                name_el= card.query_selector("h3")
                cat_el= card.query_selector("div.sv-badge.sv-badge__1.sv-badge__1__1.clickable")
                desc_el= card.query_selector("div p")
                link_el= card.query_selector("a")

                #name_text= name_el.inner_text() if name_el else "N/A"
                #cat_text= cat_el.inner_text() if cat_el else "N/A"
                #desc_text= desc_el.inner_text() if desc_el else "N/A"

                if link_el:
                    href= link_el.get_attribute("href")
                    print(f"\nVisiting: {href}")

                    # opens new page/tab
                    detail_page= context.new_page()
                    detail_page.goto(f"https://aitoolsdirectory.com{href}")
                    detail_page.wait_for_load_state("networkidle")

                    # scrapes the detail page
                    link_el1= detail_page.query_selector("div.sv-product-page__string a")
                    actual_link= link_el1.get_attribute("href") if link_el1 else "N/A"

                    print(f"Actual site link: {actual_link}")

                    # closes detail page and continues
                    detail_page.close()

                    page.wait_for_load_state("networkidle")
                    time.sleep(3)


                #name_el= card.query_selector("h3")
                #cat_el= card.query_selector("div.sv-badge.sv-badge__1.sv-badge__1__1.clickable")
                #desc_el= card.query_selector("div p")
                

                name_text= name_el.inner_text() if name_el else "N/A"
                cat_text= cat_el.inner_text() if cat_el else "N/A"
                desc_text= desc_el.inner_text() if desc_el else "N/A"
                              


                print(f"• {name_text}")
                print(f"  {cat_text}")
                print(f"  {desc_text}")
                print(f"  {actual_link}")

                data.append({"name": name_text,
                    "category": cat_text,
                    "description": desc_text,
                    "link": actual_link
                    })

            
            next_page_num= page_num +1
            next_link= page.query_selector(f'a[href="/?page={next_page_num}"]')     
            

            if next_link and next_link.is_visible():
                print(f"\n-> Moving to page {next_page_num}...")
                next_link.click()
                page.wait_for_load_state("networkidle")
                time.sleep(3)
                page_num+=1
            else:
                print("\nNo more pages found")
                break

        print(f"\n{'='*50}")
        print(f"Scraping Complete!")
        print(f"Total items collected: {len(data)}")
        print(f"Total pages scraped: {page_num}")    

except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

# how to deal with Error: Timeout 30000ms exceeded
# store in df then go to reminder logic with fuzzy. push tonight!!!!
#df= pandas.DataFrame()
