import requests
from bs4 import BeautifulSoup

print(" ______       _                _ ")#Logo
print("|  ____|     | |              | |")
print("| |__ ___  __| | ___ _ __ __ _| |")
print("|  __/ _ \/ _` |/ _ \ '__/ _` | |       CODED BY SOMEONE WHICH IS TRYING TO DIE")
print("| | |  __/ (_| |  __/ | | (_| | |    Legal Disclaimer: I'm not responsible for any damaged created with these tools!")
print("|_|  \___|\__,_|\___|_|  \__,_|_|")
print("")
print("")
print("[1]-ProxyScrapper")
print("[2]-About Federal")
print("[3]-Exit")


menu = int(input("I'm waiting for your command: ")) #Menu
if menu <= 0:
    print("Are you gay son?")
elif menu >= 4:
    print("Ain't proud son!")

proxyscrape = input() #Proxyscraper
if proxyscrape == '1':
    proxyDomain = "https://free-proxy-list.net"
    r = requests.get(proxyDomain)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', {"id": "proxylisttable"})
    proxies = open('proxies','w')
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        try:
            proxies.write(columns[0].get_text())
            print(columns[0].get_text())
            proxies.read()
            proxies.close()
        except:
            pass

aboutme = input()
if aboutme == '2':
    print("Early Developer, Aiming high")
