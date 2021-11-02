###LIB###
import os       as Os
import requests as Request

from Class.Base import Base
from dotenv     import load_dotenv as Env

Env()



###CLASS###
class Api(Base):
    """Api Class"""
    Class   = "Api"
    account = ""
    key     = ""


    ##INI##
    def __init__(self):
        self.account    = Os.getenv("OANDA_ID")
        self.key        = Os.getenv("OANDA_KEY")


    ##METHOD##
    def get(self, uri):
        token = "Bearer " + self.key
        return Request.get(uri, headers={"Authorization": token})
