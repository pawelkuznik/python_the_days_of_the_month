
# Description:
### The program counts the days of the month after entering the date and takes into account leap years
#### also contains some pytest tests
To write function returning the number of days in given month I use `datetime` and `calendar` modules
I wasn't sure if I could use these built-in functions, but nowhere said I couldn't;)
I could also write it manually:
convert date to two numbers and check:
if year % 400 == 0 or if year % 100 == 0 etc.
# To run tests:
 1. install latest pip package
 2. invoke in cmd: `pip install -r requierements.txt`
 3. run pytest by `pytest`
 4. If You want You have html report, you should invoke `pytest --html=report.html --self-contained-html` 

## I check in tests different scenarios:
