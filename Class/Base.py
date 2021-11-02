###LIB###
import inspect as Inspect



###CLASS###
class Base:
    """Base Abstract Class"""

    ##METHOD##
    def show(self):
        self.detail(self)

    def detail(self, Object):
        for members in Inspect.getmembers(Object):
                if not members[0].startswith("_") and isinstance(members[1], str):
                    print("{:<15s}{:>1s}".format(members[0],members[1]))
