import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df['race'].value_counts()
    races = pd.Series([27816,3124,1039,311,271], index = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
    
    # What is the average age of men?
    
    df['sex'].value_counts()
    total_men = df.query("sex =='Male'")
    average_age_men = total_men['age'].mean()
    
    # What is the percentage of people who have a Bachelor's degree?
    
    bach_degree = df.query("education == 'Bachelors'")
    percentage_bachelors =len('population') / len(bach_degree) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    advanced_education = df.query("education == ['Bachelors', 'Masters', 'Doctorate']")
    advanced_education_high_income = df.query("education == ['Bachelors', 'Masters', 'Doctorate'] and salary== '>50K'")
    percentage_advanced_education_high_income =  len(advanced_education_high_income) / (len(advanced_education)) * 100

    
    # What percentage of people without advanced education make more than 50K?
    
    not_high_education = df.query("education not in @advanced_education")
    not_high_education_high_income = df.query("education not in @advanced_education and salary =='>50K'")
    percentage_not_high_education_high_income = (len(not_high_education_high_income) / len(not_high_education)) *100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    low_hours = df.query("`hours-per-week` == 1")
    num_min_workers = len(low_hours)
    rich_percentage = (len(min_hours_high_income) / (len(low_hours))) * 100

    # What country has the highest percentage of people that earn >50K?

    
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    
    indian_high_income = df.query("`native-country` =='India' and salary== '>50K'")
    top_IN_occupation = indian_high_income.groupby('occupation').size().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
