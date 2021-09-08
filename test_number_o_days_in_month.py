import pytest
import number_of_days_in_month

# I could use some function eg. fixture to load data from csv or something to test functions
long_month = 31
normal_month = 30
short_month = 28
short_month_leap_year = 29

normal_year_long_month_date = "2021-12"
normal_year_normal_month_date = "2021-4"
normal_year_short_month_date = "2019-2"
leap_year_short_month_date = "2020-2"
exception_leap_year_short_month_date = "2000-2"
normal_month_out_range_date = "2000-13"
random_value = "qwerty-123"
# I could also use @pytest.parametrize to put all
# functions into one but it is not a clear solution when i should show different scenarios


def test_normal_year_long_month():
    assert number_of_days_in_month.get_no_of_days(normal_year_long_month_date) == long_month


def test_normal_year_normal_month():
    assert number_of_days_in_month.get_no_of_days(normal_year_normal_month_date) == long_month


def test_normal_year_short_month():
    assert number_of_days_in_month.get_no_of_days(normal_year_short_month_date) == short_month


def test_leap_year_short_month():
    assert number_of_days_in_month.get_no_of_days(leap_year_short_month_date) == short_month_leap_year


def test_month_out_of_range():
    assert number_of_days_in_month.get_no_of_days(normal_month_out_range_date) is None


@pytest.mark.parametrize("test_input, expected", [(normal_month_out_range_date, None), (random_value, None)])
def test_random_argument_not_regex_match(test_input, expected):
    assert number_of_days_in_month.get_no_of_days(test_input) is expected
