from abc import ABC, abstractmethod

class IPaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass
    
class BasicGiftCard(IPaymentGateway):
    def pay(self, amount: float) -> None:
        print(f"Gift card Basic used to pay {amount}.")

    def refund(self, amount: float) -> None:
        raise NotImplementedError("Gift cards Basic do not support refunds.")

    def handle_dispute(self, dispute_id: str) -> None:
        raise NotImplementedError("Gift cards Basic do not support disputes.")
    
class MediumGiftCard(IPaymentGateway):
    def pay(self, amount: float) -> None:
        print(f"Gift card Medium used to pay {amount}.")

    def refund(self, amount: float) -> None:
        raise NotImplementedError("Gift cards Medium do not support refunds.")

    def handle_dispute(self, dispute_id: str) -> None:
        raise NotImplementedError("Gift cards Medium do not support disputes.")
    
class ManagerGiftCard:
    def __init__(self, CardGift: IPaymentGateway):
        self.Card = CardGift

    def MakePayment(self, amount: float):
        self.Card.pay(amount)
    def MakeRefund(self, amount: float):
        self.Card.pay(amount)
    def HandleDispute(self, amount: float):
        self.Card.pay(amount)
    
def main():
    giftcard_basic = BasicGiftCard()
    ManagerCard = ManagerGiftCard(giftcard_basic)
    ManagerCard.MakePayment(100.0)

if __name__ == "__main__":
    main()