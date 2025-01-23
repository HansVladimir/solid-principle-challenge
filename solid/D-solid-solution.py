from abc import ABC, abstractmethod

class ServicePay(ABC):
    @abstractmethod
    def pay(self, acount:str,amount:float):
        pass

class ServicePayPal(ServicePay):
    
    def pay(self,  acount:str,amount:float):
        print("Se realizo su pago por Paypal de Manera Exitosa")
class ServiceYape(ServicePay):
    
    def pay(self,  acount:str,amount:float):
        print("Se realizo su pago por Yape de Manera Exitosa")

class PaymentProcessor():
    def __init__(self, UsingPay: ServicePay):
        self.Pay = UsingPay
    def process_payment(self, acount: str, amount: float):
        self.Pay.pay(acount, amount)

def main():
    paypal_service = ServicePayPal()
    payment_processor = PaymentProcessor(paypal_service)
    payment_processor.process_payment("Hans", 100.0)

if __name__ == "__main__":
    main()