 -------------------------------IF CONDITION--------------------------------------------------

1. Write a Python program to check if a number is positive. 
num = int(input("Enter the number :"))
if(num > 0):
    print("Poitive")




2. Print "Eligible to vote" if age is 18 or above. 
age = int(input("Enter the age : "))
if (age > 18):
    print("Eligible for vote")




3. Check if a number is divisible by 7. 
num = int(input("Enter the number:"))
if(num % 7 == 0):
    print("divisible")



4.Print "Pass" if marks are greater than 40. 
marks = int(input("Enter the marks of students :"))
if(marks > 40):
    print("Pass")



5. Check if a number is greater than 100. 
numb = int(input("Enter the number:"))
if(numb>100):
    print("Greater")



6. Display a message if temperature exceeds 45°C. 
temp = int(input("Enter the temperature :"))
if(temp>45):
    print("Temperature is too hot")



7. Check if a string length is more than 8 characters. 
char = input("Enter the character:")
if(len(char)>8):
    print("length of character is more than 8")




8. Print "Logged In" if password matches "admin123". 
password = input("Enter the correct password please: ")
if(password == "admin123"):
    print("Logged In")



9. Check if a number is a multiple of 10. 
numb = int(input("Enter the number :"))
if(numb % 10 == 0):
    print("it is a multiple of 10")



10. Print a warning if balance is below minimum limit.      
balance = int(input("Enter your balance:"))
if (balance < 1000):
    print("WARNING :  Your Balance is below minimum limit")

---------------------------------------IF_ELSE CONDITION-----------------------------------------


11. Check whether a number is even or odd.  
num = int(input("enter the number :"))
if(num % 2 == 0):
    print("even")
else:
    print("odd")




12.Find the largest of two numbers. 
n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the second number :"))
if(n1>n2):
    print("Largest number is :",n1)
else:
    print("Largest number is :",n2)




13. Check whether a person is eligible for driving license.
age = int(input("Enter the age of person:"))
if(age >= 18):
    print("eligible for driving license")
else:
    print("Not eligible for driving license")




14. Print "Pass" or "Fail" based on marks.
marks = int(input("Enter the marks of student:"))
if(marks >= 40):
    print("Pass")
else:
    print("Fail")




15. Check whether a number is positive or negative. 
numb = int(input("Enter the number:"))
if(numb >= 0):
    print("Positive")
else:
    print("Negative")




16. Check whether a character is a vowel or consonant. 
ch = input("Enter the character :")
if(ch=="A") or (ch == "E") or (ch == "I") or (ch == "O") or (ch== "U"):
    print("Vowel")
else:
    print("consonant")



17.  Check if a year is leap or not. 
year = int(input("Enter the year :"))
if(year % 4 == 0):
    print("Leap year")
else:
    print("Not leap year")



18. Print "Valid Password" or "Invalid Password".
password = input("Enter the correct password:")
if(password == 'Pragati12'):
    print("Valid Password")
else:
    print("Invalid Password")



19.  Determine whether salary is taxable or not.
Sal = int(input("Enter your Salary:"))
if(Sal> 50000):
    print("Taxable")
else:
    print("Not Taxable")



20. Check whether a number is greater than 50 or not.
num = int(input("Enter the number:"))
if(num > 50):
    print("Greater")
else:
    print("Not greater")


------------------------------NESTED IF_ELSE----------------------------------

21.  Find the largest of three numbers. 
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
if(n1>n2):
    if(n1>n3):
        print(n1)
    else:
        print(n3)
else:
    if(n2>n3):
       print(n2)
    else:
        print(n3)




22. Check whether a number is positive, negative, or zero.
n1 = int(input("Enter the first number:"))
if (n1 > 0):
    print("Positive")
else:
    if(n1<0):
        print("Negative")
    else:
        print("Zero")



23.Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60  

marks = int(input("Enter the marks of student:"))
if(marks >= 90):
    print("Grade is A")
else:
    if(marks >= 75):
        print("Grade is B")
    else:
        if (marks >= 60):
            print("Grade is C")
        else:
            print("Fail")



24. Check whether a triangle is equilateral, isosceles, or scalene.
a = int(input("Enter the first side of triangle:"))
b = int(input("Enter the second side of triangle:"))
c = int(input("Enter the third side of triangle:"))

if(a==b)and (b==c):
    print("Equilateral")
else:
    if(a==b) or (b==c) or (c==a):
        print("isosceles")
    else:
        print("scalene")
            


25. Check whether a character is uppercase, lowercase, digit, or special character.
ch = input("Enter the character :")
if(ch >= "A") and (ch <= "Z"):
    print("Uppercase")
else:
    if(ch >= "a") and (ch <= "z"):
        print("Lowercase")
    else:
        if(ch >= '0') and (ch <= '9'):
            print("Digit")
        else:
            print("Special character")




26. Calculate electricity bill using slab-wise rates. 
unit = int(input("Enter your electricity units:"))
if(unit <= 100):
    electricity_bill = unit * 5
else:
    if(unit<= 200):
        electricity_bill = unit * 7
    else:
        electricity_bill = unit * 10

print("Electricity bill is :", electricity_bill)




27.  Validate login using username and password.
username = "admin@123"
password = "639797"

a = input("Enter the username:")
b = input("Enter the correct password:")
if(a == username) and (b == password):
    print("Login Successfully")
else:
    print("Incorrect username and password")
        



28.  Check student result using marks of 3 subjects. 
physics = int(input("Enter the marks of physics:"))
Chemistry = int(input("Enter the marks of chemistry:"))
Maths = int(input("Enter the marks of Maths:"))

if (physics >= 40) and (Chemistry >= 40) and (Maths >= 40):
    print("Pass")
else:
    print("Fail")




29. Find the second largest number among three numbers.
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
if(n1>n2 and n1<n3) or (n1<n2 and n1>n3):
        print("second largest is :", n1)
else:
    if(n2>n1 and n2<n3) or (n2<n1 and n2>n3):
        print("second lagrest number is :",n2)
    else:
        print("second lagrest number is :",n3)




30. Check loan eligibility using age, salary, and credit score.
age = int(input("Enter your age:"))
salary = int(input("Enter your correct monthly salary:"))
credit_score = int(input("Enter your credit score :"))
if(age > 24 and salary > 45000 and credit_score > 8):
    print("Eligible")
else:
    print("Not eligible")



---------------------------ELIF FOR MULTIPLE CONDITIONS-----------------------------------------------------------------------------------------------

31.  Print day name using day number (1–7).
d_num = int(input("Enter the day number :"))
if(d_num == 1):
    print("Monday")
elif(d_num == 2):
    print("Tuesday")
elif(d_num == 3):
    print("Wednesday")
elif(d_num == 4):
    print("Thursday")
elif(d_num == 5):
    print("Friday")
elif(d_num == 6):
    print("Saturday")
elif(d_num == 7):
    print("Sunday")
else:
    print("Invalid day number ! Please enter only 1-7 number for searching the day name")




32. Print month name using month number.
m_num = int(input("Enter the month number for seraching a month name:"))
if(m_num == 1):
    print("January")
elif(m_num == 2):
    print("February")
elif(m_num == 3):
    print("March")
elif(m_num == 4):
    print("April")
elif(m_num == 5):
    print("May")
elif(m_num == 6):
    print("June")
elif(m_num == 7):
    print("July")
elif(m_num == 8):
    print("August")
elif(m_num == 9):
    print("September")
elif(m_num == 10):
    print("October")
elif(m_num == 11):
    print("November")
elif(m_num == 12):
    print("December")
else:
    print("Invalid Month number !Please enter only 1-12 month numbers for searching month name")




33.  Display grade based on percentage. 
per = int(input("Enter your percentage for searching of grade :"))
if(per >= 90):
    print("Grade is A")
elif(per >= 75):
    print("Grade is B")
elif(per >= 60):
    print("Grade is C")
elif(per >= 45):
    print("Grade is D")
elif(per >=33):
    print("Grade is E")
else:
    print("Fail")




34. Display bonus percentage based on experience years. 
salary = int(input("Enter your salary:"))
exp = int(input("Enter your experience in years:"))
if(exp >= 15):
    bonus = (salary * 25)/100
elif(exp >= 10):
    bonus = (salary * 18)/100
elif(exp >= 5):
    bonus = (salary * 12)/100
else:
    bonus = (salary * 7)/100

total_salary_with_bonus = salary + bonus
print(total_salary_with_bonus)
                   



35. Identify traffic signal meaning.
signal = input("Enter the colour of light:")
if(signal == "Red"):
    print("Stop")
elif(signal == "Green"):
    print("Go")
elif(signal == "Yellow"):
    print("Ready/Wait for go")
else:
    print("Nothing")




36.  Categorize temperature as Cold / Warm / Hot.
temp = int(input("Enter the temperature of weather:"))
if(temp >= 35):
    print("Hot")
elif(temp >= 22):
    print("Warm")
else:
    print("Cold")





37. Categorize employee based on salary range.

salary = int(input("Enter your salary:"))
if(salary >= 90000):
    print("Director")
elif(salary >= 75000):
    print("Manager")
elif(salary >= 50000):
    print("HR")
elif(salary >= 35000):
    print("Team Leader")
elif(salary >= 20000):
    print("Junior")
else:
    print("Trainee")





38.  Print discount percentage based on purchase amount.

amount = int(input("Enter the purchase amount:"))
if(amount <= 1000):
    discount = (amount * 5)/100
elif(amount > 1000):
    discount = (amount * 10)/100
elif(amount > 5000):
    discount = (amount * 15)/100
elif(amount > 10000):
    discount = (amount * 20)/100
else:
    discount = 0
Total_Amount = amount - discount
print(Total_Amount)





39.  Identify number type: single-digit / double-digit / multi-digit.

numb = int(input("Enter the number :"))
if(numb >=0 and numb <= 9):
    print("Single-Digit")
elif(numb >= 10 and numb <= 99):
    print("Double-Digit")
else:
    print("Multi-digit")
 




40.  Assign performance rating: Poor / Average / Good / Excellent.

rating = int(input("Enter the rating of our performance:"))
if(rating == 4 or rating == 5):
    print("Excellent")
elif(rating == 4):
    print("Good")
elif(rating == 3):
    print("Average")
elif(rating == 2 or rating == 1):
    print("Poor")


-----------------------------------------COMPLEX CONDITION (AND/OR/NOT)-----------------------------------------------------
    

41. Check whether a number is divisible by 5 and 11.

num = int(input("Enter the number :"))
if(num % 5 == 0 and num % 11 == 0):
    print("divisible")
else:
    print("Not divisible")




42. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700    

age = int(input("Enter your age:"))
salary = int(input("Enter your correct monthly salary:"))
credit_score = int(input("Enter your credit score :"))
if(age >= 21 and salary >= 25000 and credit_score >= 700):
    print("Eligible")
else:
    print("Not Eligible")





43. Validate login using username AND password.

username = "admin@123"
password = "112233"

u = input("Enter the username:")
p = input("Enter the password:")
if(u == username and p == password):
    print("Login successfully")
else:
    print("Incorrect username and password")





44.  Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50 

Sub_1 = int(input("Enter the marks of first subject:"))
Sub_2 = int(input("Enter the marks of second subject:"))
Sub_3 = int(input("Enter the marks of third subject:"))
Sub_4 = int(input("Enter the marks of fourth subject:"))
Sub_5 = int(input("Enter the marks of fifth subject:"))

Average = (Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5)/5
if(Sub_1>=40 and Sub_2>=40 and Sub_3>=40 and Sub_4>=40 and Sub_5>=40 and Average >= 50):
    print("Pass")
else:
    print("Fail")
    




45.  Check if a number lies between 10 and 100.
num = int(input("Enter the number :"))
if(num >= 10 and num <= 100):
    print("lies")
else:
    print("Not")






46.  Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available.      

attendance = int(input("Enter the percentage of attendance:"))
medical_certificate = input("Enter availability (yes/no): ")
if(attendance >= 75 and medical_certificate == "yes"):
    print("Eligible")
else:
    print("Not Eligible")




47.  Validate a date using conditions.
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Function to check leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Days in each month
if month in [1, 3, 5, 7, 8, 10, 12]:
    max_day = 31
elif month in [4, 6, 9, 11]:
    max_day = 30
elif month == 2:
    if is_leap_year(year):
        max_day = 29
    else:
        max_day = 28
else:
    max_day = 0  # Invalid month

# Validate the date
if 1 <= day <= max_day:
    print(f"{day}/{month}/{year} is a valid date.")
else:
    print(f"{day}/{month}/{year} is NOT a valid date.")







48.  Check whether an email format is valid.
email = input("Enter the email:")
if('@' in email and '.' in email):
    print("Valid Email")
else:
    print("Not Valid")





49. Determine insurance eligibility using age, health status, and income.
age = int(input("Enter the age of person:"))
Health_status = input("Enter the health status (Fit/Disease):")
income = int(input("Enter the salary of person:"))
if(age >= 18 and age <= 65) and (Health_status == "Fit" ) and (income >= 25000):
    print("Eligible")
else:
    print("Not Eligible")
    




50. Check leap year using complete leap year logic.
Year = int(input("Enter the year:"))
if(Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0): 
    print("Leap Year")
else:
    print("Not Leap Year")





-------------------------------------------------------------- INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS--------------------------------------------------

51.  Write a Python program to calculate income tax using slabs. 

salary = int(input("Enter your salary:"))
if(salary <= 250000):
    tax = 0
elif(salary > 250000 and salary <= 500000):
        tax = (salary * 5)/100
elif(salary > 500000 and salary <= 1000000):
    tax = (salary * 10)/100
else:
    tax = (salary * 20)/100

Final_salary = salary - tax
print(Final_salary)





52. Create an ATM withdrawal program with balance checks.

balance = 10000   
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")





53. Check promotion eligibility using experience and performance.

experience = int(input("Enter the experience of employee :"))
Performance = input("Enter the performance (Excellent, Good, Aveage,Poor):")

if(experience >= 8) and (Performance == "Excellent" or Performance == "Good"):
    print("Eligible for promotion")
else:
    print("Not eligible for promotion")
          
    




54.  Implement a grading system using nested if–else. 

marks = int(input("Enter the marks of student:"))
if(marks >= 90 and marks <= 100):
    print("Grade - A")
else:
    if(marks >= 75 and marks <= 89):
        print("Grade - B")
    else:
        if(marks >= 60 and marks <= 74):
            print("Grade - C")
        else:
            if(marks >= 45 and marks <= 59):
                print("Grade - D")
            else:
                if(marks >= 33 and marks <= 44):
                    print("Grade - E")
                else:
                    print("Fail")



55.  Validate strong password using multiple conditions.

import string

password = input("Enter a password: ")

# Conditions
if (len(password) >= 8 and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in string.punctuation for c in password)):
    print("Strong password")
else:
    print("Weak password")




56. Calculate delivery charges based on location and order amount.

location = input("Enter the location of delivery (local/outstation):")
amount_of_parcel = int(input("Enter the amount of order:"))

if(location == "local" and amount_of_parcel >= 1000):
    delivery_charges = 0
elif(location == "local" and amount_of_parcel < 1000):
    delivery_charges = 50
elif(location == "outstation" and amount_of_parcel >= 2000):
     delivery_charges = 100
elif(location == "outstation" and amount_of_parcel < 2000):
    delivery_charges = 200
else:
    delivery_charges = 0
    print("Invalid location entered")
    
Total_amount_of_order = amount_of_parcel + delivery_charges
print(Total_amount_of_order)








57. Determine online exam qualification.

attendance = int(input("Enter the student percentage of attendance:"))
Fee_status = input("Enter the status of fees (paid/unpaid):")
registration = input("Enter the status of registration (Done/No):")

if(attendance >= 75 and Fee_status == "paid" and registration == "Done"):
    print("Eligible")
else:
    print("Not Eligible")




58. Create movie ticket pricing logic based on age & show time.

age = int(input("Enter the age of person:"))
show_time = input("Enter the show time of movie (morning/afternoon/eveneing/night):")
ticket_price = 500   

if age < 12:
    if show_time == "morning":
        discount = 50
    elif show_time == "afternoon":
        discount = 30
    else:
        discount = 20

elif age <= 60:   
    if show_time == "morning":
        discount = 20
    elif show_time == "afternoon":
        discount = 10
    else:
        discount = 0

else:   
    if show_time == "morning":
        discount = 40
    elif show_time == "afternoon":
        discount = 30
    else:
        discount = 25

final_price = ticket_price - (ticket_price * discount / 100)

print("Final ticket price is:", final_price)






59. . Determine bank account type based on balance. 

balance = int(input("Enter the balance of your account:"))
if(balance <= 5000):
    print("Saving Account")
elif(balance <= 50000):
    print("Regular Saving Account")
elif(balance <= 200000):
    print("Premium Account")
elif(balance <= 500000):
    print("Gold Account")
else:
    print("Diamond Account")
    



60. Create a menu-driven program using if–elif–else.

print("===== Menu =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid choi

























































































