###LIB###
import os       as Os
import sys      as System
import inspect  as Inspect

from Class.Base import Base
from datetime   import datetime     as Date
from dotenv     import load_dotenv  as Env

Env()



###CLASS###
class Logger(Base):
    """Log Class"""
    Class   = "Logger"
    message = ""


    ##INI##
    def __init__(self, message):
        self.message = message


    ##PRIVATE##
    def __date(self):
        #get date and time
        Now         = Date.now()
        dateString  = Now.strftime("[%Y-%m-%d|%H:%M:%S] ")

        return dateString

    def __save(self, level):
        #show and save log
        log = level + " " + self.__date() + self.message + "\n"
        print(log)

        DIRECTORY   = Os.getenv("DIRECTORY")
        File        = open(DIRECTORY + "/log/" + level.lower() + ".log", "a")
        File.write(log)
        File.close()

        return log


    ##METHOD##
    def info(self):
        return self.__save("INFO")

    def warn(self):
        return self.__save("WARN")

    def error(self):
        return self.__save("ERROR")

    def reset(self):
        self.message = ""

    def update(self, message):
        self.message = message

    def d(self):
        print(type(self.message))
        print(self.message)

        #show attributes and methods when message is Object
        self.detail(self.message)

        print(" ")

    def dd(self):
        self.d()
        System.exit()
