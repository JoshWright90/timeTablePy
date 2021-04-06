import sys
import datetime

day = datetime.date.today().weekday()
#for testing
#day = datetime.date(2021,2,12).weekday()

weeknum = datetime.date.today().isocalendar()[1]
#for testing
#weeknum = datetime.date(2021,2,12).isocalendar()[1]

if weeknum % 2 ==0:
    abWeek = "A"
else:
    abWeek = "B"
    
timetable_a = []
timetable_b = []

# A Week
timetable_a.append(["ICT Media","Computer Science","Science","Maths","English"]) #Monday
timetable_a.append(["Maths","Science","English","Science","Computer Science"]) #Tuesday
timetable_a.append(["Engineering","PE","History","Science","Maths"]) #Wednesday
timetable_a.append(["English","History","Maths","PE","Science"]) #Thursday
timetable_a.append(["Computer Science","ICT Media","Maths","Engineering","History"]) #Friday

# B Week
timetable_b.append(["Science","Maths","English","ICT Media","English"]) #Monday
timetable_b.append(["Computer Science","Science","English","Maths","PE"]) #Tuesday
timetable_b.append(["Engineering","History","Science","PE","English"]) #Wednesday
timetable_b.append(["ICT Media","ICT Media","Maths","Science","English"]) #Thursday
timetable_b.append(["Engineering","English","History","Computer Science","Engineering"]) #Friday
            

def main():
   print("************Good Morning**************")
   menu()
   again = input("Press enter to search again")
   if again == "":
       menu()

def menu():                                                                        
    print()
    choice = input("""
        A: Lessons - Today
        B: Lessons - Tomorrow
        C: Lessons - This Week
        Q: Quit

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        today()
    elif choice == "B" or choice =="b":
        tomorrow()
    elif choice == "C" or choice =="c":
        week()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A or B, or C")
        print("Please try again")
        menu()

def today():
   print("THIS WEEK IS ** ",(abWeek)," ** WEEK")
   if abWeek == "A":
       if day == 0: 
           for index, lesson in enumerate(timetable_a[0],start=1):
               print(index,lesson)
       elif day == 1: 
           for index, lesson in enumerate(timetable_a[1],start=1):
               print(index,lesson)
       elif day == 2: 
           for index, lesson in enumerate(timetable_a[2],start=1):
               print(index,lesson)
       elif day == 3: 
           for index, lesson in enumerate(timetable_a[3],start=1):
               print(index,lesson)
       elif day == 4: 
           for index, lesson in enumerate(timetable_a[4],start=1):
               print(index,lesson)
   elif abWeek == "B":
       if day == 0: 
           for index, lesson in enumerate(timetable_b[0],start=1):
               print(index,lesson)
       elif day == 1: 
           for index, lesson in enumerate(timetable_b[1],start=1):
               print(index,lesson)
       elif day == 2: 
           for index, lesson in enumerate(timetable_b[2],start=1):
               print(index,lesson)
       elif day == 3: 
           for index, lesson in enumerate(timetable_b[3],start=1):
               print(index,lesson)
       elif day == 4: 
           for index, lesson in enumerate(timetable_b[4],start=1):
               print(index,lesson)

def tomorrow():
   print("THIS WEEK IS ** ",(abWeek)," ** WEEK")
   if abWeek == "A":
       if day == 0:
           for index, lesson in enumerate(timetable_a[1],start=1):
               print(index,lesson)
       elif day == 1:
           for index, lesson in enumerate(timetable_a[2],start=1):
               print(index,lesson)
       elif day == 2:
           for index, lesson in enumerate(timetable_a[3],start=1):
               print(index,lesson)
       elif day == 3:
           for index, lesson in enumerate(timetable_a[4],start=1):
               print(index,lesson)
       elif day == 4:
           print("Tomorrows Saturday, Stay in bed!")
   if abWeek == "B":
       if day == 0:
           for index, lesson in enumerate(timetable_b[1],start=1):
               print(index,lesson)
       elif day == 1:
           for index, lesson in enumerate(timetable_b[2],start=1):
               print(index,lesson)
       elif day == 2:
           for index, lesson in enumerate(timetable_b[3],start=1):
               print(index,lesson)
       elif day == 3:
           for index, lesson in enumerate(timetable_b[4],start=1):
               print(index,lesson)
       elif day == 4:
           print("Tomorrows Saturday, Stay in bed!")
def week():
   print("THIS WEEK IS ** ",(abWeek)," ** WEEK")
   if abWeek == "A": # Print A Week
       for index, lesson in enumerate(timetable_a[0:5], start=1):
           print(index,lesson)
   elif abWeek == "B": # Print B Week
       for index, lesson in enumerate(timetable_b[0:5], start=1):
           print(index,lesson)
main()
