###LIB###
import json     as Json
import os       as Os
import requests as Request

from Class.Base import Base
from dotenv     import load_dotenv as Env
from types      import SimpleNamespace

Env()

#OANDA API DOC https://developer.oanda.com/rest-live-v20/account-ep/



###CLASS###
class Api(Base):
    """Api Class"""
    Class   = "Api"
    account = ""
    key     = ""
    Result  = ""


    ##INI##
    def __init__(self):
        self.account    = Os.getenv("OANDA_ID")
        self.key        = Os.getenv("OANDA_KEY")


    ##METHOD##
    def get(self, uri):
        token = "Bearer " + self.key

        #call API and save Response on Result
        self.Result = Request.get(uri, headers={"Authorization": token})

        return self.check()

    def check(self):
        if "OK" != self.Result.reason:
            return False

        return Json.loads(self.Result.text)
        #return Json.loads(self.Result.text, object_hook=lambda d: SimpleNamespace(**d))
        #print(Object.accounts)

