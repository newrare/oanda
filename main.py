###LIB###
from Class.Logger   import Logger
from Class.Api      import Api



###MAIN###

#Logger("keke").show()
#Api().show()

Json = Api().get('https://api-fxtrade.oanda.com/v3/accounts')
#Result = Api().get('https://api-fxtrade.oanda.com/v3/accounts/{oanda_id}')
#Result = Api().get('https://api-fxtrade.oanda.com/v3/accounts/{oanda_id}/summary')
#Result = Api().get('https://api-fxtrade.oanda.com/v3/accounts/{oanda_id}/instruments')
Logger(Json).d()
