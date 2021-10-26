###LIB###
from Class.Logger   import Logger
from Class.Api      import Api



###MAIN###
#Logger("keke").show()
#Api().show()

Res = Api().get('https://stackoverflow.com/questions/26000336')
print(Res)
