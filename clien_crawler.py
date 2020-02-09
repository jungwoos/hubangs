import os 
from urllib.parse import urlparse 

import requests 
from bs4 import BeautifulSoup 

def fetch_clien_latest_data(): 
    result = [] 
    url = 'https://www.clien.net/service/search?q=%ED%9B%84%EB%B0%A9&sort=recency&boardCd=park&isBoard=true'
    response = requests.get(url) 
    html = response.text 
    soup = BeautifulSoup(html, 'html.parser') 
    
    web_page_link_root = "https://clien.net" 
    list_items = soup.find_all("div", "list_item symph_row jirum") 

    for item in list_items: 
        # title 
        title = item.find("a", "subject_fixed")["title"] 
        
        # link 
        page_link_raw = web_page_link_root + item.find("div", "list_title").find("a")["href"] 
        page_link_parts = urlparse(page_link_raw) 
        normalized_page_link = page_link_parts.scheme + '://' + page_link_parts.hostname + page_link_parts.path 
        # specific id 
        specific_id = page_link_parts.path.split('/')[-1] 
        item_obj = { 
            'title': title, 
            'link': normalized_page_link, 'specific_id': specific_id, 
        } 
        
        print(title) 
        result.append(item_obj) 

    return result


if __name__ == '__main__': 
    fetch_clien_latest_data()
