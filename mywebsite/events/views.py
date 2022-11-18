from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime




def home(request, year, month):
    name = "Ruslan"
    month = month.title()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calender
    cal = HTMLCalendar().formatmonth(year, month_number)
    # get current year
    now = datetime.now()
    current_year = now.year
    # get current time
    time = now.strftime('%H:%M')

    return render(request, 'home.html',
                  {"name": name, "year": year,
                   "month": month, "month_number": month_number,
                   "cal": cal,
                   "current_year": current_year,
                   "time": time})

