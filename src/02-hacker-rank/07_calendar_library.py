# You are given a date. Your task is to find what the day is on that date.

import calendar

def dia_segun_fecha(date_str):
    # we split the string and transform it into a list of strings
    lista_fecha = list(date_str.split())
    # then, we took the strings and transform them to a list of integers (using list comprehension)
    list_fecha_enteros = [int(item) for item in lista_fecha]
    # we asign the value of the previous list to 3 variables
    month, day, year = list_fecha_enteros
    #print(day,month,year,sep='-') # we could confirm if the conversion was right

    # calendar library allow us to create an array of the days in a week using calendar.dayname
    # we make these strings uppercase (using list comprehension)
    DayToStr = [item.upper() for item in list(calendar.day_name)]
    
    # Finnally, the weekday method returns the day a number indicating the day of the week 
    # who correspond tho any given day in the year. (monday = 0)
    return print(DayToStr[calendar.weekday(year,month,day)])

if __name__ == "__main__":
    text='05 08 2020'
    dia_segun_fecha(text)

# Basic use of the library: Print 2020 calendar
# print(calendar.TextCalendar(firstweekday=0).formatyear(2020)

# help(calendar)