from oop_lab1 import MyRouter

class MyNewRouter(MyRouter):
    def __init__(self,  routername, model, serialno, iosversion, partsno):
        MyRouter.__init__(self, routername, model, serialno, iosversion)
        self.partsno = partsno

    def print_new_info(self, manufacturingdate ):
        # print("new router identifier: " + self.model + "_" + self.serialno + "_" + manufacturingdate)
        print("new router identifier: " + self.partsno + "_" +  self.model + "_" + manufacturingdate)



newrouter1 = MyNewRouter('R1', '2600', '133ab23', '12.1', '10')
print(issubclass(MyNewRouter, MyRouter))

newrouter1.print_router('31122019')
newrouter1.print_new_info('31122019')
