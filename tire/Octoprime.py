from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self,tirewear):
        self.tirewear = tirewear


    def needs_service(self):
        return sum(self.tirewear)
            