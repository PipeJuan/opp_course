from account import Account

class Car:
    id        = int
    license   = str 
    driver    = Account("","") 
    passenger = int 

    def __init__(self,license,driver): #Declarando el metodo contructor que le da valores minimos a nuestro objeto para inicializar

        self.license = license
        self.driver  = driver 
    