from customerdetails import InputCustomerdata
from customervalidation import Validate_customer
from readcustomerdata import read_customerdata


while True:
        iscsv=input("Is the input is a CSV file (Y/N):")
        if iscsv=="Y":
            Customer_df=read_customerdata(input("Enter File Path:"))
        
        else:
            Customer_df = InputCustomerdata()


        if Validate_customer(Customer_df):
            print("Customer data validated successfully")
            break

        print("Please enter the customer details again.")


    
