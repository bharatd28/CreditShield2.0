import pandas as pd
def read_customerdata(file_path):
    customer_df=pd.read_csv(file_path)
    return customer_df
