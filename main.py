###LIB###
from Class.Logger   import Logger
from Class.Api      import Api



###MAIN###
#Logger("keke").show()
#Api().show()

Result = Api().get('https://api-fxtrade.oanda.com/v3/accounts')
print(Result.reason)
print(Result.text)
