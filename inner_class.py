class car:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    class engine:
        def __init__(self,number):
            self.number=number
c=car("DZIRE",2015)
e=c.engine(123)
print(e)