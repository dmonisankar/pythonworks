class MyRouter(object):
    "first hands on with oop"
    def __init__(self, routername, model, serialno, iosversion):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.iosversion = iosversion

    def print_router(self, manufacturingdate):
        print("router name :", self.routername)
        print("model:", self.model)
        print("serialno:", self.serialno)
        print("iosversion :", self.iosversion)
        print("model with manufacturing date", self.model + manufacturingdate)


router1 = MyRouter('R1', '2600', '133ab23', '12.1')
router1.print_router('08012020')

print(getattr(router1,'model'))
print(hasattr(router1,'model'))

setattr(router1, 'model', '2700')

print("updated model:" + router1.model)
