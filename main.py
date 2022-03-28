
from operator import index
from turtle import title
import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np
from datetime import date

import os
from pathlib import Path
import time

from scrapper import scraping
from save_scraped import save_new_scraped_data





# create key functions

def scraped_elements(ur, clas):
    """This function uses scripper model to gerate a list of webpage contents

    Args:
        ur (String): This is the url of the website being scraped
        clas (String): This is the tag class where the items being scarpped are located

    Returns:
        list: The returned item is a list of elements in the tag defined by the class (clas)
    """

    scrapped = scraping(ur)
    items = scrapped.find_all(class_=str(clas))
    items_all = [item for item in items]   

    return items_all

def main_func(pages_to_scrape):
    
    #Loop through pages whiles scraping each page
    for page_num in range(1, pages_to_scrape+1): 
        url = f'https://www.masterstudies.com/Technology-Studies/?page={page_num}'
        cls = 'program-listitem relative'
        IT_masters_programs = scraped_elements(url, cls)

        #Pick the required items from the scraped page and append to the dictionary above "program_list"
        for itemm in IT_masters_programs:
            for key, clss in (zip(list(program_list.keys()), div_clas)):
                tag='div'
                if key=='Read_More':
                    tag='a'
                filter_scraped(itemm, key, tag, clss)

def filter_scraped(itemm, dict_key, tag, clas):
    if itemm.find(tag, class_=clas) == None:
                program_list[dict_key].append('None')
    else:
        if tag == 'a':
            program_list[dict_key].append(itemm.find(tag, class_=clas)['href'])
        else:
            program_list[dict_key].append(itemm.find(tag, class_=clas).text.strip())

    

if __name__ == '__main__':

    # Initialize key variable
    div_clas = ['program_title', 'school', 'locations', 'description', 'languages', \
        'degree', 'based', 'show-for-medium', 'application', 'start', 'duration']

    program_list = {
        'Title':[],
        'School':[],
        'Location':[],
        'Descripion':[],
        'Language':[],
        'Type':[],
        'Style':[],
        'Read_More':[],
        'Deadline':[],
        'Start':[],
        'Duration':[],
    }
    
    # start_time = time.time()

    num_of_pages = 154
    
    main_func(num_of_pages)
  
    #   Create pandas pd.DataFrame
    df = pd.DataFrame.from_dict(program_list)

    # save Resutls
    base_path = os.path.dirname(os.path.abspath(__file__)) 
    # Source path where we want to save the scraped data
    source_path =  f"{base_path}/sp_data/scraped_at={str(date.today())}/MSC-IT.csv" #{str(date.today())}
    
    save_new_scraped_data(source_path, df)

    end_time = time.time()
    # print(end_time-start_time)