import requests, pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

url = {}
url['seasia'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDczcTEaI2oMCAQSCC9tLzA3M3ExEgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['sasia'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDZubjEaI2oMCAQSCC9tLzA2bm4xEgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['easia'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDJxbmsaI2oMCAQSCC9tLzAycW5rEgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['canada'] = 'https://www.google.com/travel/explore?tfs=CBwQAxokagcIARIDTEFYEgoyMDIyLTAyLTExcg0IBBIJL20vMGQwNjBnGiRqDQgEEgkvbS8wZDA2MGcSCjIwMjItMDItMTVyBwgBEgNMQVhwAoIBCwj___________8BQAFIAZgBAQ&tfu=GgA'
url['camerica'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDF0emgaI2oMCAQSCC9tLzAxdHpoEgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['mexico'] = 'https://www.google.com/travel/explore?tfs=CBwQAxokagcIARIDTEFYEgoyMDIyLTAyLTExcg0IBBIJL20vMGI5MF9yGiRqDQgEEgkvbS8wYjkwX3ISCjIwMjItMDItMTVyBwgBEgNMQVhwAoIBCwj___________8BQAFIAZgBAQ&tfu=GgA'
url['samerica'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDZuM3kaI2oMCAQSCC9tLzA2bjN5EgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['cafrica'] = 'https://www.google.com/travel/explore?tfs=CBwQAxokagcIARIDTEFYEgoyMDIyLTAyLTExcg0IBBIJL20vMDJuMGxkGiRqDQgEEgkvbS8wMm4wbGQSCjIwMjItMDItMTVyBwgBEgNMQVhwAoIBCwj___________8BQAFIAZgBAQ&tfu=GgA'
url['eafrica'] = 'https://www.google.com/travel/explore?tfs=CBwQAxokagcIARIDTEFYEgoyMDIyLTAyLTExcg0IBBIJL20vMDFtcWI2GiRqDQgEEgkvbS8wMW1xYjYSCjIwMjItMDItMTVyBwgBEgNMQVhwAoIBCwj___________8BQAFIAZgBAQ&tfu=GgA'
url['safrica'] = 'https://www.google.com/travel/explore?tfs=CBwQAxokagcIARIDTEFYEgoyMDIyLTAyLTExcg0IBBIJL20vMDJjNTl0GiRqDQgEEgkvbS8wMmM1OXQSCjIwMjItMDItMTVyBwgBEgNMQVhwAoIBCwj___________8BQAFIAZgBAQ&tfu=GgA'
url['nafrica'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDVnMnYaI2oMCAQSCC9tLzA1ZzJ2EgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['meast'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDR3c3oaI2oMCAQSCC9tLzA0d3N6EgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['eeurope'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDliNjkaI2oMCAQSCC9tLzA5YjY5EgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'
url['weurope'] = 'https://www.google.com/travel/explore?tfs=CBwQAxojagcIARIDTEFYEgoyMDIyLTAyLTExcgwIBBIIL20vMDg1MmgaI2oMCAQSCC9tLzA4NTJoEgoyMDIyLTAyLTE1cgcIARIDTEFYcAKCAQsI____________AUABSAGYAQE&tfu=GgA'

driver = webdriver.Chrome('C:/Users/owens/Desktop/IS455/DataRetrieval/chromedriver.exe')

html = []

for k,v in url.items():
    driver.get(v)
    sleep(6)
    html.append(BeautifulSoup(driver.page_source))

df = pd.DataFrame(
    columns=['City', 'Departure_Date', 'Return_Date', 'Picture_Path', 'Price', 'Num_Stops', 'Duration_Hours',
             'Duration_Minutes', 'Lodging_Cost', 'Description'])
df.set_index('City', inplace=True)
for page in html:
    places = page.find_all('li', {'class': 'lPyEac P0ukfb'})
    for place in places:
        picture = place.find('div', {'class': 'EWmqCb'})['style']
        picture = picture.split('\'')
        picture = picture[1]
        city = place.find('h3', {'class': 'W6bZuc YMlIz'}).text
        dates = place.find('div', {'class': 'xyc80b sSHqwe'}).text
        dates = dates.split('–')
        departureDate = dates[0]
        if len(dates[1]) < 3:
            returnDate = departureDate[:4] + dates[1]
        else:
            returnDate = dates[1]
        price = place.find('div', {'class': 'MJg7fb QB2Jof'})
        if not price is None:
            price = price.span.text[1:]
        else:
            price = ''
        stops = place.find('span', {'class': 'nx0jzf'})
        if not stops is None:
            stops = stops.text
            if stops == 'Nonstop':
                stops = 0
            else:
                stops = stops[:1]
        else:
            stops = ''
        duration = place.find('span', {'class': 'Xq1DAb'})
        if not duration is None:
            duration = duration.text
            if 'hr' in duration:
                durationHour = duration.split(' ')
                durationHour = durationHour[0]
                duration = duration[(duration.index('hr') + 3):]
            else:
                durationHour = 0
            if 'min' in duration:
                durationMin = duration.split(' ')
                durationMin = durationMin[0]
            else:
                durationMin = 0
        else:
            durationHour = ''
            durationMin = ''
        lodgingCost = place.find('div', {'class': 'o9JBjb QB2Jof'})
        if not lodgingCost is None:
            lodgingCost = lodgingCost.span.text[1:]
        else:
            lodgingCost = ''

        urlCity = city.replace(' ', '_')
        yahooUrl = f'https://en.wikipedia.org/wiki/{urlCity}'
        yahooHtml = requests.get(yahooUrl)
        descriptionHtml = BeautifulSoup(yahooHtml.text, 'html.parser')
        description = descriptionHtml.find('div', {'class': 'mw-parser-output'})

        if not description is None:
            description = description.find_all('p')
            if len(description) > 1:
                description = description[1].text
            else:
                description = description[0].text
        else:
            description = ''

        df.loc[city] = [departureDate, returnDate, picture, price, stops, durationHour, durationMin, lodgingCost,
                        description]

df

df.to_csv('flightData.csv')
driver.close()
