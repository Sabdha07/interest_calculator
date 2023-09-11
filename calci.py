import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# Set the page title
st.set_page_config(page_title="Interest Calculator", page_icon=":calculator:", layout="centered")

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
    #year = start_date.year
    if is_leap_year(start_date.year) or is_leap_year(end_date.year):
        days_in_year = 366 
    else:
        days_in_year = 365 

    # Calculate the interest
    interest = (principal * rate  * days/ (days_in_year*100))
    return interest


# Streamlit app title and description
st.title("Due Date Calculator")
st.write("Enter the principle amount, issue date, and number of months to calculate the due date.")

#prereq
#current_datetime = datetime.now() #current date and time
#current_date = current_datetime.date() #current date

# User input fields
principle = st.number_input("Principle amount", value = None) #principle amount
issue_date = st.date_input("Issue Date",format="DD.MM.YYYY") #issue date
current_date = st.date_input("Current Date",format="DD.MM.YYYY") #current date
num_months = st.number_input("Number of Months", min_value=1, step=1) #number of months
interest_rate = st.number_input("Interest Rate", min_value=0, step=0) #rate of interest
penal_interest_rate = st.number_input("Penal Interest Rate", min_value=0, step=0) #penal interest rate


#calculate and display due date
due_date = issue_date + relativedelta(months=+num_months)
st.write(f"Today's Date: {current_date.strftime('%d-%m-%Y')}")
st.write(f"Due Date: {due_date.strftime('%d-%m-%Y')}")
if (current_date - issue_date).days > 0:
    st.write("Number of days passed till today:",  (current_date - issue_date).days)
st.write("Total number of days:",  (due_date - issue_date).days)

# Calculate the interest until the due date
interest_until_due_date = calculate_interest(principle, interest_rate, issue_date, due_date)

# Calculate the penal interest if the current date is after the due date
penal_interest = 0.0
if current_date > due_date:
    days_past_due = (current_date - due_date).days
    st.write("Number of days past due:", days_past_due)
    penal_interest = calculate_interest(principle, penal_interest_rate, due_date, current_date)


# Calculate the due date
if st.button("Calculate"):
    st.write(f"Interest until Due Date: {interest_until_due_date:.2f}")
    st.write(f"Penal Interest: {penal_interest:.2f}")
    st.write(f"Total Interest: {interest_until_due_date + penal_interest:.2f}")
