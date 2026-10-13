class UPIPayment:
    def pay(self, amount):
        return f"Payment of ₹{amount} completed using UPI."

class CardPayment:
    def pay(self, amount):
        return f"Payment of ₹{amount} completed using Card."

class CashPayment:
    def pay(self, amount):
        return f"Payment of ₹{amount} completed using Cash."

upi = UPIPayment()
card = CardPayment()
cash = CashPayment()

print(f"""UPI Payment:
{upi.pay(500)}
Card Payment:
{card.pay(1000)}
Cash Payment:
{cash.pay(300)}""")
