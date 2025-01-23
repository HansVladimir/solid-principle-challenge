from abc import ABC, abstractmethod

class MethodPay(ABC):
    @abstractmethod
    def fee(self):
        pass

class Crypto(MethodPay):
    def fee(self,amount,fee):
        return amount - (amount*fee)
        
class Card(MethodPay):
    def fee(self, amount: float, fee: float) -> float:
        return amount - (amount * fee)
    
    

class FeeCalculator:
    
    @staticmethod
    def calculate_fee(payment_method:MethodPay,amount: float, fee: float):
        return payment_method.fee(amount,fee)
    
def main():
    C = Crypto()
    Result1 = FeeCalculator.calculate_fee(C, 100.0, 0.05)
    print(Result1)
    card = Card()
    Result2 = FeeCalculator.calculate_fee(card, 200,0.10)
    print(Result2)
if __name__ == "__main__":
    main()