#We will write program to convert years to seconds

years = int(input("Please enter number of years : "))

'''
No of months = 12
No of days = 365
No of hours in a day = 24
No of minutes in hour = 60
No of seconds in minute = 60
'''

calc_of_seconds = years * 12 * 365 * 24 * 60 * 60
print((f"{years} years contain {calc_of_seconds} seconds"))
