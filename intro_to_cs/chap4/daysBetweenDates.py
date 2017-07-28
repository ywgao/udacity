daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
  return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  # add days
  totalDays = day2 - day1
  
  # add year's days
  for year in range(year1, year2):
    if isLeapYear(year):
      totalDays += 366
    else:
      totalDays += 365
  
  # add month's days
  if month1 > month2:
    for month in range(month2, month1):
      totalDays -= daysOfMonths[month - 1]
  else:
    for month in range(month1, month2):
      totalDays += daysOfMonths[month - 1]

  # add one day if current year is leap year.
  if isLeapYear(year2) & (month1 <= 2) & (month2 > 2):
    totalDays += 1
  print (totalDays)

daysBetweenDates(2012, 1, 1, 2012, 2, 28)
daysBetweenDates(2012, 1, 1, 2012, 3, 1)
daysBetweenDates(2011, 6, 30, 2012, 6, 30)
daysBetweenDates(2011, 1, 1, 2012, 8, 8)
daysBetweenDates(1900, 1, 1, 1999, 12, 31)
