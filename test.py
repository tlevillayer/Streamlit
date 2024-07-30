import pandas as pd
import matplotlib.pyplot as plt
from calculator import MyCalculator


home_value=100000
deposit=10000
interest_rate=4.0
loan_term=15

# Calculate the repayments.

calculator = MyCalculator(home_value=home_value, deposit=deposit, interest_rate=interest_rate, loan_term=loan_term)
monthly_payment, total_payments, total_interest = calculator.calculate()
# Create a data-frame with the payment schedule.

schedule = calculator.scheduler()

df = pd.DataFrame(
    schedule,
    columns=["Mois", "Montant", "Principal", "Intérêt", "Montant restant", "Année"],
)

payments_df = df[["Année", "Montant restant"]].groupby("Année").min()

estimations = {}
for i in range(-10, 11):
    duration = loan_term + i
    calculation = MyCalculator(home_value=home_value, deposit=deposit, interest_rate=interest_rate, loan_term=duration)
    estimations[duration] = calculation.calculate()

print(estimations)