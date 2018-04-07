
class StoreException(Exception):
    def __init__(self,msg):
        self.messafe = msg

class StoreNotFoundException(StoreException):
    pass
