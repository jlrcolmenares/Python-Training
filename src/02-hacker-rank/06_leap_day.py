# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
# 1) The year can be evenly divided by 4, is a leap year, unless:
#   1.1) The year can be evenly divided by 100, it is NOT a leap year, unless:
#       1.1.1) The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    # We start from the innermost condition to the outermost
    if year % 400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0 :    
        return True
    return False

if __name__ == "__main__":
    # leap years
    print(is_leap(2000))
    print(is_leap(2400))
    print(is_leap(2008))
    # not leap years
    print(is_leap(1991))
    print(is_leap(1900))
    print(is_leap(2200))
    print(is_leap(2300))
    print(is_leap(2500))
