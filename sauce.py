from random import randint
import requests
from bs4 import BeautifulSoup

def hentai_code():
 code = input("Dou you really want hentai code, if it's yes then type Y[es] if it's no type N[o]: ")
 if code.lower() in ('yes', 'y'):
    del code 
    attemptCount = input('How many times do you want to attempt? ')
    if attemptCount.isdigit() & int(attemptCount) > 0:
        attemptCount = int(attemptCount)
        for _ in range(attemptCount):
           value = randint(100000, 400000)
           response = requests.get("https://nhentai.net/g/{}".format(value))
           soup = BeautifulSoup(response.text, 'html.parser')
           for title in soup.find_all('title'):
             print(title.get_text())
           if response.status_code == 200:        
              print("{} - is valid!".format(value))
           else:
              print("{} - we don't know you gotta try! [Response From Server: {}]".format(value, response.status_code))
 else:
   print("Cya! I will be hoping to see you again!")


 
if __name__ == "__main__":
    hentai_code()
 
import sauce
 
sauce.hentai_code()
