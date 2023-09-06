import streamlit as st
from datetime import datetime, timedelta

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Calculate the interest
def calculate_interest(principal, rate, start_date, end_date):
    # Calculate the number of days between start_date and end_date
    days = (end_date - start_date).days
    year = start_date.year
    days_in_year = 366 if is_leap_year(year) else 365

    # Calculate the interest
    interest = (principal * rate / days_in_year) * days  # Assuming 365 days in a year
    return interest


# Streamlit app title and description
st.title("Due Date Calculator")
st.write("Enter the principle amount, issue date, and number of months to calculate the due date.")

# User input fields
#principle amount
principle = st.number_input("Principle amount", min_value=0.00, step=0.01)
#issue date
issue_date = st.date_input("Issue Date")
#current date and time
current_datetime = datetime.now()
#current date
current_date = current_datetime.date()
#number of months
num_months = st.number_input("Number of Months", min_value=1, step=1)
#calculate and display due date
due_date = issue_date + timedelta(days=num_months * 30)
st.write(f"Today's Date: {current_date.strftime('%d-%m-%Y')}")
st.write(f"Due Date: {due_date.strftime('%d-%m-%Y')}")
st.write("Number of days:",  (current_date - issue_date).days)
#rate of interest
interest_rate = st.number_input("Interest Rate", min_value=0.00, step=0.01)
penal_interest_rate = st.number_input("Penal Interest Rate", min_value=0.00, step=0.01)

# Calculate the interest until the due date
interest_until_due_date = calculate_interest(principle, interest_rate, issue_date, due_date)

# Calculate the penal interest if the current date is after the due date
penal_interest = 0.0
if current_date > due_date:
    days_past_due = (current_date - due_date).days
    penal_interest = calculate_interest(principle, penal_interest_rate, due_date, current_date)


# Calculate the due date
if st.button("Calculate"):
    st.write(f"Interest until Due Date: {interest_until_due_date:.2f}")
    st.write(f"Penal Interest: {penal_interest:.2f}")
    st.write(f"Total Interest: {interest_until_due_date + penal_interest:.2f}")
