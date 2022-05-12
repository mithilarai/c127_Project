from bs4 import BeautifulSoup 
import time 
import csv
import requests

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(start_url)

time.sleep(10)

def scrape() : 
    headers = {'Name' , 'Distance' , 'Mass' , 'Radius'}
    stars_data = []

  

    soup = BeautifulSoup(page.content , 'html.parser')

    for table_tag in soup.find_all('table' , attrs = {'class' , 'wikitable sortable jquery-tablesorter'}) : 
        for tbody_tag in table_tag.find_all('tbody'):
            for tr_tags in tbody_tag.find_all('tr'):
        
                td_tags = tr_tags.find_all('td')
                temp_list = []
                for index,td_tag in enumerate(td_tags) :
                    if index  == 1 : 
                        temp_list.append(td_tag.find_all('a')[0].contents[0])
                    else:
                        try : 
                            lists = td_tag.contents[0]
                            temp_list.append(lists)
                        except : 
                            temp_list.append('')
                stars_data.append(temp_list)
    print(stars_data)
    
    with open('stars' , 'w') as f :
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(stars_data)

scrape()
