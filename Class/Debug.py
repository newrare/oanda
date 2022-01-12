###LIB###
import sys as System

from Class.Base import Base



###CLASS###
class Debug(Base):
    """Debug Class"""
    Class   = "Debug"
    message = ""


    ##INI##
    def __init__(self, message):
        self.message = message

        self.dump()


    ##METHOD##
    def dump(self):
        print(type(self.message))
        print(self.message)

        print(" ")
        print("**DETAIL**")

        self.detail(self.message)

        print(" ")

    def die(self):
        System.exit()
