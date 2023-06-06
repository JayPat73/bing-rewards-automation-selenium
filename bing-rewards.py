from random import randint
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Initialize browser & set constants
browser = webdriver.Edge()
RAND_WORD_URL = "https://random-word-api.herokuapp.com/word"

def bot():
    browser.get('https://www.bing.com')
    # search 40 terms, 30 needed to max out points for Level 2 rewards, extra for redundancy
    for _ in range(40):
        # Attempt to retrieve a word and search it up to 3 times before erroring out.
        attempts = 0
        while attempts < 3:
            try:
                browser.set_page_load_timeout(5000)
                assert 'Bing' in browser.title

                # Get our random term
                random_term = requests.get(RAND_WORD_URL).text.split('"')[1]
                print(str(_) + ' ' + random_term)

                # Find, Clear, and Search the term in the search box
                sleep(randint(2,4))
                search_box = browser.find_element(by='id',value='sb_form_q')
                sleep(randint(2,4))
                search_box.clear()
                sleep(randint(2,4))
                search_box.send_keys(random_term+" "+ Keys.RETURN)

                # Bring us back to the home page
                sleep(randint(2,4))
                browser.back()

                # Exit the attempts loop without triggering an error
                attempts = 4
                continue
            except Exception as e:
                # Log exception, increade attempt count, bring us back to the home page
                print(e)
                attempts += 1
                sleep(randint(2,4))
                browser.get('https://www.bing.com')
                sleep(randint(2,4))
        if attempts == 3:
            print('Max attempts reached, ending script')
            break
        

if __name__ == "__main__":
    # Log our times, should take around 7-10 minutes for 40 requests
    st = datetime.now()
    print('START TIME: ' + str(st))
    bot()
    browser.quit()
    print('END TIME:   ' + str(datetime.now()))
    print('TOTAL TIME: ' + str(datetime.now() - st))
