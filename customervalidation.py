import pandas as pd
def Validate_customer(Customer_df):
    # Acceptable Feature Value Set
    Education_values={1,2,3,4}
    Maritial_values={1,2,3}
    Sex_values={1,2}


    # Df Values
    Age=Customer_df["AGE"].iloc[0]
    Limit_Balance=Customer_df["LIMIT_BAL"].iloc[0]
    Maritial_Status=Customer_df["MARRIAGE"].iloc[0]
    Sex=Customer_df["SEX"].iloc[0]
    Education=Customer_df["EDUCATION"].iloc[0]

    # Checking Df values:

    if Customer_df.isnull().any().any():
        print("Null values present")
        return False
    if Age<18 and Age>100:
        print("Customer age less than 18")
        return False
    if  Limit_Balance<=0:
        print("limit balance <=0 ")
        return False
    if Maritial_Status not in Maritial_values:
        print("Maritial Status Invalid")
        return False
    if Sex not in Sex_values:
        print("Sex Status Invalid")
        return False
    if Education not in Education_values:
        print("Education Status Invalid")
        return False
         
    for i in range(7):
        key=f"PAY_{i}"
        if Customer_df[key].iloc[0]<-2 and Customer_df [key].iloc[0]>9:
            print("repayment status of last {i+1} month is invalid")
            return False

        key=f"BILL_AMT{i}"
        if Customer_df[key].iloc[0]<0:
            print("Bill Amount of last {i+1} month is invalid")
            return False


        key=f"PAY_AMT{i}"
        if Customer_df[key].iloc[0]<0:
            print("Payment Amount of last {i+1} month is invalid")
            return False

         

    return True


    
