class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """
        A class representing a credit card account.

        The initial balance of the credit card is zero.

        Parameters
        -----------
        customer : str
            The name of the customer (e.g., 'John Bowman').
        bank : str
            The name of the bank (e.g., 'California Savings').
        acnt : str
            The account identifier (e.g., '5391 0375 9387 5309').
        limit : float
            The credit limit of the card, measured in dollars.
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """
        Returns
        -------
        str
            The name of the customer
        """
        return self._customer

    def get_bank(self):
        """
        Returns
        -------
        str
            The name of the bank
        """
        return self._bank

    def get_account(self):
        """
        Returns
        -------
        str
            Card identifying number (typically stored as a string)
        """
        return self._acnt

    def get_limit(self):
        """
        Returns
        -------
        float
            The current limit of the card
        """
        return self._limit

    def get_balance(self):
        """
        Returns
        -------

        float
            The current balance
        """
        return self._balance

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient balance

        Returns
        --------
            Return True if charges was processed, False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


if __name__ == "__main__":
    wallet = []

    wallet.append(
        CreditCard("John Bowman", "California Savings", "5391 0375 9387 5309", 2500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Federal", "3485 0399 3395 1954", 3500)
    )
    wallet.append(
        CreditCard("John Bowman", "California Finance", "5391 0375 9387 5309", 5000)
    )

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val * 2)
        wallet[2].charge(val * 3)

    for c in range(3):
        print(f"Customer = {wallet[c].get_customer()}")
        print(f"Bank = {wallet[c].get_bank()}")
        print(f"Account = {wallet[c].get_account()}")
        print(f"Limit = {wallet[c].get_limit()}")
        print(f"Balance = {wallet[c].get_balance()}")

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f"New balance = {wallet[c].get_balance()}")

        print()
