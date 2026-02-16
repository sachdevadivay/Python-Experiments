# Check whether the given number is divisible by 3 and 5 both.

a = int(input("enter the number:"))
if a %3 == 0 and a %5 == 0 :
    print("a is divisible by both 3 and 5")
else :
    print ("a is not divisible by 3 and 5")

# Check whether a given number is multiple of five or not.

a = int(input("Enter the number:"))
if a % 5 == 0 :
    print("a is multiple of 5")
else :
    print("a is not multiple of 5")

# Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”.

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
if a >b :
    print("a is greater than b")
elif b >a :
    print("b is greater than a")
else :
    print("Both a and b are same")

# Find the greatest among three numbers assuming no two values are same. 

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("enter the value of c:"))
if a > b and a >c :
    print("a is greater")
elif b > a and b > c :
    print("b is greater")
else :
    print("c is greater")

# Check whether the quadratic equation has real roots or imaginary roots. Display the roots.


import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))


D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and distinct")
    print("x1 =", x1)
    print("x2 =", x2)

elif D == 0:
    x = -b / (2*a)
    print("Roots are real and equal")
    print("x1 = x2 =", x)

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("Roots are imaginary")
    print("x1 =", real, "+ i", imag)
    print("x2 =", real, "- i", imag)

# Find whether a given year is a leap year or not.


year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

# Write a program which takes any date as input and display next date of the calendar


day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))


if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if day < days_in_month[month - 1]:
    day += 1
else:
    day = 1
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1


print("Next Date is:")
print("day =", day, "month =", month, "year =", year)

#Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
#CGPA=percentage/10
#CGPA range:
#0 to 3.4 -> F
#3.5 to 5.0->C+
#5.1 to 6->B
#6.1 to 7-> B+
#7.1 to 8-> A
#8.1 to 9->A+
#9.1 to 10-> O (Outstanding)


name = input("Enter Name: ")
roll_no = input("Enter Roll Number: ")
sapid = input("Enter SAP ID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")


print("\nEnter marks of five subjects:")
Maths = int(input("Maths: "))
python = int(input("Python: "))
chemistry = int(input("Chemistry: "))
english = int(input("English: "))
physics = int(input("Physics: "))

total_marks = Maths + python + chemistry + english + physics
percentage = total_marks / 5
cgpa = percentage / 10


if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"


print("\n----------- Grade Sheet -----------")
print("Name:", name)
print("Roll Number:", roll_no, "\tSAPID:", sapid)
print("Sem:", sem, "\t\tCourse:", course)

print("\nSubject Name\tMarks")
print("Maths:\t\t", Maths)
print("Python:\t\t", python)
print("Chemistry:\t", chemistry)
print("English:\t", english)
print("Physics:\t", physics)

print("\nPercentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)
