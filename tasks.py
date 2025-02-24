# # a
# #  check  number positive  or negative or zero 

# num = int(input("enter a number")) 
# if num > 0 :
#     print("num is postive")
# elif num == 0 :
#     print("num is zero")
# else:
#     print("num is negative")  

# odd or even 

# num = int(input("enter a number"))

# if(num%2) == 0:
#     print("even number")
# else:
#     print("odd number") 

# vote eligibility 

# num = int(input("enter a number"))
# if num >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible") 



# # greatest of 2 numbers 

# num1=int(input("enter a num"))
# num2=int(input("enter a num"))

# str1 = 'num1 is greater' if num1 > num2  else 'num2 is greater'
# print(str1) 


# scores of students greater than 40 marks pass or else fail 

# score = int(input("enter marks")) 
# if score > 40:
#     print("student is passed")
# else:
#     print("student is failed") 


# #  days in a week print 1 == monday ...etc  

# num = int(input("enter a number"))
# if num == 1:
#     print("day is monday")
# elif num == 2 :
#     print("day is tuesday")
# elif num == 3:
#     print("day is wendesday")
# elif num == 4:
#     print("day is thusday")
# elif num == 5:
#     print("day is friday")
# elif num == 6:
#     print("day is saturday")
# elif num == 7:
#     print("day is sunday")
# else:
#     print("not valid") 

# # display name of month according to numbers 

# num = int(input("enter a number"))
# if num == 1:
#     print(" january")
# elif num == 2 :
#     print("febuary")
# elif num == 3:
#     print("march")
# elif num == 4:
#     print(" april")
# elif num == 5:
#     print(" may")
# elif num == 6:
#     print(" june")
# elif num == 7:
#     print(" july")
# else:
#     print("not valid") 

# # b.
# # greatest of 3 numbers 


# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# num3 = int(input("enter third number")) 

# str2 = 'first num is greater' if num1 > num2 and num1 > num3  else 'second num is greater'  if num2 > num3  else 'third  num is greater' 
# print(str2)

# # student grades based on marks 

# marks = int(input("enter score"))

# if marks >= 90:
#     print("grade A") 
# elif marks >= 80:
#     print("grade B")
# elif marks >=70:
#     print("grade C")
# elif marks < 70:
#     print("fail")
# else:
#     print("not valid") 

# # leap year  or not -
# #  non centuary years should divide by 4
# #  and century years should be divide by 400  

# year = int(input("enter year"))
# if year % 100 != 0 and year % 4 == 0:
#     print("it is leap year")
# elif year % 400 == 0 :
#     print("it is leap year")
# else:
#     print("not a leap year") 

# year = int(input("enter year"))
# # if (year % 100 != 0 and year % 4 == 0 )or year % 400 == 0 :
# #     print("it is leap year")
# # else:
# #     print("not a leap year") 

# str1 = "it is leap year" if (year % 100 != 0 ) or year % 400 == 0  else "it is not a leap year" 
# print(str1) 

# to check if three sides length form a valid triangle. - s1 + s2 > s3 ; s2 + s3 > s1 ; s3 + s1 > s2

# side1 = int(input("enter side1")) 
# side2 = int(input("enter side2"))
# side3 = int(input("enter side3")) 

# # print("triangle possible" if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2) else "invalid triangle") 

# if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
#     print("triangle possible")
# else:
#     print("invalid triangle") 

#  check entered charcter are vowels  or consonants or neither 

# str1 = input("enter a single character ").lower()

# # vowels_str = 'aeiou'  
# # if str1 in ['a','e','i','o','u']:
# #     print("vowels")
# # else:
# #     print("consonants") 
# if len(str1) > 1 or len(str1) == 0 :
#     print("wont run")
# else:
#     if str1 in 'aeiou':
#         print("vowels")
#     elif str1.isalpha():
#         print("consonants")
#     else:
#         print("neither") # numbers  



# # battle of warriors


# health1=int(input("enter health1")) 
# health2=int(input("enter health2"))
# attack1=int(input("enter attack1"))
# attack2=int(input("enter attack2")) 

# if attack1 > attack2:
#     print("warrior 1 wins")
# elif attack2 > attack1:
#     print("warrior 2 wins")
# else:
#     if health1 > health2:
#         print("warrarior 1 wins")
#     elif health2 > health1:
#         print("warrarior 2 wins")
#     else:
#         print("Draw")


# # Q1: Nearest leap year in the increasing side 


# year = int(input("enter a year"))

# year += 1 
# while True:
#     if year % 100 != 0 and year % 400 == 0 and year %4 == 0:
#         print("its a leap year")
#         break 
#     else:
#         print("not a leap year")
      

# # Q2 -Perfect number 6 => 1, 2, 3, 6 => Sum of 1, 2, 3 => 6

# number = 28
# sum = 0

# for i in range(1, number):
#     if number % i == 0:
#         sum += i

# if sum == number:
#     print("perfect num")
# else:
#     print(" not a  perfect number.")

# # write a program to print numbers from  -1 to -10
# def print_neg_num():
#     for i in range(-1, -11, -1):
#         print(i)

# print_neg_num() 

# # sum of digits 
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10  
#         n //= 10  
#     return total

# num = int(input("Enter a number: "))
# print("Sum of digits:", sum_of_digits(num))

# # add digits when num is  even 

# def sum_of_digits_if_even(n):
#     if n % 2 != 0:  
#         return 0
    
#     total = 0
#     while n > 0:
#         total += n % 10 
#         n //= 10  
#     return total

# num = int(input("Enter a number: "))
# result = sum_of_digits_if_even(num)

# if result == 0:
#     print("The number is odd, so the sum is 0.")
# else:
#     print("Sum of digits:", result) 

# prime or not 

# def is_prime(n):
#     if n < 2:
#         return False  
#     for i in range(2, int(n ** 0.5) + 1):  
#         if n % i == 0:
#             return False 
#     return True  

# num = int(input("Enter a number: "))

# if is_prime(num):
#     print(num, "is a Prime Number.")
# else:
#     print(num, "is NOT a Prime Number.") 


# # even or odd 

# num = int(input("enter a number:"))
# if(num%2) == 0:
#     print("even number")
# if(num%2) != 0:
#     print("odd number")

# # positive or negative 

# num1 = int(input("enter a number:"))
# if(num1>0):
#     print("positive number")
# else:
#     if(num1<0):
#         print("negative number")

# # maximum number in an array 

# arr = [2,15,24,8,9]
# max=arr[0]
# for i in arr:
#     if i<max:
#         max=i
# print("maximum number is : ", max)

# # to check max and min numbers in an array 

# arr1=[2,5,3,4,8,9,6,1]
# max=arr1[0]
# min=arr1[0]
# for i in arr1:
#     if i>max:
#         max=i
# for i in arr1:
#     if i<min:
#         min=i
# print("maximum number is: ",max)
# print("minimum number is: ",min) 


# # compare first digit and last digit in a number  (print equal - if there are  equal )

# ef compare_first_last_digit(num):
#     str1 = str(num)
#     if str1[0] == str1[-1]:
#         print("Equal")
#     else:
#         print("Not equal")

# num = int(input("Enter a number: "))
# compare_first_last_digit(num)  


# # reverse of negative numbers 

# def reverse_number(n):
#     if n >= 0:
#         return int(str(n)[::-1])
#     else:
#         return -int(str(n)[:0:-1])

# num = int(input("Enter a number: "))
# print("Reversed number:", reverse_number(num))


# # search of number in list with their indexes if found 

# def search_a_num(list, search_num):
#     """Search for a number in the list and print its index."""
#     index = 0  
#     for num in list:
#         if num == search_num:
#             return index  
#         index += 1  
#     return -1  

# list = [2, 4, 6, 8, 10, 0.2, -3]
# search_num = float(input("Enter a number to search: "))  

# index = search_a_num(list, search_num)
# if index != -1:
#     print(f"Found at index {index}")
# else:
#     print("Not found") 

#find duplicates 


# def find_duplicates(lst):
#     duplicates = set()
#     seen = set()

#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)

#     return list(duplicates)

# lst = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 
# duplicates = find_duplicates(lst)

# print("Duplicate elements:", duplicates) 



# def unique_elements(lst):
#     unique_list = []
#     for item in lst:


#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list


# lst = [1, 2, 2, 3, 4, 4, 5]
# print(unique_elements(lst))   



# 17 - 02 -task 

#Arrays/Lists Questions:
# 1. Sum of elements in a List.

# def sum_of_elements(lst):
#     sum = 0
#     for num in lst:
#         sum += num
#     return sum

# my_list = [11, 25, 43, 64, 15]
# result = sum_of_elements(my_list)
# print("The sum of elements in the list is:", result) 


# 2 .Finding the k Element which is present in a List.

# def find_kth_element(list, k):
#     if k < 0 or k >= len(list):
#         return "Index out of range"
#     return list[k]

# my_list = [10, 20, 30, 40, 50]
# k = 2
# result = find_kth_element(my_list, k)
# print(f"The {k}th element in the list is:", result) 


# reverse an array 

# def rev_array(arr):
#     return arr[::-1]

# my_array = [21, 12, 43, 34, 55]
# rev_array = rev_array(my_array)
# print("The reversed array is:", rev_array) 

#12) Find Largest & Smallest element in an list.  

# list1=[2,5,3,4,8,9,6,1]
# large=list1[0]
# small=list1[0]
# for i in list1:
#     if i>large:
#         large=i
# for i in list1:
#     if i<small:
#         small=i

# print("maximum number is: ",large)
# print("minimum number is: ",small)  


#3) Wap to print duplicates and unique numbers in an array/List.

# def find_duplicates(lst):
#     duplicates = set()
#     seen = set()

#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)

#     return list(duplicates)

# lst = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8,5,10]
# duplicates = find_duplicates(lst)

# print("Duplicate elements:", duplicates) 



# 18-02 task 
# 17 , 8 , 19 , 20  


# 8 

# Input list
# my_list = [568, 89, 112, 88, 571]

# incr_list = []

# for num in my_list:
#     digits = my_list(str(num))
#     if digits == sorted(digits):
#         incr_list.append(True)
#     else:
#         incr_list.append(False)

# print(incr_list)  # Output: [True, True, False, False, False]  

# 19 subset of 2 arrays 


# # arr1 = [1,3,4,5,2]
# # arr2 = [2,4,3,1,7.5,15] 
# arr1 = [2, 21, 5, 7, 3, 5, 7, 3, 1, 6, 14, 44]
# arr2 = [7, 3, 1]

# array1 = set(arr1)
# array2 = set(arr2)
# def check_subset(arr1, arr2):
#     for element in array2:
#         if element  in array1:
#             return "arr1 is  subset of arr2 "
#     return "arr1 is not a subset of arr2" 

# print(check_subset(arr1, arr2)) 


# 17 

# arr1 = [10, 30, 10, 20, 10, 20, 30, 10] 

# freq_res = []

# res = {}
# for element in arr1:
#     if element in res:
#         res[element] += 1
#     else:
#         res[element] = 1 

# freq_res.append(res)

# print(freq_res)   

# 20      count pairs 

# def check_pairs(arr):
#     res = {}

#     for element in arr:
#         if element in res:
#             res[element] += 1
#         else:
#             res[element] = 1 

#     pairs = 0 

#     for count in res.values():
#         pairs += count // 2 
#     return pairs 

# arr1 = [10, 20, 10, 30, 20, 20] 
# arr2 = [30, 50, 30, 50, 20, 50, 50, 20, 50, 50]
# print(check_pairs(arr1))
# print(check_pairs(arr2)) 


# 2D matrix -3 


# matrix = [
#     [2, 3, 4],
#     [3, 9, 2],
#     [3, 4, 1],
# ]

# sum_of_diagonals = [2, 9, 1, 4, 3]
# total_sum = sum(sum_of_diagonals)
# print(total_sum)  



# 5 count of digits 

# number = 2788
# number_str = str(number)
# count_digit = {}

# for digit in number_str:
#     if digit in count_digit:
#         count_digit[digit] += 1
#     else:
#         count_digit[digit] = 1

# for digit, count in count_digit.items():
#     print(count)  



# matrixes 
# 4 - print 2 diagonals of    8 1 3  , 4 2 9 , 3 1 5 

# matrix = [[8 ,1,3],[4,2,9],[3,1,5]]


# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if i == j:
#             print(matrix[i][j],end = " ")
#     print() 




# Mul and division using recursion

def multiple(p,q):
    if q == 0:
        return 0
    if q > 0:
      return p + multiple (p , q - 1)
    else:
       return multiple(p, -q)
print(multiple(4,5))

def division(a,b):
   if a == 0:
      return 0
   if a < b:
      return 0
   return 1 + division(a - b, b)
print(division(15, 5))

# Printing 1 to n numbers without multiple print statements and loops

def natural_number(num,num1 =1):
    if num1 > num:
        return 
    print(num1, end = " ")
    natural_number(num,num1 + 1)
natural_number(20)

# Sum of first n natural numbers using recursion

def natural_numbers_sum(num):
    sum = 0
    for i in range(1,num + 1):
        sum += i
    return sum
print(natural_numbers_sum(30))

def natural_numbers_sum(n):
     if n == 0:  
        return 0
     return n + natural_numbers_sum(n - 1)
print(natural_numbers_sum(20))

# Printing a list in reverse order using recursion

def print_reverse(lst, index=None):
    if index is None:
        index = len(lst) - 1  
    if index < 0:  
        return
    print(lst[index], end=" ") 
    print_reverse(lst, index - 1)  
my_list = [6,7,8,9,10]
print_reverse(my_list)               
                            































