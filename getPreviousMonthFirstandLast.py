import datetime

#list of month contains all month with their days
dict_of_months={
    1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31
}

#get todays date
todays_date=datetime.datetime.now()

first_day_previous_month=""
last_day_previous_month=""

#If current month is january then previous month will be by default december
if todays_date.month==1:
    first_day_previous_month=f"{todays_date.year-1}-12-01"
    last_day_previous_month=f"{todays_date.year-1}-12-31"
else:
    first_day_previous_month=f"{todays_date.year}-0{todays_date.month-1}-01"
    last_day_previous_month=f"{todays_date.year}-0{todays_date.month-1}-{dict_of_months[todays_date.month-1]}"

print(first_day_previous_month)

print(last_day_previous_month)
