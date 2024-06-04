#!/usr/bin/env python
# coding: utf-8

# In[6]:


def star_pattern(n):
    # Upper part of Pascal Triangle
    for i in range(1, n + 1):
        print('*' * i)
    # Lower part of Pascal Triangle
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Call the function with the desired number of rows
star_pattern(5)


# In[2]:


# Provided list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Loop through the list and print elements at odd indexes
for index in range(len(my_list)):
    if index % 2 != 0:  # Check if the index is odd
        print(my_list[index])


# In[3]:


# Given list
x = [23, 'Python', 23.98]

# Print the original list
print(x)

# Create a new list to store the types of the elements
types = [type(element) for element in x]

# Print the list of types
print(types)


# In[4]:


def get_unique_items(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    unique_list = list(set(input_list))
    return unique_list

# Sample list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

# Get the unique list
unique_list = get_unique_items(sample_list)

# Print the unique list
print(unique_list)


# In[5]:


def count_upper_and_lower(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

# Sample input
input_string = 'The quick Brow Fox'

# Get the counts of upper-case and lower-case characters
upper_count, lower_count = count_upper_and_lower(input_string)

# Print the results
print(f"No. of Upper-case characters: {upper_count}")
print(f"No. of Lower-case characters: {lower_count}")


# In[ ]:




