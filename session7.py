#!/usr/bin/env python
# coding: utf-8

from numbers import Number
import math
import string
import requests
import random
from functools import reduce, partial


#Question1 
def fibonacci(n): 
    '''
    This function takes a number as input and determines if that number comes in the fibonacci series or not 
    input : Any Number
    Output : True/False

    '''
    fibArray = [0,1] 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(fibArray): 
        return fibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        fibArray.append(temp_fib) 
        return  temp_fib
def find_fib():
    '''
    List comprehension which iterates between 1 and 23 to generate fibonacci numbers upto 10000+
    '''
    fib_numbers = [fibonacci(i) for i in range(1,23)]
    return fib_numbers

# function using only list filter lambda that can tell whether a number is a Fibonacci number or not
def check_fibonocci(n):
    '''
    A function which decides fibonacci number or not using lambda function, filter
    '''
    l=[]
    if not isinstance(n,Number):
        raise ValueError("Please enter a number as valid Input")
    l.append(n)
    return bool(list(filter(lambda x:  x in find_fib(),l)))

#Question2 
#add 2 iterables a and b such that a is even and b is odd
f = lambda iter1,iter2: [x+y for x,y in zip(iter1,iter2) if x%2 == 0 and y%2!=0]

#strips every vowel from a string provided (tsai>>t s)
strip_vowels = lambda y: ''.join(list(filter(lambda x : x not in "AaEeIiOoUu",y)))

# ReLU function for a 1D array
relu_func = lambda x:  list(map(lambda y: y if y>0 else 0 ,x))

# a sigmoid function for a 1D array
sigmoid_func = lambda x :  list(map(lambda y: (1/(1+math.exp(-y))),x))

#takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
shift_alphabets = lambda input_string : ''.join(map(lambda x: chr(97+(ord(x) - 97)%21 + 5)  if ord(x) < 118 else chr(97+(ord(x)-97)%21),filter(lambda x: x in string.ascii_lowercase ,input_string.lower())))

#question 3 
def profanity_check(passage):
    '''
    This function reads a paragraph and filters all the obscene words 
    input : A passage
    Process : Checks if any of the words in the passage is in the profanity list
    Output : Filtered output
    '''
    target_url=' https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt'
    response = requests.get(target_url)
    checked_list = [i for i in passage.split() if i not in response.text]
    return checked_list
#Question4
#first
def add_even_no(l1):
    '''
    This function takes a list as input and returns the summation of all the even number digits 
    '''
    return reduce (lambda a,b: a+b if b%2==0  else a,l1,0)
#second
def find_biggest_char(l1):
    '''
    Given any list or string it finds out the biggest ascii character of the string 
    '''
    return reduce (lambda a,b: a if ord(a) > ord(b) else b,l1)
#third
def add_every_third_no(l1):
    '''
    Given any list of numbers this functions adds every 3rd number in the function 

    '''
    return reduce(lambda a,b: a+b if (l1.index(b)+1) %3 ==0 else a,l1,0)
#Question5
def generate_number_plate():
    '''
    Using randint, random.choice and list comprehensions, write an expression that
    generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, 
    and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
    '''
    return ['KA' + str(random.randint(10,100)) + random.choice(string.ascii_uppercase) +random.choice(string.ascii_uppercase) + str(random.randint(1000,10000)) for i in range(15)]
#Question6
def generate_reg_plate(state_code,area_code,alpha_code,reg_no):
    return state_code + str(area_code) + alpha_code + str(reg_no)
registration_number = partial(generate_reg_plate,area_code = random.randint(10,99),alpha_code = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase), reg_no = random.randint(1000,10000))
def get_number_plate(state_code):
    '''
    Using randint, random.choice and list comprehensions, write an expression that
    generates 15 random KADDAADDDD number plates where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 
    1000/9999 are hardcoded, but KA can be provided or any other state code 
    '''
    return [registration_number(state_code) for i in range(15)]

