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
        city = input('which city you would like to filter with? New York City, Washington or Chicago? ').lower()
        if city not in ('new york city', 'washington','chicago'):
         print("Try again")
         continue
        else:
         break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
       month = input('which month you would like to filter with? All, January, February, March, April, May, June? ').lower()
       if month not in ('all', 'january','february','March','april','may','june'):
        print("Try again")
        continue
       else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input('which day you would like to filter with? All, Monday, Tuesday, Wednesday, Thurseday, Friday, Saturday, Sunday? ').lower()
      if day not in ('all', 'monday','tuesday','wednesday','thurseday','friday','saturday','sunday'):
       print("Try again")
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
    df =   pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    if month !='all':
        months = ['jan','feb','mar','abril','may','jun']
        month = months.index(month)+1
        df=df[df['month']==month]
    if day !='all':

        df=df[df['day']==day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    c_month=df['month'].mode()[0]
    print('The most common month is: ', c_month, "\n")

    # TO DO: display the most common day of week
    c_day=df['day'].mode()[0]
    print('The most common day of week is: ', c_day, "\n")


    # TO DO: display the most common start hour
    c_hour=df['hour'].mode()[0]
    print('The most common hour is: ', c_hour, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: \"', df['Start Station'].mode()[0], "\"\n")

    # TO DO: display most commonly used end station
    print('The most commonly used end station is: \"', df['End Station'].mode()[0], "\"\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Combo'] = "\""+ df['Start Station'] +"\"" + ' and ' + "\""+ df['End Station'] +"\""
    print('The most frequent combination of start station and end station trip is: ', df['Start_End_Combo'].mode()[0], "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the total travel time is: ', df['Trip Duration'].sum(),'\n')

    #  TO DO: display mean travel time
    print('the total mean travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, '\n')

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Gender: No data given for this city')
    else:
        gender = df.groupby(['Gender'])['Gender'].count()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Year of Birth Stats: No YOB data given for this city')
    else:
        earliest_yob = df['Birth Year'].min()
        print('Earliest YOB Is: ',earliest_yob)
        recent_yob = df['Birth Year'].max()
        print('Most Recent YOB Is: ',recent_yob)
        common_yob = df['Birth Year'].mode().max()
        print('Most Common YOB Is: ',common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_preview(df):
    raw_data= input('Would you like to preview raw data? Choose yes or no: \n')
    if raw_data.lower()=='yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count +=5
            more = input('5 more lines? Yes/No: \n')
            if more.lower()=='yes':
             continue
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
        data_preview(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
