###LIB###
import os as Os

from Class.Base     import Base
from Class.Api      import Api
from Class.Debug    import Debug as d



###CLASS###
class Instrument(Base):
    """Instrument Class"""
    Class   = "Instrument"
    error   = ""
    name    = ""


    ##INI##
    def __init__(self, name):
        self.name = name



    ##METHOD##
    def orderBook(self):
        Call = Api().get("instruments/" + self.name + "/orderBook")

        if "" != Call.error:
            self.error = Call.error

            return self

        return Call.Result["orderBook"]
