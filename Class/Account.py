###LIB###
import os as Os

from Class.Base     import Base
from Class.Api      import Api



#https://api-fxtrade.oanda.com/v3/accounts
#https://api-fxtrade.oanda.com/v3/accounts/{oanda_id}
#https://api-fxtrade.oanda.com/v3/accounts/{oanda_id}/summary
#https://api-fxtrade.oanda.com/v3/accounts/{oanda_id}/instruments


###CLASS###
class Account(Base):
    """Account Class"""
    Class   = "Account"
    error   = ""
    id      = ""
    balance = 0

    ##INI##
    def __init__(self):
        Accounts = Api().get("accounts")

        if "" != Accounts.error:
            self.error = Accounts.error

            return self

        self.id = Accounts.Result["accounts"][0]["id"]

        Account = Api().get("accounts/" + self.id)

        if "" != Account.error:
            self.error = Account.error

            return self

        self.balance = Account.Result["account"]["balance"]
