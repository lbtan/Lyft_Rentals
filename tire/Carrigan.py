from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self,tirewear):
        self.tirewear = tirewear


    def needs_service(self):
        for tire in self.tirewear:
            if tire >= 0.9:
                return True
            else: return False