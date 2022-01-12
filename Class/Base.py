###LIB###
import inspect  as Inspect
import json     as Json



###CLASS###
class Base:
    """Base Abstract Class"""

    ##METHOD##
    def show(self):
        self.detail(self)

    def detail(self, Object):
        if isinstance(Object, dict):
            #show details when Oject is dictonary like a Json
            print(Json.dumps(Object, indent=2, sort_keys=True))
        else:
            #show attributes and methods when Object
            for members in Inspect.getmembers(Object):
                    if not members[0].startswith("_") and isinstance(members[1], str):
                        if "" != members[1]:
                            print("{:<15s}{:>1s}".format(members[0],members[1]))
                        else:
                            print("{:<15s}{:>1s}".format(members[0],"<null>"))

                    if not members[0].startswith("_") and isinstance(members[1], dict):
                        print("{:<15s}{:>1s}".format(members[0],"<Object>"))
