import pandas as pd
# basic pandas dataframe
df = pd.read_csv('student_mental_health.csv')

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

#reading csv file
def reading_csv_file(df):
    print("\n============student mental health==============")
    print(df)

#pandas analyzing data
def analyzing_dataframe(df):
    #viewing the data
    def use_of_head_function(df):
        print("\n=========head function==========")
        print(df.head(10)) #The head() method returns the headers and a specified number of rows, starting from the top.

    def use_of_tail_function(df):
        print("\n=============tail function============")
        print(df.tail(5)) #The tail() method returns the headers and a specified number of rows, starting from the bottom.

    def use_of_info_function(df):
        print("\n=================info function===============")
        print(df.info()) #The DataFrames object has a method called info(), that gives you more information about the data set

    def main_menu_of_analyzing_data():
        while True:
            print("\n=========Analyzing DataFrame==========")
            print("1. Use of head function")
            print("2. Use of tail function")
            print("3. Use of info function")
            print("4. exit the menu")

            choice = int(input("enter your choice between(1-4)=> "))

            if choice == 1:
                use_of_head_function(df)
            elif choice == 2:
                use_of_tail_function(df)
            elif choice == 3:
                use_of_info_function(df)
            elif choice == 4:
                print("\nexiting the main menu of analyzing data")
                break
            else:
                print("[invalid choice] please enter number between 1-4")
    main_menu_of_analyzing_data()

def main_menu_of_pandas(df):
    while True:
        print("\n=======main menu of pandas========")
        print("1. run basic dataframe of pandas")
        print("2. run reading csv file")
        print("3. run analyzing dataframe")
        print("4. exit the main menu of pandas")
        
        choice = int(input("Enter your choice between(1-4)=> "))
        
        if choice == 1:
            basic_dataframe_of_pandas()
        elif choice == 2:
            reading_csv_file(df)
        elif choice == 3:
            analyzing_dataframe(df)
        elif choice == 4:
            print("\nexiting the main menu of pandas")
            break
        else:
            print("[invalid choice] please enter number between 1-4")
main_menu_of_pandas(df)
