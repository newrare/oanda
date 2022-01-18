###LIB###
import json     as Json
import os       as Os
import requests as Request

from Class.Base     import Base
from dotenv         import load_dotenv as Env
from types          import SimpleNamespace

Env()

#OANDA API DOC https://developer.oanda.com/rest-live-v20/account-ep/



###CLASS###
class Api(Base):
    """Api Class"""
    Class   = "Api"
    mode    = ""
    key     = ""
    call    = ""
    url     = ""
    error   = ""
    Result  = ""


    ##INI##
    def __init__(self):
        self.mode = Os.getenv("MODE")

        if "LIVE" == self.mode:
            self.key = Os.getenv("OANDA_KEY_LIVE")
            self.url = Os.getenv("OANDA_URL_LIVE")
        else:
            self.key = Os.getenv("OANDA_KEY_DEMO")
            self.url = Os.getenv("OANDA_URL_DEMO")


    ##METHOD##
    def get(self, uri):
        self.call = self.url + uri

        token = "Bearer " + self.key

        #call API and save Response on Result
        self.Result = Request.get(self.call, headers={"Authorization": token})

        return self.check()

    def check(self):
        if "OK" != self.Result.reason:
            self.error  = self.Result.text
        else:
            self.Result = Json.loads(self.Result.text)

        return self
