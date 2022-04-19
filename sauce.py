from random import randint
import requests
        
code = input("Dou you really want hentai code, if it's yes then type Y[es] if it's no type N[o]: ")

if code.lower() == "Y" or code.lower() == "yes":
    for _ in range(6):
        value = randint(100000,400000)
        response = requests.get("https://nhentai.net/g/{}".format(value))
        if response.status_code == 200:        
          print("{} - is valid!".format(value))
        else:
          print("{} - we don't know you gotta try!".format(value))
else:
   print("Cya! I will be hoping to see you again!")






