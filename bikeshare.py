import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_month():
    '''getting the month from the user'''
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month= input("\nPlease pick a month from those options (all, january, february, ..., june) by typing its name: \n").lower()
    while True:    
        if month in months:
            break
        else:
            month= input("\nEnter the month in the same way as shown previously: \n").lower()
    return month
def get_day():
    '''getting the day from the user'''
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day= input("\n Please pick a day from those options (all, monday, tuesday, ..., sunday) by typing its name: \n").lower()
    while True:    
        if day in days:
            break
        else:
            day = input("\n Enter the day in the same way as shown previously: \n").lower()
    return day

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("Please pick a city from those options (chicago, new york city, washington) by typing its name: \n").lower()
    while True:
        if city in CITY_DATA:
            break  
        else:
            city = input("\nEnter the city name in the same way as shown previously: \n").lower()

    
    choose = input("\nWould you like to filter the data by month, day, both or not at all?\n").lower()
    """Asking the user to filter the data or not"""
    options =['month','day','both','not at all']
    while True:
        if choose == options[0]:
            # TO DO: get user input for month (all, january, february, ... , june)
            month = get_month()
            day = 'all'
            break
        elif choose == options[1]:
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = get_day()
            month = 'all'
            break
        elif choose == options[2]:
            '''the user chooses to filter by month and day'''
            month = get_month()
            day = get_day()
            break
        elif choose == options[3]:
            """the user didn't choose any filter"""
            month = 'all'
            day = 'all'
            break
        elif choose not in options:
            choose = input("\nPlease enter a valid option:\n").lower()
    print('-'*40)
    return city, month, day

def display(df):
    #display data - getting first 5 lines per iteration
    start=0
    see= input("\nWould you like to see some of the raw data?\nAnswer with yes or no\n").lower()
    while True:
        if see == 'yes':
            end= start+5
            while start < end:
                print(df[start:end])
                start += 5
            see = input("\nWould you like to see more of the raw data?\nAnswer with yes or no\n").lower()
        elif see =='no':
            break
        else:
            see=input("\nPlease type 'yes' if you want to show raw data or 'no' if you don't want that\n").lower()
    print('-'*40)
    
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nMost Common Month:',months[common_month - 1])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nMost Common Day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost Common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost Common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nMost Common End Station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    t=' to '
    df['start_to_end'] = df['Start Station'] + t + df['End Station']
    common_combination= df['start_to_end'].mode()[0]
    print('\nMost frequent combination of start station and end station trip:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_1 =time.gmtime(df['Trip Duration'].sum())
    total_travel_time_2 = time.strftime("%H hours :%M minutes :%S seconds",total_travel_time_1)
    print("\nTotal Trip Duration: ",total_travel_time_2)

    # TO DO: display mean travel time
    mean_travel_time_1 = time.gmtime(round(df['Trip Duration'].mean()))
    mean_travel_time_2 = time.strftime("%H hours :%M minutes :%S seconds",mean_travel_time_1)                                              
    print("\nAverage Trip Duration: ",mean_travel_time_2)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe count of each user type:\n",user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("\nThe number of users by gender:\n",gender)
    else:
        print("\nThere is no gender column in this city.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is: {}\nThe most recent year of birth: {}\nThe most common year of birth: {}".format(earliest,most_recent,most_common))
    else: 
        print("\nThere is no birth year column in this city info.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
"""def display(df):
    f=0
    see= input("\nWould you like to see some of the raw data?\nAnswer with yes or no").lower()
    while True:
        #see= input("\nWould you like to see some of the raw data?\nAnswer with yes or no").lower()
        if see == 'yes':
            while f < 5:
                print(df.head(f))
                f += 1
            see = input("\nWould you like to see more of the raw data?\nAnswer with yes or no").lower()
        elif see =='no':
            break
    print('-'*40)"""

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
