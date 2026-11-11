from customerdetails import InputCustomerdata
from customervalidation import Validate_customer

while True:
    Customer_df = InputCustomerdata()

    if Validate_customer(Customer_df):
        print("Customer data validated successfully")
        break

    print("Please enter the customer details again.")
