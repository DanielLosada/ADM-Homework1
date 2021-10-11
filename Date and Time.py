#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

m, d, y = list(map(int,input().split()))

weekday = calendar.weekday(y, m, d)
if(weekday == 0):
    print("MONDAY")
elif(weekday == 1):
    print("TUESDAY")
elif(weekday == 2):
    print("WEDNESDAY")
elif(weekday == 3):
    print("THURSDAY")
elif(weekday == 4):
    print("FRIDAY")
elif(weekday == 5):
    print("SATURDAY")
else:
    print("SUNDAY")

