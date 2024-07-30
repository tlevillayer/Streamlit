import math

class MyCalculator:
    def __init__(self, home_value, deposit, interest_rate, loan_term):
        self.home_value = home_value
        self.deposit = deposit
        self.interest_rate = interest_rate
        self.loan_term = loan_term

        self.loan_amount = home_value - deposit
        self.monthly_interest_rate = 0
        self.number_of_payments = 0
        self.monthly_payment = 0
        self.total_payments = 0
        self.total_interest = 0

    def calculate(self):
        
        self.monthly_interest_rate = (self.interest_rate / 100) / 12
        self.number_of_payments = self.loan_term * 12
        self.monthly_payment = (
            self.loan_amount
            * (self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.number_of_payments)
            / ((1 + self.monthly_interest_rate) ** self.number_of_payments - 1)
        )

        # Calculate the repayments.
        self.total_payments = self.monthly_payment * self.number_of_payments
        self.total_interest = self.total_payments - self.loan_amount

        return self.monthly_payment, self.total_payments, self.total_interest
    
    def scheduler(self):
        schedule = []
        remaining_balance = self.loan_amount

        for i in range(1, self.number_of_payments + 1):
            self.interest_payment = remaining_balance * self.monthly_interest_rate
            principal_payment = self.monthly_payment - self.interest_payment
            remaining_balance -= principal_payment
            year = math.ceil(i / 12)  # Calculate the year into the loan
            schedule.append(
                [
                    i,
                    self.monthly_payment,
                    principal_payment,
                    self.interest_payment,
                    remaining_balance,
                    year,
                ]
            )

        return schedule