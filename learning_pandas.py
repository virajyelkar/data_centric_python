import pandas as pd
# basic pandas dataframe
def basic_dataframe_of_pandas():
    data = {
        "calories" : [120,350,500],
        "duration": [20,30,50]
    }
    df = pd.DataFrame(data)
    print(df)
    print(df.loc[0])
    df1 = pd.DataFrame(data, index=["day1","day2","day3"])
    print(df1)

def reading_csv_file():
    df = pd.read_csv('student_mental_health.csv')
    print(df)
reading_csv_file()
