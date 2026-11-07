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
    
    #Attributes (no parentheses) that describe the DataFrame's structure: row/column counts, names, and data types.
    def use_of_attributes(df):
        print("\n=================attributes================")
        print(f"Shape of DataFrame: {df.shape}")
        print(f"Columns of DataFrame: {df.columns.tolist()}")
        print(f"Data types of DataFrame: {df.dtypes.tolist()}")
        print(f"size of DataFrame: {df.size}")
    
    def use_of_describe(df):
        print("\n=============Describe function============")
        print(df.describe()) #Returns summary statistics (count, mean, std, min, quartiles, max). Compare feature scales and spot suspicious ranges before scaling.

    def use_of_value_counts(df):
        print("\n=============value_counts function=============")
        print(df.value_counts())

    def main_menu_of_analyzing_data():
        while True:
            print("\n=========Analyzing DataFrame==========")
            print("1. Use of head function")
            print("2. Use of tail function")
            print("3. Use of info function")
            print("4. Use of attributes")
            print("5. Use of describe function")
            print("6. Use of value_counts function")
            print("7. exit the menu")

            choice = int(input("enter your choice between(1-7)=> "))

            if choice == 1:
                use_of_head_function(df)
            elif choice == 2:
                use_of_tail_function(df)
            elif choice == 3:
                use_of_info_function(df)
            elif choice == 4:
                use_of_attributes(df)
            elif choice == 5:
                use_of_describe(df)
            elif choice == 6:
                use_of_value_counts(df)
            elif choice == 7:
                print("\nexiting the main menu of analyzing data")
                break
            else:
                print("[invalid choice] please enter number between 1-7")
    main_menu_of_analyzing_data()

#selecting and filtering data in pandas
def selecting_and_filtering_data(df):
    #selecting data
    def selecting_data(df):
        print("\n==============selecting data===============")
        print(df['age']) #selecting a single column
        print(df[['age','gender']]) #selecting multiple columns

    #filtering data
    def filtering_data(df):
        print("\n==============filtering data===============")
        print(df[df['age'] > 20]) #filtering rows based on a condition
        print(df[(df['age'] > 20) & (df['gender'] == 'Female')]) #filtering rows based on multiple conditions
    
    #Querying data
    def querying_data(df):
        print("\n==============querying data===============")
        print(df.query('age > 20')) #querying rows based on a condition
        print(df.query('age > 20 & gender == "Female"')) #querying rows based on multiple conditions
        print(df.query('age > 20 | study_hours > 7')) #querying rows based on multiple conditions with OR operator

    #isin function
    def isin_function(df):
        print("\n==============isin function===============")
        print(df['department'].isin(['BCA']))
        print(df[~df['department'].isin(['BCA'])]) #~is used to negate the condition, so it will return all the rows where the department is not BCA

    def main_menu_of_selecting_and_filtering_data():
        while True:
            print("\n=========main menu of selecting and filtering data==========")
            print("1. run selecting data")
            print("2. run filtering data")
            print("3. run querying data")
            print("4. run isin function")
            print("5. exit the menu")

            choice = int(input("Enter your choice between(1-5)=> "))

            if choice == 1:
                selecting_data(df)
            elif choice == 2:
                filtering_data(df)
            elif choice == 3:
                querying_data(df)
            elif choice == 4:
                isin_function(df)
            elif choice == 5:
                print("\nexiting the main menu of selecting and filtering data")
                break
            else:
                print("[invalid choice] please enter number between 1-5")
    main_menu_of_selecting_and_filtering_data()

#handling missing value
def handling_missing_values(df):
    def null_value(df):
            print("\n============== isnull function===========")
            print(df.isnull()) #to check specific cell is empty or blank

    def null_with_sum_function(df):
        print("\n=============isnull with sum===============")
        print(df.isnull().sum()) # Returns the column names with the total number of missing cells in each

    def not_null_function(df):
        print("\n==============notnull function==============")
        print(df.notnull()) #to check specific cell is not empty or blank

    #fillna function Replaces missing values with a constant, a statistic (mean/median/mode), or a per-column dict. This is imputation.
    def  fillna_function(df):
        print("\n==============fillna function==============")
        print(df.fillna(0)) #to fill the missing values with 0

    def fillna_with_parameters(df):
        print("\n================fillna with parameters================")
        print(df.fillna(value=None, limit=None, inplace=False))

    #ffill and bfill function Replaces missing values with the next or previous value in the column. This is imputation.
    def ffill_and_bfill_function(df):
        print("\n=================ffill and bfill function==================")
        print(df.ffill()) #to fill the missing values with the previous value
        print(df.bfill()) #to fill the missing values with the next value

    def ffill_and_bfill_with_limit_parameters(df):
        print("\n=================ffill and bfill with limit parameters==================")
        print(df.ffill(limit=2)) #to fill the missing values with the previous value, but only up to 2 consecutive values
        print(df.bfill(limit=2)) #to fill the missing values with the next value, but only up to 2 consecutive values

    def main_menu_of_handling_missing_values():
        while True:
            print("\n================main menu of handling missing values===============")
            print("1. run isnull function")
            print("2. run isnull with sum function")
            print("3. run notnull function")
            print("4. run fillna function")
            print("5. run fillna with parameters")
            print("6. run ffill and bfill function")
            print("7. run ffill and bfill with limit parameters")
            print("8. exit the menu")

            choice = int(input("Enter your choice between (1-8)=> "))

            if choice == 1:
                null_value(df)
            elif choice == 2:
                null_with_sum_function(df)
            elif choice == 3:
                not_null_function(df)
            elif choice == 4:
                fillna_function(df)
            elif choice == 5:
                fillna_with_parameters(df)
            elif choice == 6:
                ffill_and_bfill_function(df)
            elif choice == 7:
                ffill_and_bfill_with_limit_parameters(df)
            elif choice == 8:
                print("\n exiting the main menu of handling missing values...")
                break
            else:
                print("Invalid choice")
    main_menu_of_handling_missing_values()

#descriptive statistics in pandas with describe and more

def Individual_Descriptive_Statistical_Functions(df):
    def mean_function(df):
        print("\n==============mean function==============")
        print(df.mean(numeric_only=True)) #mean() function is used to calculate the mean of the values for the requested axis. The mean is the sum of the values divided by the number of values.
        print(df['sleep_hours'].mean()) #column based mean calculation

    def median_function(df):
        print("\n===============median function===========")
        print(df.median(numeric_only=True))#median() function is used to calculate the median of the values for the requested axis. The median is the middle value of the values.
        print(df['sleep_hours'].median()) #column based median calculation

    def mode_function(df):
        print("\n===============mode function==============")
        print(df.mode(numeric_only=True)) #mode() function is used to calculate the mode of the values for the requested axis. The mode is the value that appears most frequently in the values.
        print(df['sleep_hours'].mode()) #column based mode calculation

    #std() / var() function
    def std_and_var_function(df):
        print("\n===============std and var function==============")
        print(df.std(numeric_only=True)) #std() function is used to calculate the standard deviation of the values for the requested axis. The standard deviation is a measure of how spread out the values are.
        print(df.var(numeric_only=True)) #var() function is used to calculate the variance of the values for the requested axis. The variance is a measure of how spread out the values are.
        print(df['sleep_hours'].std()) #column based std calculation
        print(df['sleep_hours'].var()) #column based var calculation
    
    #min() / max() function
    def min_and_max_function(df):
        print("\n===============min and max function==============")
        print(df.min(numeric_only=True)) #min() function is used to calculate the minimum of the values for the requested axis. The minimum is the smallest value in the values.
        print(df.max(numeric_only=True)) #max() function is used to calculate the maximum
        print(df['screen_time'].min()) #column based min calculation
        print(df['screen_time'].max()) #column based max calculation
    
    #sum() / count() function
    def sum_and_count_function(df):
        print("\n===============sum and count function==============")
        print(df.sum(numeric_only=True)) #sum() function is used to calculate the sum of the values for the requested axis. The sum is the total of the values.
        print(df.count()) #count() function is used to calculate the count of the values for the requested axis. The count is the number of non-null values in the values.
        print(df['financial_stress'].sum()) #column based sum calculation

    #quantile() function
    def quantile_function(df):
        print("\n===============quantile function==============")
        print(df.quantile(numeric_only=True)) #quantile() function is used to calculate the quantiles of the values for the requested axis. The quantiles are the values that divide the values into equal parts.
        print(df['sleep_hours'].quantile()) #column based quantile calculation

    #skew() / kurt() function
    def skew_and_kurt_function(df):
        print("\n==============skew and kurt function==============")
        print(df.skew(numeric_only=True)) #skew() measures asymmetry (above 0 is a long right tail)
        print(df.kurt(numeric_only=True)) # kurt() measures tail heaviness. Both guide transformations such as log.

    #corr() function
    def corr_function(df):
        print("\n===============corr function===============")
        print(df.corr(numeric_only=True)) #Pairwise correlation between numeric columns. Shows feature-target relationships and redundant features.

    #agg() function
    def agg_function(df):
        print("\n=============== agg function=============")
        print(df.agg(["mean","min","max"])) #Computes several statistics at once, for all columns or a different list per column.
        print(df.agg({"sleep_hours" : "mean","marks" : ["mean","mode"]}))

    def main_menu_of_statistical_operation():
        while True:
            print("\n=========main menu of statistical operation============")
            print("1. run mean operation")
            print("2. run median operation")
            print("3. run mode operation")
            print("4. run standard deviation and variance operation")
            print("5. run min and max operation")
            print("6. run sum and count operation")
            print("7. run quantile calculation operation")
            print("8. run skew and kurt operation")
            print("9. run correlation operation")
            print("10. run agg operation")
            print("11. exit the main menu of descriptive statistics")

            choice = int(input("Enter your choice between(1-11)=> "))

            if choice == 1:
                mean_function(df)
            elif choice == 2:
                median_function(df)
            elif choice == 3:
                mode_function(df)
            elif choice == 4:
                std_and_var_function(df)
            elif choice == 5:
                min_and_max_function(df)
            elif choice == 6:
                sum_and_count_function(df)
            elif choice == 7:
                quantile_function(df)
            elif choice == 8:
                skew_and_kurt_function(df)
            elif choice == 9:
                corr_function(df)
            elif choice == 10:
                agg_function(df)
            elif choice == 11:
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
        print("4. run selecting and filtering data")
        print("5. run handling missing values")
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
            selecting_and_filtering_data(df)
        elif choice == 5:
            handling_missing_values(df)
        elif choice == 6:
            Individual_Descriptive_Statistical_Functions(df)
        elif choice == 7:
            print("\nexiting the main menu of pandas")
            break
        else:
            print("[invalid choice] please enter number between 1-7")
main_menu_of_pandas(df)
