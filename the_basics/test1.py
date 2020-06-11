import datetime
print("current date time is ", datetime.datetime.now())

student_grades = {'sam':9.0, 'joy':7.5, 'harry': 8.5}

score_sum = sum(student_grades.values())
students = len(student_grades)
avg = score_sum/students

day_temperatures = { 'morning' : (23.4, 30.1, 28.1),
                     'noon' : (21.4, 31.1, 27.1),
                     'evening' : (19.1, 20.1 , 13.1)
                   }

print(avg)
print(day_temperatures)
