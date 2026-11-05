import pandas as pd
# basic pandas dataframe
df = pd.read_csv('student_mental_health.csv')

#basic dataframe of pandas
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

#handling missing value
def handling_missing_values(df):
    def null_value(df):
            print("\n============== isnull function===========")
            print(df.isnull()) #to check specific cell is empty or blank

    def null_with_sum_function(df):
        print("\n=============isnull with sum===============")
        print(df.isnull().sum()) # Returns the column names with the total number of missing cells in each

    def main_menu_of_handling_missing_values():
        while True:
            print("\n================main menu of handling missing values===============")
            print("1. run isnull function")
            print("2. run isnull with sum function")
            print("3. exit the menu")

            choice = int(input("Enter your choice between (1-3) => "))

            if choice == 1:
                null_value(df)
            elif choice == 2:
                null_with_sum_function(df)
            elif choice == 3:
                print("\n exiting the main menu of handling missing values...")
                break
            else:
                print("Invalid choice")
    main_menu_of_handling_missing_values()

#descriptive statistics in pandas with describe and more
def use_of_describe(df):
    print(df.describe())

def Individual_Descriptive_Statistical_Functions(df):
    def mean_function(df):
        print("\n==============mean function==============")
        print(df.mean(numeric_only=True))#mean only works with numerical values

    def median_function(df):
        print("\n===============median function===========")
        print(df.median(numeric_only=True))

    def main_menu_of_statistical_operation():
        while True:
            print("\n=========main menu of statistical operation============")
            print("1. run mean operation")
            print("2. run median operation")
            print("3. exit the menu")

            choice = int(input("Enter your choice between(1-3)=> "))

            if choice == 1:
                mean_function(df)
            elif choice == 2:
                median_function(df)
            elif choice == 3:
                print("\nexiting the main menu of statistical functions")
                break
            else:
                print("\n invalid choice")
    main_menu_of_statistical_operation()

#main menu of pandas
def main_menu_of_pandas(df):
    while True:
        print("\n=======main menu of pandas========")
        print("1. run basic dataframe of pandas")
        print("2. run reading csv file")
        print("3. run analyzing dataframe")
        print("4. run handling missing values")
        print("5. run describe function")
        print("6. run individual statistical operation")
        print("7. exit the main menu of pandas")

        choice = int(input("Enter your choice between(1-7)=> "))

        if choice == 1:
            basic_dataframe_of_pandas()
        elif choice == 2:
            reading_csv_file(df)
        elif choice == 3:
            analyzing_dataframe(df)
        elif choice == 4:
            handling_missing_values(df)
        elif choice == 5:
            use_of_describe(df)
        elif choice == 6:
            Individual_Descriptive_Statistical_Functions(df)
        elif choice == 7:
            print("\nexiting the main menu of pandas")
            break
        else:
            print("[invalid choice] please enter number between 1-6")
main_menu_of_pandas(df)
