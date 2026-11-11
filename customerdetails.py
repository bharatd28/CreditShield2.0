import pandas as pd
def InputCustomerdata():
    # Intialization Of structure of Dictionary
    Customer_details={
    "LIMIT_BAL":None,
    "SEX":None,
    "EDUCATION":None,
    "MARRIAGE":None,
    "AGE":None,
    "PAY_0":None,
    "PAY_2":None,
    "PAY_3":None,
    "PAY_4":None,
    "PAY_5":None,
    "PAY_6":None,
    "BILL_AMT1":None,
    "BILL_AMT2":None,
    "BILL_AMT3":None,
    "BILL_AMT4":None,
    "BILL_AMT5":None,
    "BILL_AMT6":None,
    "PAY_AMT0":None,
    "PAY_AMT1":None,
    "PAY_AMT2":None,
    "PAY_AMT3":None,
    "PAY_AMT4":None,
    "PAY_AMT5":None,
    "PAY_AMT6":None}


    # Basic Customer detail Extraction
    Customer_details["LIMIT_BAL"]=int(input("Enter Customer's Limit Balance:"))
    Customer_details["AGE"]=int(input("Enter Customer's Age :"))
    Customer_details["EDUCATION"]=int(input("Enter Customer's Education Status (1 = graduate school; 2 = university; 3 = high school; 4 = others).:"))
    Customer_details["MARRIAGE"]=int(input("Enter Customer's Maritial Status (1 = married; 2 = single; 3 = others).:"))
    Customer_details["SEX"]=int(input("Enter Customer's Sex (1 = male; 2 = female).:"))

    # Advanced Payment Details Extraction
    for i in range(0,7):
        print("The measurement scale for the repayment status is: \n -1 = pay duly;\n 1 = payment delay for one month;\n 2 = payment delay for two months;\n .\n .\n .;\n 8 = payment delay for eight months;\n 9 = payment delay for nine months and above.")
        if i!=1:
            key=f"PAY_{i}"
            Customer_details[key]=int(input(f"Enter repayment status of last {i+1} month: "))
        if i!=0:
            key=f"BILL_AMT{i}"
            Customer_details[key]=int(input(f"Enter Bill Amount of last {i+1} month: "))
        key=f"PAY_AMT{i}"
        Customer_details[key]=int(input(f"Enter Payment Amount of last {i+1} month: "))
    # Conversion to DataFrame
    Customer_df=pd.DataFrame([Customer_details])
    return Customer_df



        



