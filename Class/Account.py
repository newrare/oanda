###LIB###
import os as Os

from Class.Base     import Base
from Class.Api      import Api



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


    ##METHOD##
    def summary(self):

        Summary = Api().get("accounts/" + self.id + "/summary")

        if "" != Summary.error:
            self.error = Summary.error

            return self
