from payment import Payment

class Creditcard(Payment):

    id              = int
    cvv             = int
    experation_date = int
    number          = int

    def __init__(self,id, number, cvv, expiration_date):
        super().__init__(id)
        self.number          = number
        self.cvv             = cvv
        self.experation_date = expiration_date
        