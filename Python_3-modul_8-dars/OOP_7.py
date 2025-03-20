class User:
    def __init__(self, name, card, amount, currency):
        self.__name=name
        self.__card=card
        self.__amount=amount
        self.__currency=currency
    def get_name(self):
        return self.__name
    def get_currency(self):
        return self.__currency
    def add_amount(self, amount2):
        self.__amount+=amount2
        return self.__amount
    def get_money(self, amount3):
        if self.__amount>=amount3:
            self.__amount-=amount3
            return True
        if self.__amount<amount3:
            return False
    def __str__(self):
        return f"CARD INFO: \nHOLDER: {self.__name} \nAMOUNT: {self.__amount} {self.__currency}"

user1=User("Ali", "6800 1234 5678 1234", 107700.0, "UZS")
print(f"Foydalanuvchi ismi: {user1.get_name()}")
print(f"Valyuta birligi: {user1.get_currency()}")
print(f"Kartadagi jami summa: {user1.add_amount(100000)}")
print(f"Kartadan pul yechmoqchiman: {user1.get_money(7700)}")
print(f"Kartada qolgan summa: {user1.add_amount(0)}")
print(user1)


