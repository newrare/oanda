###LIB###
import os as Os

from Class.Base     import Base
from Class.Api      import Api
from Class.Debug    import Debug as d



###CLASS###
class Account(Base):
    """Account Class"""
    Class   = "Account"
    error   = ""
    id      = ""
    balance = 0



    ##INI##
    def __init__(self):
        Call = Api().get("accounts")

        if "" != Call.error:
            self.error = Call.error

            return

        self.id = Call.Result["accounts"][0]["id"]

        CallAccount = Api().get("accounts/" + self.id)

        if "" != CallAccount.error:
            self.error = CallAccount.error

            return

        self.balance = CallAccount.Result["account"]["balance"]



    ##METHOD##
    def summary(self):
        Call = Api().get("accounts/" + self.id + "/summary")

        if "" != Call.error:
            self.error = Call.error

            return self

        return Call.Result["account"]


    def instruments(self):
        Call = Api().get("accounts/" + self.id + "/instruments")

        if "" != Call.error:
            self.error = Call.error

            return self

        return Call.Result["instruments"]


    def names(self):
        names       = []
        instruments = self.instruments()

        if not isinstance(instruments, list):
            return names

        for Instrument in instruments:
            names.append(Instrument["name"])

        return names
