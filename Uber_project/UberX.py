from car import Car

class UberX(Car): #Asi se aplica una herencia de una clase padre "Car" a la clase hija Uberx
    brand     = str
    model     = str

    def __init__(self,license,driver ,brand ,model ): #Declarando el metodo contructor que le da valores minimos a nuestro objeto para inicializar
        super().__init__(license,driver) # Declarando los valores minimo de nuestro metodo constructor del padre 
        self.brand   = brand
        self.model  = model 
    