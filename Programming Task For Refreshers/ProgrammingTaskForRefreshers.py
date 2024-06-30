#calculate the area of rectangle
lenght_input=int(input("enter the length of rectangle")) #take lenght input from user 
width_input=int(input("enter the width of rectangle")) #take width input from user 

def Rectangle_Area():
    formula_calulation=lenght_input*width_input #area formula lenght*width
    print(f"The Area of Rectangle is {formula_calulation}") #output shown
Rectangle_Area()    

#check if a number is even or odd
number_input=int(input("Enter the number:"))

def Even_Odd():
    if number_input % 2 ==0:
        print(f"{number_input} is even")
    else:
        print(f"{number_input} is odd")

Even_Odd() 


#reverse a string


def Reverse_String():
    
        string_taken=str(input("Enter The String:"))

        rev_result=string_taken[::-1]
        print(f" {string_taken} is reversed into {rev_result} ")

       
    
Reverse_String()        


#find a factorial of a number

import math
fac_num=int(input("Enter the no for factorial") )
fac_result=math.factorial(fac_num)
print(f"the factorial of {fac_num} is {fac_result}")




#check if a string is palindrome or not
user_palindrome=input("Enter a String:")

remove_spaces=user_palindrome.replace(" ","").lower()

revrsed_check=remove_spaces[::-1]

if remove_spaces==revrsed_check:
    print(f""" "{user_palindrome}" is palindrome word""")
else:
   print(f""" "{user_palindrome}" is not palindrome word""")


#generate the fabonacci series upto n terms

def fabonacci_series():
    number1=0
    number2=1
    for i in range(1,11):
        thirdnum=number1+number2
        print(thirdnum)
        number1=number2
        number2=thirdnum
    
    

fabonacci_series() 


#find the largest among three numbers

print("find Largest Among Three Number") 

number_1=int(input("Enter The First Number:"))
number_2=int(input("Enter The  Second Number:"))
number_3=int(input("Enter The Third Number:"))

numbers_list=[] 

def largrest_num(n1,n2,n3):
    numbers_list.append(n1)
    numbers_list.append(n2)
    numbers_list.append(n3)
    return numbers_list.sort()

    

largrest_num(number_1,number_2,number_3)


print(f"\n\n\nthe largest number between {numbers_list} is {numbers_list[-1]}")
    
#calculate the simple interest
print("calculate the simple intrest".center(100).title())

principal_amount=float(input("Enter the principal amount"))
rate_intrest=float(input("Enter the rate of amount"))
time_period=float(input("Enter the time period in years"))


def intrest_calculate(pa,ri,tp):
    multiplication=ri*tp
    divison=pa/multiplication
    print(f"\n\n\n\nThe simple intrest is {divison}")
    
intrest_calculate(principal_amount,rate_intrest,time_period)


#check a year is leap or not 


def leap_calculation():
    try:
      y=int(input("Enter The Year To Calculate"))
      if y%4==0:
            print(f""" {y} is "Leap year" """)
      else:
        print(f""" {y} is "not Leap year" """)   
    except ValueError as ve:
        print( f"{ve}")
      
  
  

leap_calculation()

    