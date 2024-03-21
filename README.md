# Inspirehep Web Scraper
This is a web scraper to extract data from inspirehep. It can collect titles, arXiv numbers and citations of my author page ([https://inspirehep.net/authors/1622480](https://inspirehep.net/authors/1622480)). If there are new citations, it can also send me an email.
## Prerequisites
This program have used the following python modules: **BeatifuleSoup**, **selenium**, **pandas**, and **smtplib**. 
All of them can be installed by **pip**. It has been tested by chrome webdriver, which can be downloaded from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). 
The function for sending email has been tested by SMTP server from Google. 
## Usage
After downloading the webdriver, user should give the path to the executable file to the **executable_path** in the **inspirehep_scraper.py** file.
To use the email funciton, one have to edit the email addresses for sender and recipient in the **send_email.py**, and give the password of the sender account (For Gmail, it must be the APP password). 
Finally, please launch the main program by python:
```
python main.py
```
It will moniter my author page everyday. If there are any new citations, it will send a message to the recipient by email. 
Principally, it can be used to other authors on Inspirehep, too. 
