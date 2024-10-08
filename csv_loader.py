import pandas as pd
def load_to_csv(data):
    df=pd.DataFrame(data=data)
    df.to_csv("data.csv")
    return "Csv created"