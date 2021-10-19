###LIB###
import os as Os

from datetime import datetime as Date
from dotenv import load_dotenv as Env

Env()



###CLASS###
class Logger:
    """Log Class"""
    name    = "Logger"
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

    def show(self):
        print(self.message)

