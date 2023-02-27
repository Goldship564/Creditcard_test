# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:23:17 2023

@author: Nicholas
"""
    
sum_odd = 0 
sum_even = 0 
total = 0 
num = input("Welcome, please enter your credit card number: ")
num = num.replace("-", "")
num = num.replace(" ", "")



N = 2 

new_list = []
for index in range (0,N):
    new_list.append(num[index])
#print(new_list)



num = num[::-1]

for i in num[::2]:
    sum_odd += int(i)
    
for i in num[1::2]:
    i = int(i) * 2
    if i >=10:
        sum_even += (1+(i % 10))
    else:
        sum_even += i 
        
total = sum_odd + sum_even

if total % 10 == 0:
    print("This is an valid card number")
    
    if new_list == ["3","4"]:
        print("It is a American Express Card")
    if new_list == ["3","7"]:
        print("It is a American Express Card") 
    if new_list == ["5","1"]:
        print("It is a Master Card")
    if new_list == ["5","2"]:
        print("It is a Master Card")
    if new_list == ["5","3"]:
        print("It is a Master Card")
    if new_list == ["5","4"]:
        print("It is a Master Card")
    if new_list == ["5","5"]:
        print("It is a Master Card")
    if new_list == ["4",""]:
        print("It is a Visa Card")
    
else: 
    print("Sorry, this is an invalid card number")

if len(num)<10:
    print("credit card number is too short")
if len(num)>16:
    print("credit card number is too long")

 


