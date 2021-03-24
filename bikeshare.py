import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_user_inputs(input_str,input_check):
# this function takes the user inputs and check if the input data of the city, month, day is correct either lower or uppercase
# TO DO: get user input for city (chicago, new york city, washington).
# HINT: Use a while loop to handle invalid inputs

    while True: #keep asking the user for an input until the input matches the requirments
        input_string=input(input_str).lower()
        try: # this to make sure the code will not run a error also that the input data are the same for each list
            if input_string.lower() in ['chicago','new york','washington'] and input_check == 1:
                break
            elif input_string.lower() in ['january', 'february', 'march', 'april', 'may', 'june','all'] and input_check == 2:
                break
            elif input_string.lower() in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_check == 3:
                break
            else:
                if input_check == 1:
                    print("Sorry, your input should be one of the following cities: chicago, new york city ,or washington")
                if input_check == 2 :
                    print("Sorry, your input should be one of the following months: january, february, march, april, may, june , all ")
                if input_check == 3 :
                    print("Sorry, your input should be: sunday, ... friday, saturday or all")
        except ValueError:
            print("Sorry, your input is incorrect can you please try again")
    return input_string

def get_filters():
    # this functin asks the user to specify a city, month and day to analyze.
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please Enter name of the City, Month and Day')

    city = check_user_inputs("Would you like to see the data for chicago, new york city or washington?",1)

    # get user input for month (all, january, february, ... , june)
    month = check_user_inputs("Which Month (all, january, ... june)?",2)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_user_inputs("Which day? (all, monday, tuesday, ... sunday)",3)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)
    # TO DO: display the most common day of week

    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', popular_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':

        # TO DO: Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    ''' this function display 5 rows of data from the csv file for the selected city.'''
    RESPONSE_LIST = ['yes', 'no']
    user_response = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while user_response not in RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        user_response = input().lower()
        #the raw data from the df is displayed if user opts for it
        if user_response == "yes":
            print(df.head())
        elif user_response not in RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while user_response == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        user_response = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if user_response == "yes":
             print(df[counter:counter+5])
        elif user_response != "yes":
             break

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        #this to keep asking the user
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
             break
        else:
            print('Please Enter yes or anything to end the program')

if __name__ == "__main__":
	main()
