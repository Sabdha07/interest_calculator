# interest_calculator

This is a simple Streamlit web application for calculating the due date of a financial transaction, along with the accrued interest and penal interest. The application takes the principal amount, issue date, number of months, interest rate, and penal interest rate as input, and then provides the due date and interest calculations based on the provided information.

How to Use:
Principle Amount: Enter the principal amount of the transaction. The minimum value allowed is 0.00, and you can use increments of 0.01.

Issue Date: Select the issue date using the date picker. This is the date when the financial transaction occurred.

Current Date: Choose the current date using the date picker. This is the date at which you want to calculate the due date and interest.

Number of Months: Specify the number of months for which you want to calculate the due date. The minimum value allowed is 1, and you can use increments of 1.

Interest Rate: Enter the interest rate as a percentage. The minimum value allowed is 0.00, and you can use increments of 0.01.

Penal Interest Rate: Enter the penal interest rate as a percentage. The minimum value allowed is 0.00, and you can use increments of 0.01.

Calculate Button: Click the "Calculate" button to calculate the due date, interest until the due date, penal interest (if applicable), and the total interest.

Results
Today's Date: Displays the current date you've entered in the format DD-MM-YYYY.

Due Date: Shows the calculated due date in the format DD-MM-YYYY.

Number of Days Passed Till Today: If the current date is after the issue date, this will display the number of days that have passed since the issue date.

Total Number of Days: Displays the total number of days between the issue date and the due date.

Interest Until Due Date: Shows the interest accrued on the principal amount until the due date.

Penal Interest: If the current date is after the due date, this will display the penal interest accrued.

Total Interest: Displays the sum of interest until the due date and penal interest (if applicable).

How it Works:
The application calculates the due date by adding the specified number of months to the issue date. It then calculates interest based on the principal amount, interest rate, and the number of days between the issue date and the due date. If the current date is after the due date, it also calculates penal interest based on the penal interest rate and the number of days past due.

The application takes into account leap years when calculating the number of days in a year.

Important Notes:
Ensure that you enter valid and consistent dates for accurate calculations.

The calculated results are based on the information you provide and the formula used in the code.

This application is intended for informational purposes and should not be used for critical financial decisions without verification by a financial expert.

Feel free to use this Due Date Calculator to quickly estimate due dates and interest amounts for your financial transactions.
