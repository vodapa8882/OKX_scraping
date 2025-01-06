import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import os
import json
import time
from tqdm import tqdm
from scraper.fetch_article_content import fetch_article_content

def scrape_announcements(start_date, end_date, folder):

    base_url = "https://www.okx.com"
    url = f"{base_url}/help/section/announcements-latest-announcements"
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    # return a datetime corresponding to date input, parsed according to format
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    announcements_list = []
    page = 1
    has_more_pages = True

    while has_more_pages:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print(f"Request timed out for page {page}. Skipping...")
            break
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break

        # parse HTML
        soup = BeautifulSoup(response.text, "html.parser")
        announcements = soup.find_all('li', class_='index_articleItem__d-8iK')

        script_tag = soup.find("script", {"data-id": "__app_data_for_ssr__"})
        if not script_tag:
            print("Error: JSON script tag not found!")
    
        # parse the JSON data to get publish time (in CST)
        try:
            json_data = json.loads(script_tag.string)
            articles = json_data["appContext"]["initialProps"]["sectionData"]["articleList"]["items"]
            publish_times = [(article["title"], article["publishTime"]) for article in articles]
        except Exception as e:
            print(f"Error parsing JSON data: {e}")

        print(f"Processing page {page}")
        # process each announcement for output
        for announcement in tqdm(announcements):
            # convert date to UTC
            cur_index = announcements.index(announcement)
            publish_time = publish_times[cur_index][1]
            cst_time = datetime.fromisoformat(publish_time)
            utc_time = cst_time.astimezone(timezone.utc)
            adjusted_date = utc_time.date()
            
            title = announcement.find('div', class_='index_title__iTmos').text.strip()
            link = announcement.find('a', class_='index_articleLink__Z6ycB')['href']

            # check if the announcement date between input dates
            if start_date.date() <= adjusted_date <= end_date.date():
                full_link = f"{base_url}{link}"
                content = fetch_article_content(full_link, headers)
                announcements_list.append({
                    "title": title,
                    "publish date": adjusted_date.isoformat(),
                    "link": full_link,
                    "content": content 
                })
        
        # check for the next page
        if start_date.date() <= adjusted_date:
            pagination = soup.find('a', class_='okui-pagination-next')
            if pagination:
                next_page_url = pagination['href']
                url = f"{base_url}{next_page_url}"
                page += 1
                time.sleep(0.5)
            else:
                has_more_pages = False
        else:
                has_more_pages = False

    # save results to the specified folder
    os.makedirs(folder, exist_ok=True)
    output_file = os.path.join(folder, 
        f"news_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.json")
    if os.path.exists(output_file):
        count = 1
        while os.path.exists(output_file):
            output_file = os.path.join(folder, 
                f"news_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}_{count}.json")
            count += 1
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(announcements_list, f, indent=4)
        