import pandas as pd
def Validate_customer(Customer_df):
    # Acceptable Feature Value Set
    Education_values={1,2,3,4}
    Maritial_values={1,2,3}
    Sex_values={1,2}

    for index, row in Customer_df.iterrows():

        # Df Values
        Age=row["AGE"]
        Limit_Balance=row["LIMIT_BAL"]
        Maritial_Status=row["MARRIAGE"]
        Sex=row["SEX"]
        Education=row["EDUCATION"]

        # Checking Df values:

        if Customer_df.isnull().any().any():
            print("Null values present")
            return False
        if Age<18 or Age>100:
            print(f"Customer {index} age less than 18")
            return False
        if  Limit_Balance<=0:
            print(f"Customer {index} limit balance <=0 ")
            return False
        if Maritial_Status not in Maritial_values:
            print(f"Customer {index} Maritial Status Invalid")
            return False
        if Sex not in Sex_values:
            print(f"Customer {index} Sex Status Invalid")
            return False
        if Education not in Education_values:
            print(f"Customer {index} Education Status Invalid")
            return False
            
        for i in range(7):
            key=f"PAY_{i}"
            if i!=1:
                if row[key]<-2 or row[key]>9:
                    print(f"Customer {index} repayment status of last {i+1} month is invalid")
                    return False

            if i!=0:
                key=f"BILL_AMT{i}"
                if row[key]<0:
                    print(f"Customer {index} Bill Amount of last {i+1} month is invalid")
                    return False
                key=f"PAY_AMT{i}"
                if row[key]<0:
                    print(f"Customer {index} Payment Amount of last {i+1} month is invalid")
                    return False

            

    return True


    
