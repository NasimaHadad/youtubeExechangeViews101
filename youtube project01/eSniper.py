"""
########################################################
# Program Algorithm :

1 - import what needed to work work
2 - code the core process
    --- Search, Scrape & Save

########################################################
"""

# Program Resources :
import Sys30
from configparser import ConfigParser
from selenium import webdriver
import time
import re
from termcolor import colored

"""
###################
# Program Defines #
###################
"""

# Create a keywords list from keywords text file
def keywords_list_from_file():
    with open('Keywords.txt', 'r') as keywords_file:
        raw_keywords_list = keywords_file.readlines()
        keywords_list = []
        for keyword in raw_keywords_list:
            keywords_list.append(keyword.replace("\n", ""))
    return keywords_list

# Set user input from config.ini / set variables
def get_user_inputs():
    print("[*] Get config")
    config_file = "config.ini"
    config = ConfigParser()
    config.read(config_file)
    print("[*] Get keywords list")
    keywords_list = keywords_list_from_file()
    esp = config["user_data"]["esp"]
    area = config["user_data"]["area"]
    return keywords_list, esp, area

# Search, Scrape & Save
def search_scrape_save():
    print("[*] Launch eSniper campaign")
    # Set emails counter
    emails_count = 0

    for keyword in keywords_list:
        print("\n[~] Targeting " + keyword + " in " + area )
        print("\t\t\t⟲ Process Extraction\n")
        # Set search formula
        search_formula = '"' + keyword + '"+' + '"@' + esp + '"+' + '"' + area + '"'
        # Navigate to bing.com
        driver.get("http://www.bing.com")
        time.sleep(7)

        # type the search phrase
        s_form = driver.find_element_by_xpath("//input[@id='sb_form_q']")
        s_form.send_keys(search_formula)
        time.sleep(5)

        # Click search button
        s_button = driver.find_element_by_xpath("//body/div[1]/div[1]/div[3]/div[2]/form[1]/label[1]/*[1]")
        s_button.click()
        time.sleep(7)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        next_button = driver.find_elements_by_xpath("//a[@title='Next page']")
        time.sleep(3)

        # The next page loop
        while next_button:
            # The start of scrape, save & go to the next page loop
            # Get page text
            page_text = driver.find_element_by_tag_name("body").text
            page_text = page_text.lower()

            # Extract Emails From HTML
            email_regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
            extracted_emails = re.findall(email_regex, page_text)

            for email in extracted_emails:
                # if email is not in the Data_emails.txt then add it
                with open("Data_emails.txt", "r") as file:
                    if email not in file.read():
                        # if email contain less than or two dots
                        dots_count = email.count('.')
                        if dots_count <= 2:
                            # if the email contain "esp"
                            if esp in email:
                                with open('Data_emails.txt', 'a') as file:
                                    file.write(email + "\n")
                                    emails_count += 1
                                    print("\t Process " + str(emails_count) + " Extracted: " + colored(email, 'red') + "\n\t\t\t↳ Micro-niche: " + keyword + " Geo-target: " + area )
            time.sleep(7)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # Click next if Next Pege Button exist
            next_button = driver.find_elements_by_xpath("//a[@title='Next page']")
            if next_button:
                next_button[0].click()

            else:
                break
    # Close browser
    driver.quit()

"""
#################
# Program Flow #
################
"""
# Check user-id
Sys30.sys30()

# Get keywords list from keywords file
keywords_list = keywords_list_from_file()


# Get user inputs
keywords_list, esp, area = get_user_inputs()

# Launch webdriver
driver = webdriver.Chrome()
time.sleep(7)

# Search, Scrape & Save
search_scrape_save()

# Mission Complete
print("\nMission Complete !!")


"""
#################
# Program Raw #
################
"""