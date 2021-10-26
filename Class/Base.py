###LIB###
import inspect as Inspect



###CLASS###
class Base:
    """Base Abstract Class"""

    ##METHOD##
    def show(self):
        for members in Inspect.getmembers(self):
            if not members[0].startswith("_") and isinstance(members[1], str):
                print("{:<15s}{:>1s}".format(members[0],members[1]))
                #attribute = members[0] + " => " + members[1]
                #print(attribute)
