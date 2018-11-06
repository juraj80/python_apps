import datetime

def print_header():
    print('--------------------------------')
    print('         BIRTHDAY APP')
    print('--------------------------------')


def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('YEAR[YYYY]: '))
    month =  int(input('MONTH[MM]: '))
    day = int(input('DAY[DD]: '))
    birthday = datetime.date(year,month,day)
#    print(type(birthday))
    return birthday # class datetime.date

def compute_days_between_dates(original_date,target_date):
    this_year = datetime.date(target_date.year,original_date.month,original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_info(bday,day_diff):
    print('It looks like you were born on {}'.format(bday))
    if day_diff > 0:
        print('Your birthday is in {} days'.format(day_diff))
    elif day_diff < 0:
        print('Your birthday was {} days ago'.format(-day_diff))
    else:
        print('Happy Birthday!')

def main():
    print_header()
    user_bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(user_bday,today)
    print_birthday_info(user_bday,number_of_days)


main()
