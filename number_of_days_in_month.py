import calendar
import regex
from datetime import datetime


# get_no_of_days(“yyyy-mm”)
# Function get_no_of_days
# INPUT:
# "yyyy - int number range [from -1 mln to +1 mln years]
# "mm - int number range[1-12] without 0 leading
# strptime - convert string into a date and time


def get_no_of_days(date):
    try:
        is_date = regex.match("^(-[1-9]|-?[1-9][0-9]{1,6}|-?10000000|[0-9])-([1-9]|1[0-2])$", date)
        if is_date is not None:
            date_date_format = datetime.strptime(date, "%Y-%m")
            return calendar.monthrange(date_date_format.year, date_date_format.month)[1]
    except ValueError:
        return False
