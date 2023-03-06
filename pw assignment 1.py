#!/usr/bin/env python
# coding: utf-8

# 1.  Explain with an example each when to use a for loop and a while loop.?
# 

# In[ ]:


# In general, we use a for loop when we want to iterate over a sequence of items, 
# and we use a while loop when we want to execute a block of code repeatedly, 
# as long as some condition is true.


# Q2.  Write a python program to print the sum and product of the first 10 natural numbers using for
# and while loop

# In[3]:


sum = 0
product = 1
for i in range(1,11):
    sum +=i
    product *= i
print("sum of 10 natural numbers is:",sum)
print("product of 10 natural numbers is:",product)


# Q3. Create a python program to compute the electricity bill for a household.
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# 
# 
# You are required to take the units of electricity consumed in a month from the user as input.
# 
# 
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# 310, the total electricity bill should be 2250.

# In[ ]:


#taking units from user 
units =int(input("Enter your units consumed "))
if units <= 100:
    bill =units * 4.5
elif units <= 200:
    bill = 100*4.5 +(units -200) *6
elif units <= 300:
    bill = 100*4.5 + 100*6 +(units -200) *10
else:
    bill = 100*4.5 + 100*6 + 100*10 +(units-300) *20
print("Electricty bill is: RS",bill


# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
# that list

# In[19]:


# BY FOR LOOP
cube_div_by_4_or_5 = []
for i in range (1,101):
    cube = i ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        
        cube_div_by_4_or_5.append(cube)
print(cube_div_by_4_or_5)


# In[ ]:


# BY WHILE LOOP
L1 =range(0,101)


# Q5.  Write a program to filter count vowels in the below-given string.
# 
# string = "I want to become a data scientist"
# 

# In[22]:


string = "I want to become a data scientist"
vowels ='aeiouAEIOU'
count = 0
for i in string:
    if i in vowels:
        count += 1
print(f"NUMBER OF VOWELS IN '{string}' is {count}")
        


# In[23]:


string = "I want to become a data scientist"

vowels = 'aeiouAEIOU'

count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{string}' is {count}")


# In[ ]:




