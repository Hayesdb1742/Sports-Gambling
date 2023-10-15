import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import gambling



url = "https://www.oddsshark.com/ncaaf/odds"

response = requests.get(url)
time.sleep(1)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    odds_section = soup.find_all(class_ = "odds--group__event-container football")

    oddsList = {}

    if odds_section:
        for game in odds_section:
            teams = game.find_all("div", class_="participant-name")
            if teams:
                team1 = teams[0].text.strip()
                team2 = teams[1].text.strip()
                entry = {}
                entry['opponent'] = team2
                oddsList[team1] = entry
                entry['opponent'] = team1
                oddsList[team2] = entry
            spreads = game.find("div",class_="odds--group__event-books")
            if spreads:
                for child in spreads.children:
                    if "book-5600" in child.attrs['class']:
                        book = "opening"
                    else:
                        book = "current"
                    spread1 = child.find("div", class_="first-row")
                    spread2 = child.find("div", class_="second-row")
                    if spread1:
                        s1 = spread1.find("div", class_="odds-spread")
                        s2 = spread2.find("div", class_="odds-spread")
                        ml1 = spread1.find("div", class_="odds-moneyline above-tablet-only")
                        ml2 = spread2.find("div", class_="odds-moneyline above-tablet-only")
                        ou1 = spread1.find("div", class_="odds-total above-tablet-only")
                        ou2 = spread2.find("div", class_="odds-total above-tablet-only")
                        # for box in spread1.children:
                        if s1:
                            oddsSpread = s1.find("div", attrs={"data-odds-spread": True})
                            oddsSignedSpread = s1.find("div", attrs={"data-odds-signed-spread": True})
                            print(oddsList[team1])
                            if oddsSpread and oddsSignedSpread:
                                oddsList[team1]['%s-odds-spread' % book] = oddsSpread.text
                                oddsList[team1]['odds-spread-signed'] = oddsSignedSpread.text
                            else:
                                print("no spread", team1)
                            # print(oddsSpread.text, oddsSignedSpread.text)
                        else:
                            print("No odds")
                        if s2:
                            oddsSpread = s2.find("div", attrs={"data-odds-spread": True})
                            oddsSignedSpread = s2.find("div", attrs={"data-odds-signed-spread": True})
                            if oddsSpread and oddsSignedSpread:
                                oddsList[team2]['odds-spread'] = oddsSpread.text.strip()
                                oddsList[team2]['odds-spread-signed'] = oddsSignedSpread.text.strip()

                            # print(oddsSpread.text, oddsSignedSpread.text)
                            
                        if ml1:
                            ml = ml1.find("div", attrs={"data-odds-moneyline": True})
                            oddsList[team1]['odds-ml'] = ml.text
                        if ml2:
                            ml = ml2.find("div", attrs={"data-odds-moneyline": True})
                            oddsList[team2]['odds-ml'] = ml.text.strip()
                        if ou1:
                            ou = ou1.find("div", attrs="data-odds-total")
                            overprice = ou1.find("div", attrs="data-odds-overprice")
                            oddsList[team1]['odds-ou-total'] = ou
                            oddsList[team1]['odds-ou-overprice'] = overprice
                        if ou2:
                            ou = ou1.find("div", attrs="data-odds-total")
                            overprice = ou2.find("div", attrs="data-odds-overprice")
                            if ou and overprice:
                                oddsList[team2]['odds-ou-total'] = ou.text.strip()
                                oddsList[team2]['odds-ou-overprice'] = overprice.text.strip()
    print(oddsList['Middle Tennessee'])     

              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                