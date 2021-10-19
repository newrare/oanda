###LIB###
import requests
import sys

from Class.Logger import Logger



###MAIN###
Log = Logger("super")
Log.info()

#ending
sys.exit()



#curl
Res = requests.get('https://stackoverflow.com/questions/26000336')

print(Res)

