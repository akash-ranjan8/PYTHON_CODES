class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class ThreeSeries(BMW):
    def __init__(self,cruisecontrolenabled,make,model,year):
       BMW.__init__(self,make,model,year)
       self.cruisecontrolenabled=cruisecontrolenabled
three=ThreeSeries(True,"BMW","328i","2018")
print(three.cruisecontrolenabled)
print(three.make)
print(three.model)
print(three.year)
