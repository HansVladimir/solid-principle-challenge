from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def pay(self, balance: float, amount: float):
        pass
    @abstractmethod
    def refund(self, amount: float):
        pass
        
    
class CardGift(Card):
    def pay(self, balance: float, amount: float):
        print("Realizaste el pago con tu tarjeta de regalo")
    def refund(self, amount: float):
        #print("Tarjeta de regalo no reembonsable.")
        raise ValueError("Tarjeta de regalo no reembonsable.")
    
class CardDebito(Card):
    def pay(self,balance: float, amount: float):
        print("Realizaste el pago con tu tarjeta de debito")
    def refund(self, amount: float):
        print("Tarjeta de debito reembonsable.")

class PaymentMethod:
    def __init__(self, balance: float, CardUser:Card):
        self.CardVisa = CardUser
        self.balance = balance
    def make_pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        self.CardVisa.pay(self.balance,amount)
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def make_refund(self, amount: float):
        self.CardVisa.refund(amount)
        self.balance += amount
        #print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")


def main():
    giftcard = CardGift()
    ManagerCard = PaymentMethod(200.0, giftcard)
    ManagerCard.make_pay(210)
    #ManagerCard.make_refund(10)

if __name__ == "__main__":
    main()