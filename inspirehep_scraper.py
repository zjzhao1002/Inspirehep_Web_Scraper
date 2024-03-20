from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import pandas as pd

def inspirehep_scraper():

    url = "https://inspirehep.net/authors/1622480" # my inspirehep author page

    options = Options()
    options.add_argument("--headless=new")

    service = webdriver.ChromeService(executable_path="<path to chrome webdriver>")

    browser = webdriver.Chrome(options=options, service=service)
    browser.get(url)

    WebDriverWait(driver=browser, timeout=60).until(visibility_of_element_located((By.CLASS_NAME, "flex-grow-1")))

    page = browser.page_source

    browser.close()

    soup = BeautifulSoup(page, "html.parser")

    # get titles of publications
    all_titles = soup.find_all(attrs={'class':'flex-grow-1'})
    titles = [title.get_text() for title in all_titles ]

    # get arXiv numbers
    all_eprints = soup.find_all('a', attrs={'target':'_blank'})
    eprints = []
    for eprint in all_eprints:
        text = eprint.get_text()
        if any(char.isdigit() for char in text):
            eprints.append(text)

    eprints.insert(-2, '') # give an empty arXiv number to my thesis

    # get citations
    all_citations = soup.find_all('span', attrs={'class':'v-top'})
    citations = []
    for citation in all_citations:
        text = citation.get_text()
        if any(char.isdigit() for char in text):
            for i in text.split():
                if i.isnumeric():
                    citations.append(int(i))

    data = {'Title': titles, 'arXiv': eprints, 'Citations': citations}

    df = pd.DataFrame(data=data)
    # df.to_csv('out.csv', index=False)
    return df
