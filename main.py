import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from calculator import MyCalculator

st.title("Calculatrice achat immobilier")

st.write("### Données d'entrée")
col1, col2 = st.columns(2)
home_value = col1.number_input("Valeur du bien", min_value=0, value=100000)
deposit = col1.number_input("Apport", min_value=0, value=10000)
interest_rate = col2.number_input("Taux d'intérêt (en %)", min_value=0.0, value=4.0)
loan_term = col2.number_input("Durée du crédit (en années)", min_value=1, value=20)

# Calculate the repayments.

calculator = MyCalculator(home_value=home_value, deposit=deposit, interest_rate=interest_rate, loan_term=loan_term)
monthly_payment, total_payments, total_interest = calculator.calculate()
st.metric(label="Total emprunté", value=f"{calculator.loan_amount:,.0f} €")

st.write("### Remboursements")
col1, col2, col3 = st.columns(3)
col1.metric(label="Mensualités", value=f"{monthly_payment:,.2f} €")
col2.metric(label="Remboursement total", value=f"{total_payments:,.0f} €")
col3.metric(label="Coût total des intérêts", value=f"{total_interest:,.0f} €")


# Create a data-frame with the payment schedule.

schedule = calculator.scheduler()

df = pd.DataFrame(
    schedule,
    columns=["Mois", "Montant", "Principal", "Intérêt", "Montant restant", "Année"],
)

# Display the data-frame as a chart.
st.write("### Echeancier")
payments_df = df[["Année", "Montant restant"]].groupby("Année").min()
st.line_chart(payments_df)
