# a
#  check  number positive  or negative or zero 

num = int(input("enter a number")) 
if num > 0 :
    print("num is postive")
elif num == 0 :
    print("num is zero")
else:
    print("num is negative")  

odd or even 

num = int(input("enter a number"))

if(num%2) == 0:
    print("even number")
else:
    print("odd number") 

vote eligibility 

num = int(input("enter a number"))
if num >= 18:
    print("eligible to vote")
else:
    print("not eligible") 



# greatest of 2 numbers 

num1=int(input("enter a num"))
num2=int(input("enter a num"))

str1 = 'num1 is greater' if num1 > num2  else 'num2 is greater'
print(str1) 


scores of students greater than 40 marks pass or else fail 

score = int(input("enter marks")) 
if score > 40:
    print("student is passed")
else:
    print("student is failed") 


#  days in a week print 1 == monday ...etc  

num = int(input("enter a number"))
if num == 1:
    print("day is monday")
elif num == 2 :
    print("day is tuesday")
elif num == 3:
    print("day is wendesday")
elif num == 4:
    print("day is thusday")
elif num == 5:
    print("day is friday")
elif num == 6:
    print("day is saturday")
elif num == 7:
    print("day is sunday")
else:
    print("not valid") 

# display name of month according to numbers 

num = int(input("enter a number"))
if num == 1:
    print(" january")
elif num == 2 :
    print("febuary")
elif num == 3:
    print("march")
elif num == 4:
    print(" april")
elif num == 5:
    print(" may")
elif num == 6:
    print(" june")
elif num == 7:
    print(" july")
else:
    print("not valid") 

# b.
# greatest of 3 numbers 


num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number")) 

str2 = 'first num is greater' if num1 > num2 and num1 > num3  else 'second num is greater'  if num2 > num3  else 'third  num is greater' 
print(str2)

# student grades based on marks 

marks = int(input("enter score"))

if marks >= 90:
    print("grade A") 
elif marks >= 80:
    print("grade B")
elif marks >=70:
    print("grade C")
elif marks < 70:
    print("fail")
else:
    print("not valid") 

# leap year  or not -
#  non centuary years should divide by 4
#  and century years should be divide by 400  

year = int(input("enter year"))
if year % 100 != 0 and year % 4 == 0:
    print("it is leap year")
elif year % 400 == 0 :
    print("it is leap year")
else:
    print("not a leap year") 

year = int(input("enter year"))
# if (year % 100 != 0 and year % 4 == 0 )or year % 400 == 0 :
#     print("it is leap year")
# else:
#     print("not a leap year") 

str1 = "it is leap year" if (year % 100 != 0 ) or year % 400 == 0  else "it is not a leap year" 
print(str1) 

to check if three sides length form a valid triangle. - s1 + s2 > s3 ; s2 + s3 > s1 ; s3 + s1 > s2

side1 = int(input("enter side1")) 
side2 = int(input("enter side2"))
side3 = int(input("enter side3")) 

# print("triangle possible" if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2) else "invalid triangle") 

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
    print("triangle possible")
else:
    print("invalid triangle") 

 check entered charcter are vowels  or consonants or neither 

str1 = input("enter a single character ").lower()

# vowels_str = 'aeiou'  
# if str1 in ['a','e','i','o','u']:
#     print("vowels")
# else:
#     print("consonants") 
if len(str1) > 1 or len(str1) == 0 :
    print("wont run")
else:
    if str1 in 'aeiou':
        print("vowels")
    elif str1.isalpha():
        print("consonants")
    else:
        print("neither") # numbers  



# battle of warriors


health1=int(input("enter health1")) 
health2=int(input("enter health2"))
attack1=int(input("enter attack1"))
attack2=int(input("enter attack2")) 

if attack1 > attack2:
    print("warrior 1 wins")
elif attack2 > attack1:
    print("warrior 2 wins")
else:
    if health1 > health2:
        print("warrarior 1 wins")
    elif health2 > health1:
        print("warrarior 2 wins")
    else:
        print("Draw")


# Q1: Nearest leap year in the increasing side 


year = int(input("enter a year"))

year += 1 
while True:
    if year % 100 != 0 and year % 400 == 0 and year %4 == 0:
        print("its a leap year")
        break 
    else:
        print("not a leap year")
      

# Q2 -Perfect number 6 => 1, 2, 3, 6 => Sum of 1, 2, 3 => 6

number = 28
sum = 0

for i in range(1, number):
    if number % i == 0:
        sum += i

if sum == number:
    print("perfect num")
else:
    print(" not a  perfect number.")

# write a program to print numbers from  -1 to -10
def print_neg_num():
    for i in range(-1, -11, -1):
        print(i)

print_neg_num() 

# sum of digits 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  
        n //= 10  
    return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

# add digits when num is  even 

def sum_of_digits_if_even(n):
    if n % 2 != 0:  
        return 0
    
    total = 0
    while n > 0:
        total += n % 10 
        n //= 10  
    return total

num = int(input("Enter a number: "))
result = sum_of_digits_if_even(num)

if result == 0:
    print("The number is odd, so the sum is 0.")
else:
    print("Sum of digits:", result) 

prime or not 

def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False 
    return True  

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number.")
else:
    print(num, "is NOT a Prime Number.") 


# even or odd 

num = int(input("enter a number:"))
if(num%2) == 0:
    print("even number")
if(num%2) != 0:
    print("odd number")

# positive or negative 

num1 = int(input("enter a number:"))
if(num1>0):
    print("positive number")
else:
    if(num1<0):
        print("negative number")

# maximum number in an array 

arr = [2,15,24,8,9]
max=arr[0]
for i in arr:
    if i<max:
        max=i
print("maximum number is : ", max)

# to check max and min numbers in an array 

arr1=[2,5,3,4,8,9,6,1]
max=arr1[0]
min=arr1[0]
for i in arr1:
    if i>max:
        max=i
for i in arr1:
    if i<min:
        min=i
print("maximum number is: ",max)
print("minimum number is: ",min)







