#!/usr/bin/env python
# coding: utf-8

# In[4]:


#                       Assignment No - 2


# In[9]:


#Qno.1- How do you comment code in Python? What are the different types of comments?
''' In python there are two types of comment are as follows:-
1-Single line comment= it is begin with '#'.
2-Multiline comment= if the statements are long then we use multi line comment.
it is begin with pair of tick.'''
#Example of Singleline comment:-
#This is my first comment
print("Hello World!")
#Example of Multiline Comment:-
'''This is my first Multiline comments
Welcome to my code'''
print("Welcome to My code!")




# In[28]:


'''Qno-2 What are variables in Python ? How do you declare  
and assign values to variables?'''
# variables are container they store values.
var1=12
var2='neha'
var3= 14.5
var4= 3+2j
a,b,c= 1,'neha',12.5 # assign multiple variable with values
print(a)
print(b)
print(c)


# In[33]:


'''Qno-3 How do you convert one data type to another in python?
Ans :-In Python, you can convert one data type to another using various built-in functions. 
This process is known as type casting or type conversion. '''
# Examples:-
var1=int(input("enter your value 1"))
var2=int(input("enter your value 2"))
add=print(var1+var2)
var3= 12
var4=7.5
var34=print(var3*var4)



# In[26]:


'''Qno-4 How do you execute a Python script from the command
line?
Ans:- Use python script_name.py to execute a Python script from the command line.'''


# In[2]:


'''Qno-5 Given a list my_list=[1,2,3,4,5], write the code to slice the list
and obtain sub-list[2,3]'''
my_list=[1,2,3,4,5]
print(my_list[1:3])


# In[15]:


'''Qno-6 What is a complex number in mathematics, and how is it represented
in Python?'''
'''Ans- In mathemstics , A complex number is a number in the form 𝑎
a+bi, where a and b are real numbers, and i is the imaginary unit with i*i=-1
In python, complex number is created by a+bj, where  a is the real part and
b is the imaginary.'''
#example-
z= (3+4j)
print(type(z))


# In[9]:


'''Qno-7 What is the correct way to decalare a variable named age and 
assign the value 25 to it?'''
age= 25



# In[16]:


'''Qno-8 Declare a variable named price and assign value 9.99 to it. what 
data type does this variable belong to?'''
price = 9.99 #this belongs the float data type because it stores the decimal value
print(price)
type(price)


# In[19]:


''' Qno-9 create a variable named name and assig your full name to it as a string
how would you print the value of this variable?'''
name="Neha Srivastava"#whenever we store any string value in variable we use single quote or double quote
print(name)
type(name)


# In[24]:


'''Qno-10 given the string "Hello, world!", extract the substring "World".'''
str="Hello,World!"
print(str[6:11])
type(str)


# In[25]:


'''Qno- 11 create a variable named is_student and assign it a boolean value 
indicating wheather you are currently a student or not.'''
is_student=True
print(is_student)


# In[ ]:




