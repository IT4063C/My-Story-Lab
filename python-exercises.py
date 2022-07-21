#!/usr/bin/env python
# coding: utf-8

# # Python Exercises
# ## Emojis Legend
# - 👨🏻‍💻 - Tells you about something specific you need to do.
# - 🦉 - Will tell you about some hints, tips and best practices
# - 📜 - provides links to documentations
# - 🚩 - marks a good spot for you to commit your code to git

# In[27]:


# 🦉 Generally, it is a good practice to import the modules you use at the top of your code.
# 🦉 You can also import modules from the Python standard library, or from third-party libraries installed using (pip, conda, poetry, etc.).
# 👨🏻‍💻 Use this Code block to import the modules you will need.
import numpy as np


# ## Exercise
# In one line and (one line only), create a numpy array that contains a range of evenly spaced intervals. Starting with number 3, ending with the number 15, with an intervals of 3
# > Output should look like `array([ 3,  6,  9, 12])`
# 
# 📜 [Here's a link to the `numpy.arange` function](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange)

# In[28]:


np.arange(3,15,3)


# ## Exercise
# in the following cell, I used the `numpy.empty` function to generate a 2D array (2x2).
# Although, It's supposed to be empty, it seems to have generated some values. Why?
# 
# 📜 [`numpy.empty` function](https://numpy.org/doc/stable/reference/generated/numpy.empty.html)
# 

# In[ ]:





# In[12]:


np.empty([2,2])


# 👨🏻‍💻 Enter your Answer here:

# ## Exercise
# Given an array `some_array` of a certain shape, create another array of the same shape with the a space for input
# 
# - 📜 [`numpy.copy` function](https://numpy.org/doc/stable/reference/generated/numpy.copy.html)
# - 📜 [`numpy.fill` function](https://numpy.org/doc/stable/reference/generated/numpy.chararray.fill.htm)
# - 📜 [`numpy.full_like` function](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html)

# In[24]:


some_array = np.array([1,2,3,4,5])
print(some_array.shape)


# ## Exercise
# given 2 numpy arrays of strings, one containing first names, and the other containing last names. Concatenate the arrays into a single array, with full names
# 
# 🦉 I'm not going to give you the answer directly. However, these doc links should guide you
# 
# - 📜 [`numpy.concatenate` function](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)
# - 📜 [`numpy.char.add` function](https://numpy.org/doc/stable/reference/generated/numpy.char.add.html)
# 

# In[23]:


first_names = np.array(["Bob", "Jane", "Mallory"])
last_names = np.array(["Smith", "Jones", "Williams"])

# 👨🏻‍💻 a simple concatenation would look like this: ['BobSmith' 'JaneJones' 'MalloryWilliams']


spaces = np.copy(first_names)
spaces.fill(" ")
spaces2 = np.full_like(first_names, " ")
print(spaces2)

# 👨🏻‍💻 Use the np.concatenate function to concatenate the first_names and last_names arrays.
# 🦉 You can't simply use the cancatenate function to concatenate the first_names and last_names arrays. This would combine the arrays into a single array. Like this: ['Bob' 'Jane' 'Mallory' ' ' ' ' ' ' 'Smith' 'Jones' 'Williams']
# full_names = np.concatenate((first_names, spaces, last_names))
_full_names = np.char.add(first_names, spaces2)
full_names = np.char.add(_full_names, last_names)
print(full_names)


# ## Exercise 
# Wrap the above in a function named `get_full_names(...)` such that you only call one function passing in first_names and last_names as parameters, and it would RETURN an array of the same length with the full names

# In[26]:


def get_full_names(first_names, last_names):
  spaces = np.full_like(first_names, " ")
  first_names_with_spaces = np.char.add(first_names, spaces)
  return np.char.add(first_names_with_spaces, last_names)

# All of the following calls should work
print(get_full_names(["Tom", "Jane"], ["Smith", "Jones"]))
print(get_full_names(["Tom", "Jane", "John"], ["Smith", "Jones", "Reed"]))


# ## Exercise
# Write a program that RETURNS (not prints) the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# In[2]:


# 🦉 Use this Code block to define your functions.
def fizzbuzz():
    return 0
    # for i in range(1, 51):
    #     if i % 3 == 0 and i % 5 == 0:
    #         print("FizzBuzz")
    #     elif i % 3 == 0:
    #         print("Fizz")
    #     elif i % 5 == 0:
    #         print("Buzz")
    #     else:
    #         print(i)

# 👨🏻‍💻 What's missing here for the function to execute?


# ## Exercise
# Write a python function to check whether a given number is even or odd

# In[ ]:


def is_even_or_odd(n):
  if n % 2 == 0:
      return "even"
  else:
      return "odd"


# ## Exercise
# write a python function to convert the temperature from Celsius to Fahrenheit $ F^{\circ}=C^{\circ}\times\frac{9}{5}+32 $

# In[ ]:


def convert_celsius_to_fahrenheit(celsius):
  return celsius * 9 / 5 + 32


# ## Exercise
# write a python function to get the average of a set of integers

# In[ ]:


def get_average_of_numbers(numbers):
  return np.mean(numbers)


# ## Exercise
# get the circumference and area of a circle given a radius
# $$ Circumference = 2 \pi \times radius $$
# $$ Area = \pi \times radius^{2}  $$

# In[ ]:


def get_area_and_circumference_of_circle(radius):
  return np.pi * radius ** 2, 2 * np.pi * radius


# ## Exercise
# write a python function that, given a year, returns `True` if the year is a leap year, and `False` if it's not.

# In[2]:


def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


# In[11]:


try:
  leap_years = (2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048)
  not_leap_years = (2000, 2005, 2009, 2013, 2017, 2021, 2025, 2029, 2033, 2037, 2041, 2045, 2049)
  for year in leap_years:
    assert is_leap_year(year) == True, "❌ Expected {} to be a leap year".format(year)
  for year in not_leap_years:
    assert is_leap_year(year) == False, "❌ Expected {} to be a not leap year".format(year)
except AssertionError as e:
  print(e)


# ## Wrap up
# Just to get familiar with working with pure python files `*.py` files, export this notebook to a python script file and make sure it runs. 
# You should be able to get something that likes like this. 
# ![final page](#)

# In[13]:


get_ipython().system('jupyter nbconvert --to python python-exercises.ipynb')
get_ipython().system('git add python-exercises.py')
get_ipython().system('git commit -am "push py file"')


# In[ ]:




