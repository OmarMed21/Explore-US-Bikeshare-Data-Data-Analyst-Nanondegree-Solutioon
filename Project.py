import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
        city = input('Enter the City (Chicago, NYC, Washington DC) : ')
        if city not in ('Chicago', 'NYC','Washington DC'):
            print("Oops Sorry we can't find that")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the Month (January, February, March, April, May, June, all) : ')
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("Oops Sorry we can't find that")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Enter the day (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) : ')
        if day not in ('Saturday', 'Sunday', 'Monday', 'Tuesday',' Wednesday', 'Thursday', 'Friday'):
            print("Oops Sorry we can't find that")
            continue
        else:
            break

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    The_Most_Common_Month = df['month'].mode()[0]
    print(f'The Most Common Month is {The_Most_Common_Month}')

    # TO DO: display the most common day of week
    The_Most_Common_Day = df['day_of_week'].mode()[0]
    print(f'The Most Common Day is {The_Most_Common_Day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    The_Most_Common_Hour = df['hour'].mode()[0]
    print(f'The Most Common hour is {The_Most_Common_Hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    The_Most_Common_Start_Station = df['Start Station'].value_counts().idxmax()
    print(f'The Most Common Start Station is {The_Most_Common_Start_Station}')

    # TO DO: display most commonly used end station
    The_Most_Common_End_Station = df['End Station'].value_counts().idxmax()
    print(f'The Most Common End Station is {The_Most_Common_End_Station}')

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).count()

    print(f'The Most Frequent Combination are {The_Most_Common_Start_Station} and {The_Most_Common_End_Station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print(f'The Total Travel Time is {total_time/86400} Days')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f'The Mean Travel Time is {total_time/60} Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].value_counts()
    print(f'The Count of Users are {users}')

    # TO DO: Display counts of gender
    df['Gender'] = df['Gender'].dropna()
    gender = df['Gender'].value_counts()
    print(f'The Gender Types are {gender}')

    # TO DO: Display earliest, most recent, and most common year of birth
    df['Birth Year'] = df['Birth Year'].dropna()
    early = df['Birth Year'].min()
    print(f'The Earliest Year is {early}')

    recent = df['Birth Year'].max()
    print(f'The Recent Year is {recent}')

    common = df['Birth Year'].idxmax()
    print(f'The Most Common Year is {common}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
