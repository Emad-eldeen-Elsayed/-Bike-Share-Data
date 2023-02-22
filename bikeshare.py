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
    city = input("Would you like to see data for Chicago, New York City, or Washington?: ").lower() 
    while city not in CITY_DATA.keys():
         print('Please choose a valid city from the list')
         city = input("Would you like to see data for Chicago, New York City, or Washington?: ").lower()    
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    while True:
         month = input("Please choose a month from this list (January, February, March, April, May, June, all) to filter the data: ").lower()
         if month in months:
            break
         else:
            print('Please choose a valid month from the list') 
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] 
    while True:
        day = input("Please choose a day of week (all, monday, tuesday, ... sunday) to filter the data: ").lower()
        if day in days:
            break
        else:
             print('Please enter a valid day of week (all, monday, tuesday, ... sunday)')

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

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    df['start_hour'] = df['Start Time'].dt.hour
    
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
    print('The most common month is : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is : {}'.format(df['start_hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common End station is : {}'.format(df['End Station'].mode()[0]))
     
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = "From "+ df['Start Station']+" to "+df['End Station']
    print('The most common trip is : {}'.format(df['trip'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is :', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('The average travel time is :', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts())
        
    # TO DO: Display earliest, most recent, and most common year of birth    
        print('The most common year of birth is :',int(df['Birth Year'].mode()[0]))
        print('The most recent year of birth is :', int(df['Birth Year'].max()))
        print('The earliest year of birth is :',int(df['Birth Year'].min()))
        
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    # to prompt the user whether they would like want to see the raw data.
    i = 0
    responses = ['yes','no']
    response = input("Would you like to see 5 rows of the data ?, please reply with a responding Yes or No:").lower()
    while response not in responses:
        print("Please enter a valid response either Yes or No.: ")
        response = input("Would you like to see 5 rows of the data ?, please reply with a responding Yes or No:").lower()
        
    if response == 'no':
        print('Thank you for your participation.')        
                
    elif response == 'yes':
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            response = input("Would you like to see more 5 rows of the data ?, please reply with a responding Yes or No:").lower()
            while response not in responses:
                 print("Please enter a valid response either Yes or No.: ")
                 response = input("Would you like to see more 5 rows of the data ?, please reply with a responding Yes or No:").lower()
            if response == 'no':
                print('We appreciate your participation.')
                break   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
