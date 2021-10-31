import time
import pandas as pd
import numpy as np

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Args:
        None.
    Returns:
        str (city): name of the city to analyze
        str (month): name of the month to filter by, or "all" to apply no month filter
        str (day): name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWelcome to this program. Please choose your city:")
        print("\n1. Chicago \n2. New York City \n3. Washington")
        # print("\nPlease Type Your Reponse As An Integer (e.g 1 = chicago))")
        city = input("\nPlease Type Your Reponse As An Integer (e.g 1 = chicago))").lower()
        if city not in CITY_DATA.keys():
            print("\nSorry You have Entered Wrong Input, TRY AGAIN!!!")
            print("\nRestarting... Please Wait")
    print(f"\n{city.title()}")    
    Months = {'1':'January', 
              '2':'February', 
              '3':'March', 
              '4':'April', 
              '5': 'May', 
              '6':'June', 
              '7':'All' }
    month = ''
    while month not in Months.keys():
        
        print("\nPlease Enter The Month:")
        print("\n1. January \n2. February \n3. March\n4. April \n5. May \n6. June\n7. All Months")
        # print("\nPlease Type Your Reponse As An Integer (e.g 1 = January))")
        month = input("\nPlease Type Your Reponse As An Integer (e.g 1 = January))").lower()
        if month not in Months.keys():
            print("\nSorry You have Entered Wrong Input, TRY AGAIN!!!")
            print("\nRestarting... Please Wait")

    print(f"\n{Months[month]}")   
    Days = {'1':'monday', 
            '2':'tuesday', 
            '3':'wednesday', 
            '4':'thursday', 
            '5': 'friday', 
            '6':'saturday', 
            '7':'sunday' , 
            '8':'all' }
    day = ''
    while day not in Days:
        print("\n1. monday\n2. tuesday\n3. wednesday\n4. thursday\n5. friday\n6. saturday\n7. sunday \n8. all")
        # print("\nPlease Type Your Reponse As An Integer (e.g 1 = monday))")
       
        day = input("\nPlease Type Your Reponse As An Integer (e.g 1 = monday))").lower()

        if day not in Days:
            print("\nSorry You have Entered Wrong Input, TRY AGAIN!!!")
            print("\nRestarting... Please Wait")
    print('-'*40)
    return city, Months[month], Days[day]


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
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])
    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =  df['Start Time'].dt.day_name()

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

#     print('\nCalculating The Most Frequent Times of Travel...\n')
#     start_time = time.time()
    print('\nStatistic 1: The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display Most Popular month
    df['month'] = df['Start Time'].dt.month_name()
    Popular_month = df['month'].mode()[0]
    print("Most Popular month is ", Popular_month)
    df['day_of_week'] = df['Start Time'].dt.day_name()
    Popular_day = df['day_of_week'].mode()[0]
    print('Most Popular day is ', Popular_day)
    df['hour'] = df['Start Time'].dt.hour
    Popular_hour = df['hour'].mode()[0]
    print('Most Popular hour is ', Popular_hour)   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most Popularly used start station: %s" % popular_start_station)
    popular_stop_station = df['End Station'].mode()[0]
    print(f"\nMost Popularly used end station: "+popular_stop_station)    
    _combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("\nThe most frequent combination of trips are from" + str(_combination.split("||")))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    print("\nTotal Trip Duration from the selected dataset is: " + str(total_travel_time))    
    print("\nAverage Trip Duration from the selected dataset is: " + str(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type = df['User Type'].value_counts()

    print(f"User Types from selected dataset:\n\n %s " % user_type)  

    try:
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode()[0])
        print('Earliest birth from the given selected data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given seleted data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given selected data is: {}\n'.format(most_common_birth) )
        
    except:
        print("No birth year details found in this file.")

    try:
        _gender = df['Gender'].value_counts()
        print(f"\n\n\nGender Types in selected data below:\n\n{gender}")
    except:
        print("\nNo Gender Found in column file")
        
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)
    
def individual_data(df):
    #individual trip data.
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    
    while start_data < df_length:
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':
            
            print("\nDisplaying only 5 rows of data.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
