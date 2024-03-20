import pandas as pd
from inspirehep_scraper import inspirehep_scraper
from send_email import send_email
import time

df = inspirehep_scraper()
yesterday_citations = df['Citations'].to_list()

while(True):
    time.sleep(86400)
    df = inspirehep_scraper()
    today_citations = df['Citations'].to_list()

    if today_citations != yesterday_citations and len(today_citations) == len(yesterday_citations):
        for i in range(len(today_citations)):
            if today_citations[i] != yesterday_citations[i]:
                msg = "Your paper \"" + df.iloc[i]['Title'] + "\" (arXiv:" + df.iloc[i]['arXiv'] + ") has new citation. Now it is cited " + str(df.iloc[i]['Citations']) + " times."
                send_email(msg)
    
    yesterday_citations = today_citations.copy()