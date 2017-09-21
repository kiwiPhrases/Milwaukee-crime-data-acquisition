#import requests
#import os, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
###############################################################################
############################### parameters ####################################
## parameters
base_url = "http://itmdapps.milwaukee.gov/publicApplication_QD/queryDownload/login.faces"
census_tab = "http://itmdapps.milwaukee.gov/publicApplication_QD/queryDownload/censusTractfm.faces"
#user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


############################### open and fill ###############################
def initialize(base_url, census_tab):
    """
    INPUT:
        1. base_url - url of the login page and subsequent query page
        2. census_tab - url of the tab from which you wish to download data
            ...in my case, this was the census_tract tab
    OUTPUT:
        1. driver - connection to the browser driver on the specified page
    DESCRIPTION:
        [initialize] a) opens Firefox, b) goes to login page(you manually login in browser)
        c) navigates to desired tab d) here you fill out the query form
    """
    print("\n...Initiating browser")
    driver=webdriver.Firefox()
    driver.get(base_url)
    print("\nUser input in the browser is required: login")
    input("\nTo proceed, hit [Enter]")

    # enter census tract tab:
    driver.get(census_tab)
    print("\nPlease fill out the query form")
    print("Need: dates, format")
    input("\nTo proceed, hit [Enter]")
    
    return(driver)

########################### find census tracts ###############################
def find_option_set(driver):
    """
    INPUT:
        1. driver - Firefox driver passed from [initialize]
    OUTPUT:
        1. Select - Selenium class for selecting options
    DESCRIPTION:
        [find_option_set] takes the driver from [initialize], uses
        its page source to find the available options (in my case the census tracts)
        and returns a list of options as well as a class to select the options
    
    """
    source = driver.page_source
    soup = BeautifulSoup(source)
    rows = soup.findAll("option")#, {'class': ['odd', 'even']})
    census_tracts = []
    for row in rows[1:]:
      census_tracts.append(row.getText())

    select = Select(driver.find_element_by_id("formQuery:menuCenId"))
    
    return([census_tracts, select])

############################# download data ##################################
def download_data(driver, census_tracts, select):
    """
    INPUT:
        1. driver - from [initialize]
        2. census_tracts - set of options from [find_option_set]
        3. select - select class from [find_option_set]
    OUTPUT:
        1. downloaded files in the browser-specified download directory
    DESCRIPTION:
        [download_data] simply iterates over the options list by "clicking"
        on each option and submitting the query form. There is a throttle
        built into the loop just in case.
    """
    submit_button = driver.find_element_by_id("formQuery:buttonQueryId")
    print("Downloading data...")
    
    for tract in census_tracts:
        select.select_by_visible_text(tract)
        submit_button.send_keys(Keys.ENTER)
        time.sleep(2)
        
############################# main function ###################################
def main():
    base_url = "http://itmdapps.milwaukee.gov/publicApplication_QD/queryDownload/login.faces"
    census_tab = "http://itmdapps.milwaukee.gov/publicApplication_QD/queryDownload/censusTractfm.faces"

    driver = initialize(base_url, census_tab)
    census_tracts, select = find_option_set(driver)
    download_data(driver, census_tracts, select)
    
if "__main__"==__name__:
    main()    