#median of three num
numbers_list=[] #number list to find the lenght of list
def median():
    try:
        number1=int(input("Enter The First Number"))
        number2=int(input("Enter The Second Number"))
        number3=int(input("Enter The Third Number")) 
     
        numbers_list.append(number1)
        numbers_list.append(number2)
        numbers_list.append(number3) 
        numbers_list.sort()
        mean_calculation=numbers_list[1]
        return mean_calculation

    except ValueError as ve:
        print(f"{ve}")
median()

#count the numbers of words in sentences


s=input("Enter a sentence")

words_count=s.split()
# words_array.split()
print(len(words_count))

#calculate the sum of digits in a numbers
import numpy as np
number_input=input("Enter Numbers sperated by commas")

numbers=number_input.split(",") 

numbers_list=np.array( [int (num)for num in numbers])

numbers_list.sum()

#check if a num is prime or not
num=int(input("Enter a Number"))

if num>1:
    isprime=True
    for i in range(2,num):
        if num % i==0:
            isprime=False
            break
    
    if isprime:
         print(f"{num} is prime")
    else:
         print(f"{num}is not prime")

#convert celcuis into farenhite
celsius=int(input("Enter temperature in Celsius:"))
def farhenite_coverter(c):
    farhenite=(c*9/5)+32
    print(f"Temperature in Fahrenheit:{farhenite}")

farhenite_coverter(celsius) 


#